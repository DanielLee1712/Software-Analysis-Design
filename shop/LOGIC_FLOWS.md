# 🔄 Logic Flow & Integration

## 1. Authentication Flow

### Registration
```
1. User fills form → POST /register/
2. Validate (name, email, password length)
3. Check if email exists → Error if duplicate
4. Hash password with make_password()
5. Create Customer object
6. Create empty Cart (is_active=True)
7. Redirect to login
```

### Login
```
1. User enters email + password → POST /login/
2. Query Customer by email
3. Verify password with check_password()
4. Store customer.id in request.session['customer_id']
5. Redirect to book_list
```

### Logout
```
1. Delete request.session['customer_id']
2. Redirect to book_list (as anonymous)
```

### Session Management
```
Every view checks: 'customer_id' in request.session
- If exists: Fetch customer, get cart, cart_count
- If missing: Redirect to login
- Pass to template: is_logged_in, customer, cart_count
```

---

## 2. Book Browsing Flow

### Book List
```
1. GET /books/ (or /books/?search=...&category=...&sort=...)
2. Query Book.objects.all()
3. Filter by category if provided
4. Filter by search query (title OR author name)
5. Sort (title, price_asc, price_desc, rating)
6. Get all categories for filter dropdown
7. Render with books, categories, selected_category
```

### Book Detail
```
1. GET /book/<id>/
2. Query Book by id or redirect
3. Query all Rating objects for this book
4. Calculate avg_rating
5. If logged in: Check if book in wishlist
6. Render with book, ratings, avg_rating, in_wishlist
```

---

## 3. Shopping Cart Flow

### Add to Cart
```
1. POST /cart/add/<book_id>/
2. Check: is_logged_in? → redirect to login
3. Get customer, book, active cart
4. Try get CartItem(cart, book)
   - If exists: quantity += posted_quantity
   - If new: create with quantity
5. Save & redirect to book_detail (or JSON if AJAX)
```

### View Cart
```
1. GET /cart/
2. Check: is_logged_in? → redirect to login
3. Get active cart for customer
4. Get all CartItem objects for this cart (with book FK)
5. Calculate total_price = sum(item.book.price * item.quantity)
6. Render with cart_items, total_price
```

### Update Cart Item
```
1. POST /cart/update/<cart_item_id>/
2. Verify owner (cartitem.cart.customer == session customer)
3. Get new quantity from POST
4. If quantity <= 0: delete CartItem
5. Else: update quantity, save
6. Redirect to /cart/
```

### Remove from Cart
```
1. GET/POST /cart/remove/<cart_item_id>/
2. Verify owner
3. Delete CartItem
4. Redirect to /cart/
```

---

## 4. Checkout & Order Flow

### Checkout View
```
1. GET /checkout/
2. Check: logged in? cart exists? has items?
3. Render form with:
   - cart_items (from cart)
   - total_price (calculated)
   - customer.address (pre-filled)
   - payment method options

1. POST /checkout/ (confirm)
2. Create Order:
   - customer = logged-in customer
   - address = customer.address
   - status = 'pending'
   - total_price = calculated
3. Create Payment:
   - order = created_order
   - amount = total_price
   - payment_method = from POST
   - status = 'pending'
4. Set cart.is_active = False (mark as used)
5. Redirect to order_confirmation/<order_id>/
```

### Order Confirmation
```
1. GET /order/confirmation/<order_id>/
2. Check: logged in? order belongs to customer?
3. Render success page with order details
4. Show order ID, total, status, address
```

---

## 5. Rating Flow

### Add Rating
```
1. POST /book/<book_id>/rate/
2. Check: logged in?
3. Get customer, book
4. Get or create Rating(customer, book)
5. Update score (1-5) from POST
6. Save
7. Redirect to /book/<id>/
```

### Display Ratings
```
On book_detail.html:
1. Query Rating.objects.filter(book=book)
2. Calculate avg_rating = sum(r.score) / len(ratings)
3. Display each rating with customer name & score
4. If logged in: show form to add rating
```

---

## 6. Wishlist Flow

### View Wishlist
```
1. GET /wishlist/
2. Check: logged in?
3. Get or create Wishlist(customer)
4. Get all WishlistItem objects
5. Render grid of books with add-to-cart button
```

### Add to Wishlist
```
1. POST /wishlist/add/<book_id>/
2. Check: logged in?
3. Get or create Wishlist(customer)
4. Get or create WishlistItem(wishlist, book)
5. Redirect to book_detail or return JSON
```

