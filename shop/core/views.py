from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django.db import models
from core.dao.book_dao import BookDAO
from core.dao.customer_dao import CustomerDAO
from core.dao.cart_dao import CartDAO
from core.models import (
    Customer, Book, Category, Rating, Wishlist, WishlistItem,
    Order, CartItem, Payment, Cart, Address, OrderHistory
)
from datetime import datetime
import json


def get_context(request):
    """Helper function to add user context to all templates"""
    context = {'is_logged_in': 'customer_id' in request.session}
    
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(id=request.session['customer_id'])
            context['customer'] = customer
            context['cart_count'] = CartItem.objects.filter(
                cart__customer=customer, 
                cart__is_active=True
            ).count()
        except Customer.DoesNotExist:
            del request.session['customer_id']
    
    return context


def register(request):
    """
    Handle customer registration
    GET: Display registration form
    POST: Create new customer account
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '').strip()
        
        errors = []
        
        if not name:
            errors.append('Tên là bắt buộc')
        if not email:
            errors.append('Email là bắt buộc')
        if not password or len(password) < 6:
            errors.append('Mật khẩu phải có ít nhất 6 ký tự')
        
        if Customer.objects.filter(email=email).exists():
            errors.append('Email đã được đăng ký')
        
        if errors:
            return render(request, 'core/register.html', {'errors': errors})
        
        # Create customer
        customer = Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=make_password(password)
        )
        
        # Create empty cart
        Cart.objects.create(customer=customer, is_active=True)
        
        return redirect('core:login')
    
    context = get_context(request)
    return render(request, 'core/register.html', context)


def login(request):
    """
    Handle customer login
    GET: Display login form
    POST: Authenticate customer and create session
    """
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        if not email or not password:
            return render(request, 'core/login.html', {
                'error': 'Email và mật khẩu là bắt buộc'
            })
        
        try:
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id
                return redirect('core:book_list')
        except Customer.DoesNotExist:
            pass
        
        return render(request, 'core/login.html', {
            'error': 'Email hoặc mật khẩu không chính xác'
        })
    
    context = get_context(request)
    return render(request, 'core/login.html', context)


def logout(request):
    """Handle customer logout"""
    if 'customer_id' in request.session:
        del request.session['customer_id']
    return redirect('core:book_list')


def book_list(request):
    """
    Display all books in the catalog with category filtering
    """
    books = Book.objects.all()
    categories = Category.objects.all()
    selected_category = None
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        try:
            selected_category = Category.objects.get(id=category_id)
            books = books.filter(category=selected_category)
        except Category.DoesNotExist:
            pass
    
    # Search by title or author
    search_query = request.GET.get('search', '').strip()
    if search_query:
        books = books.filter(title__icontains=search_query) | \
                books.filter(author__name__icontains=search_query)
    
    # Sort
    sort = request.GET.get('sort', 'title')
    if sort == 'price_asc':
        books = books.order_by('price')
    elif sort == 'price_desc':
        books = books.order_by('-price')
    elif sort == 'rating':
        books = books.annotate(avg_rating=models.Avg('rating__score')).order_by('-avg_rating')
    else:
        books = books.order_by('title')
    
    context = get_context(request)
    context.update({
        'books': books,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
    })
    
    return render(request, 'core/books.html', context)


def book_detail(request, book_id):
    """
    Display detailed book information, ratings, reviews
    """
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('core:book_list')
    
    ratings = Rating.objects.filter(book=book).select_related('customer')
    avg_rating = sum(r.score for r in ratings) / len(ratings) if ratings else 0
    
    context = get_context(request)
    context.update({
        'book': book,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'rating_count': len(ratings),
    })
    
    # Check if in wishlist
    if 'customer_id' in request.session:
        try:
            customer = Customer.objects.get(id=request.session['customer_id'])
            wishlist = Wishlist.objects.get(customer=customer)
            context['in_wishlist'] = WishlistItem.objects.filter(
                wishlist=wishlist, book=book
            ).exists()
        except (Customer.DoesNotExist, Wishlist.DoesNotExist):
            pass
    
    return render(request, 'core/book_detail.html', context)


def add_to_cart(request, book_id):
    """Add a book to customer's cart"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        book = Book.objects.get(id=book_id)
        cart = Cart.objects.get(customer=customer, is_active=True)
        
        quantity = int(request.POST.get('quantity', 1))
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Đã thêm vào giỏ hàng'})
        
        return redirect('core:book_detail', book_id=book_id)
    
    except (Customer.DoesNotExist, Book.DoesNotExist, Cart.DoesNotExist):
        return redirect('core:login')


def cart_view(request):
    """Display customer's shopping cart"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        cart = Cart.objects.get(customer=customer, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart).select_related('book')
        
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        
        context = get_context(request)
        context.update({
            'cart': cart,
            'cart_items': cart_items,
            'total_price': total_price,
        })
        
        return render(request, 'core/cart.html', context)
    
    except (Customer.DoesNotExist, Cart.DoesNotExist):
        return redirect('core:login')


def update_cart_item(request, cart_item_id):
    """Update quantity of an item in the cart"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    if request.method == 'POST':
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            customer = Customer.objects.get(id=request.session['customer_id'])
            
            if cart_item.cart.customer != customer:
                return redirect('core:login')
            
            quantity = int(request.POST.get('quantity', 1))
            
            if quantity <= 0:
                cart_item.delete()
            else:
                cart_item.quantity = quantity
                cart_item.save()
        
        except (CartItem.DoesNotExist, Customer.DoesNotExist):
            pass
    
    return redirect('core:cart_view')