### Remove from Wishlist
```
1. POST /wishlist/remove/<wishlist_item_id>/
2. Verify owner (wishlist_item.wishlist.customer)
3. Delete WishlistItem
4. Redirect to /wishlist/
```

### Check if In Wishlist
```
On book_detail:
1. If logged in:
   wishlist = Wishlist.objects.get(customer=customer)
   in_wishlist = WishlistItem.objects.filter(
       wishlist=wishlist, book=book
   ).exists()
2. Pass to template to show/hide heart icon
```

---

## 7. Account Flow

### View Account
```
1. GET /account/
2. Check: logged in?
3. Get customer object
4. Get all Order objects for customer
5. Render with:
   - customer (name, email, phone, membership_level, loyalty_points)
   - orders (id, status, total_price, date)
```

### Edit Account
```
GET /account/edit/:
1. Render form with customer data

POST /account/edit/:
1. Update customer.name, phone from POST
2. Email is readonly
3. Save customer
4. Redirect to /account/
```

---

## 8. Context Helper Function

### `get_context(request)` - Used in all views
```python
def get_context(request):
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
```

This ensures every page shows:
- Login/logout buttons (based on is_logged_in)
- User name (if logged in)
- Cart count (if logged in)
- Navigation (wishlist, account, etc. only if logged in)

---

## 9. Security Measures

### Owner Verification
```python
# Cart operations
if cart.customer != logged_in_customer:
    return redirect('core:login')

# Wishlist operations
if wishlist.customer != logged_in_customer:
    return redirect('core:login')

# Order operations
if order.customer != logged_in_customer:
    return redirect('core:login')
```

### CSRF Protection
```html
<!-- All forms include -->
{% csrf_token %}
```

### Session-based Auth
```python
# No tokens, just session ID
request.session['customer_id'] = customer.id

# Check in every protected view
if 'customer_id' not in request.session:
    return redirect('core:login')
```

---

## 10. Data Validation

### Registration
- ✅ Name: Required, non-empty
- ✅ Email: Valid email format, unique
- ✅ Password: Min 6 characters, hashed
- ✅ Phone: Optional

### Add to Cart
- ✅ Book exists (or 404)
- ✅ User logged in
- ✅ Cart exists (auto-created on register)
- ✅ Quantity > 0

### Checkout
- ✅ User logged in
- ✅ Cart exists & has items
- ✅ Address exists
- ✅ Payment method selected

### Rating
- ✅ User logged in
- ✅ Book exists
- ✅ Score 1-5 (enforced with max/min)

---

## 11. URL Flow Diagram

```
Start (Anonymous)
    ↓
    ├─→ /register/ → POST → Create Customer → /login/
    ├─→ /login/ → POST → Set Session → /books/
    └─→ /books/ → View all books (anonymous OK)
         ↓
    Logged In
    ├─→ /book/<id>/ → View details, can rate/wishlist
    ├─→ /cart/add/<id>/ → CartItem created/updated
    ├─→ /cart/ → View items, can update/remove
    ├─→ /checkout/ → POST → Order + Payment created
    ├─→ /order/confirmation/<id>/ → Success page
    ├─→ /wishlist/ → View wishlist items
    ├─→ /wishlist/add/<id>/ → WishlistItem created
    ├─→ /account/ → View orders & profile
    ├─→ /account/edit/ → Update info
    └─→ /logout/ → Delete session → /books/
```

---

## 12. Template Inheritance

```
base.html (header, nav, footer)
    ├── login.html
    ├── register.html
    ├── books.html (grid with filter)
    ├── book_detail.html (with ratings form)
    ├── cart.html (with update quantity form)
    ├── checkout.html (with payment method selection)
    ├── order_confirmation.html
    ├── wishlist.html
    ├── account.html (with menu sidebar)
    └── edit_account.html

All inherit from base.html for:
- Header with logo & navigation
- Footer
- CSS styles (gradients, colors, responsive)
- Error/success message blocks
```

---

## 13. Database Queries Used

### Efficient Queries
```python
# With select_related (ForeignKey)
books = Book.objects.select_related('author', 'category', 'publisher')

# With prefetch_related (reverse FK, M2M)
cart_items = CartItem.objects.select_related('book').filter(cart=cart)

# Aggregation
Rating.objects.filter(book=book).aggregate(Avg('score'))

# Existence check
WishlistItem.objects.filter(wishlist=wishlist, book=book).exists()

# Counting
CartItem.objects.filter(cart__customer=customer, cart__is_active=True).count()
```

---

**All logic flows verified and tested! ✅**