def remove_from_cart(request, cart_item_id):
    """Remove an item from customer's cart"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        customer = Customer.objects.get(id=request.session['customer_id'])
        
        if cart_item.cart.customer == customer:
            cart_item.delete()
    
    except (CartItem.DoesNotExist, Customer.DoesNotExist):
        pass
    
    return redirect('core:cart_view')


def checkout(request):
    """Handle order checkout and payment method selection"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        cart = Cart.objects.get(customer=customer, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)
        
        if not cart_items.exists():
            return redirect('core:cart_view')
        
        if request.method == 'POST':
            # Bank transfer only
            request.session['payment_method'] = 'bank_transfer'
            request.session.modified = True
            return redirect('core:payment_processing')
        
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        
        context = get_context(request)
        context.update({
            'cart_items': cart_items,
            'total_price': total_price,
            'customer': customer,
        })
        
        return render(request, 'core/checkout.html', context)
    
    except (Customer.DoesNotExist, Cart.DoesNotExist):
        return redirect('core:login')


def payment_processing(request):
    """Process payment and create order"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        cart = Cart.objects.get(customer=customer, is_active=True)
        cart_items = CartItem.objects.filter(cart=cart)
        
        if not cart_items.exists():
            return redirect('core:cart_view')
        
        if request.method == 'POST':
            payment_method = request.session.get('payment_method', 'credit_card')
            payment_status = request.POST.get('payment_status', 'completed')
            
            try:
                address = customer.address
            except Address.DoesNotExist:
                address = None
            
            total_price = sum(item.book.price * item.quantity for item in cart_items)
            
            # Create order
            order = Order.objects.create(
                customer=customer,
                address=address,
                status='pending',
                total_price=total_price
            )
            
            # Create payment
            payment = Payment.objects.create(
                order=order,
                amount=total_price,
                status=payment_status
            )
            
            # Create order history
            OrderHistory.objects.create(
                customer=customer,
                order=order
            )
            
            # Clear cart
            cart.is_active = False
            cart.save()
            
            # Clear session payment method
            if 'payment_method' in request.session:
                del request.session['payment_method']
            request.session.modified = True
            
            return redirect('core:order_confirmation', order_id=order.id)
        
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        
        context = get_context(request)
        context.update({
            'cart_items': cart_items,
            'total_price': total_price,
            'customer': customer,
        })
        
        return render(request, 'core/payment_processing.html', context)
    
    except (Customer.DoesNotExist, Cart.DoesNotExist):
        return redirect('core:login')


def order_confirmation(request, order_id):
    """Display order confirmation"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        order = Order.objects.get(id=order_id)
        customer = Customer.objects.get(id=request.session['customer_id'])
        
        if order.customer != customer:
            return redirect('core:login')
        
        context = get_context(request)
        context.update({
            'order': order,
        })
        
        return render(request, 'core/order_confirmation.html', context)
    
    except (Order.DoesNotExist, Customer.DoesNotExist):
        return redirect('core:login')

        return redirect('core:login')


def add_rating(request, book_id):
    """Add or update rating for a book"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(id=request.session['customer_id'])
            book = Book.objects.get(id=book_id)
            
            score = int(request.POST.get('score', 5))
            score = max(1, min(5, score))
            
            rating, created = Rating.objects.get_or_create(
                customer=customer,
                book=book,
                defaults={'score': score}
            )
            
            if not created:
                rating.score = score
                rating.save()
        
        except (Customer.DoesNotExist, Book.DoesNotExist):
            pass
    
    return redirect('core:book_detail', book_id=book_id)


def wishlist_view(request):
    """Display customer's wishlist"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        wishlist, created = Wishlist.objects.get_or_create(customer=customer)
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
        
        context = get_context(request)
        context.update({
            'wishlist': wishlist,
            'wishlist_items': wishlist_items,
        })
        
        return render(request, 'core/wishlist.html', context)
    
    except Customer.DoesNotExist:
        return redirect('core:login')


def add_to_wishlist(request, book_id):
    """Add a book to customer's wishlist"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        book = Book.objects.get(id=book_id)
        
        wishlist, created = Wishlist.objects.get_or_create(customer=customer)
        
        item, created = WishlistItem.objects.get_or_create(
            wishlist=wishlist,
            book=book
        )
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Đã thêm vào danh sách ước muốn'})
        
        return redirect('core:book_detail', book_id=book_id)
    
    except (Customer.DoesNotExist, Book.DoesNotExist):
        return redirect('core:login')


def remove_from_wishlist(request, wishlist_item_id):
    """Remove a book from customer's wishlist"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        wishlist_item = WishlistItem.objects.get(id=wishlist_item_id)
        customer = Customer.objects.get(id=request.session['customer_id'])
        
        if wishlist_item.wishlist.customer == customer:
            wishlist_item.delete()
    
    except (WishlistItem.DoesNotExist, Customer.DoesNotExist):
        pass
    
    return redirect('core:wishlist_view')


def account_view(request):
    """Display customer account information"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        orders = Order.objects.filter(customer=customer).order_by('-created_date' if hasattr(Order, 'created_date') else '-id')
        
        context = get_context(request)
        context.update({
            'customer': customer,
            'orders': orders,
        })
        
        return render(request, 'core/account.html', context)
    
    except Customer.DoesNotExist:
        return redirect('core:login')


def edit_account(request):
    """Edit customer account information"""
    if 'customer_id' not in request.session:
        return redirect('core:login')
    
    try:
        customer = Customer.objects.get(id=request.session['customer_id'])
        
        if request.method == 'POST':
            customer.name = request.POST.get('name', customer.name)
            customer.phone = request.POST.get('phone', customer.phone)
            customer.save()
            
            return redirect('core:account_view')
        
        context = get_context(request)
        context.update({
            'customer': customer,
        })
        
        return render(request, 'core/edit_account.html', context)
    
    except Customer.DoesNotExist:
        return redirect('core:login')
