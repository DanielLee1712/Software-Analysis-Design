from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from core.models import (
    Author, Publisher, Category, Book, Customer, Address,
    MembershipLevel, Order, Payment, Rating, Wishlist, WishlistItem,
    Warehouse, Inventory, Notification, Discount, Voucher
)
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Load comprehensive sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🔄 Bắt đầu tải dữ liệu mẫu...'))
        
        # Create sample data
        self.create_addresses()
        self.create_membership_levels()
        self.create_authors()
        self.create_publishers()
        self.create_categories()
        self.create_books()
        self.create_warehouse()
        self.create_inventory()
        self.create_customers()
        self.create_orders()
        self.create_ratings()
        self.create_wishlists()
        self.create_discounts()
        self.create_vouchers()
        
        self.stdout.write(self.style.SUCCESS('✅ Đã tải xong tất cả dữ liệu mẫu!'))

    def create_addresses(self):
        """Create sample addresses"""
        addresses = [
            {'street': '123 Nguyễn Huệ', 'city': 'Hồ Chí Minh', 'province': 'Hồ Chí Minh'},
            {'street': '456 Hà Nội', 'city': 'Hà Nội', 'province': 'Hà Nội'},
            {'street': '789 Đà Nẵng', 'city': 'Đà Nẵng', 'province': 'Đà Nẵng'},
            {'street': '321 Cần Thơ', 'city': 'Cần Thơ', 'province': 'Cần Thơ'},
        ]
        
        for addr in addresses:
            Address.objects.get_or_create(**addr)
        
        self.stdout.write(self.style.SUCCESS('✓ Địa chỉ được tạo'))

    def create_membership_levels(self):
        """Create membership levels"""
        levels = [
            {'name': 'Bronze', 'discount_rate': 5.0, 'required_points': 0},
            {'name': 'Silver', 'discount_rate': 10.0, 'required_points': 1000},
            {'name': 'Gold', 'discount_rate': 15.0, 'required_points': 5000},
            {'name': 'Platinum', 'discount_rate': 20.0, 'required_points': 10000},
        ]
        
        for level in levels:
            MembershipLevel.objects.get_or_create(**level)
        
        self.stdout.write(self.style.SUCCESS('✓ Cấp độ thành viên được tạo'))

    def create_authors(self):
        """Create sample authors"""
        authors = [
            {'name': 'Nguyễn Nhật Ánh', 'bio': 'Tác giả nổi tiếng Việt Nam', 'email': 'nna@example.com'},
            {'name': 'Tô Hoài', 'bio': 'Tác giả kinh điển', 'email': 'tohoai@example.com'},
            {'name': 'Mạc Can', 'bio': 'Nhà văn hiện đại', 'email': 'maccan@example.com'},
            {'name': 'Dạ Vệ', 'bio': 'Tác giả khoa học viễn tưởng', 'email': 'dawe@example.com'},
            {'name': 'Thạch Lam', 'bio': 'Nhà văn tâm lý', 'email': 'thachlam@example.com'},
            {'name': 'Vũ Trụ', 'bio': 'Tác giả trữ tình', 'email': 'vutru@example.com'},
            {'name': 'Quỳnh Dao', 'bio': 'Tác giả lãng mạn', 'email': 'quinhdao@example.com'},
            {'name': 'Kim Dung', 'bio': 'Tác giả kiếm hiệp', 'email': 'kimdung@example.com'},
        ]
        
        for author in authors:
            Author.objects.get_or_create(**author)
        
        self.stdout.write(self.style.SUCCESS('✓ Tác giả được tạo'))

    def create_publishers(self):
        """Create sample publishers"""
        publishers = [
            {'name': 'NXB Kim Đồng', 'email': 'kimdong@example.com', 'phone': '0283456789'},
            {'name': 'NXB Trẻ', 'email': 'tre@example.com', 'phone': '0283456790'},
            {'name': 'NXB Văn Học', 'email': 'vanhoc@example.com', 'phone': '0283456791'},
            {'name': 'NXB Thế Giới', 'email': 'thegioi@example.com', 'phone': '0283456792'},
            {'name': 'NXB Công Thương', 'email': 'congthuong@example.com', 'phone': '0283456793'},
        ]
        
        for pub in publishers:
            Publisher.objects.get_or_create(**pub)
        
        self.stdout.write(self.style.SUCCESS('✓ Nhà xuất bản được tạo'))

    def create_categories(self):
        """Create book categories"""
        categories = [
            {'name': 'Tiểu thuyết', 'description': 'Sách tiểu thuyết'},
            {'name': 'Lịch sử', 'description': 'Sách lịch sử'},
            {'name': 'Khoa học', 'description': 'Sách khoa học'},
            {'name': 'Kinh tế', 'description': 'Sách kinh tế'},
            {'name': 'Tâm lý', 'description': 'Sách tâm lý'},
            {'name': 'Kỹ năng sống', 'description': 'Sách kỹ năng sống'},
            {'name': 'Truyện tranh', 'description': 'Truyện tranh'},
            {'name': 'Thơ', 'description': 'Sách thơ'},
        ]
        
        for cat in categories:
            Category.objects.get_or_create(**cat)
        
        self.stdout.write(self.style.SUCCESS('✓ Danh mục sách được tạo'))

    def create_books(self):
        """Create sample books"""
        books = [
            # Tiểu thuyết
            {'title': 'Chiều hè và những cơn gió lạnh', 'author': 'Nguyễn Nhật Ánh', 'price': 85000, 'stock': 30, 'category': 'Tiểu thuyết', 'description': 'Một tác phẩm kinh điển', 'isbn': '978-604-1001001'},
            {'title': 'Những đứa trẻ lạc lối', 'author': 'Tô Hoài', 'price': 75000, 'stock': 25, 'category': 'Tiểu thuyết', 'description': 'Truyện kinh điển', 'isbn': '978-604-1001002'},
            {'title': 'Thế giới mầu xanh lam', 'author': 'Mạc Can', 'price': 95000, 'stock': 20, 'category': 'Tiểu thuyết', 'description': 'Tiểu thuyết đương đại', 'isbn': '978-604-1001003'},
            {'title': 'Quỷ nhân', 'author': 'Dạ Vệ', 'price': 88000, 'stock': 22, 'category': 'Tiểu thuyết', 'description': 'Viễn tưởng kỳ ảo', 'isbn': '978-604-1001004'},
            {'title': 'Số phận con người', 'author': 'Thạch Lam', 'price': 92000, 'stock': 18, 'category': 'Tiểu thuyết', 'description': 'Tiểu thuyết tâm lý', 'isbn': '978-604-1001005'},
            
            # Lịch sử
            {'title': 'Lịch sử Việt Nam thời cổ đại', 'author': 'Vũ Trụ', 'price': 120000, 'stock': 15, 'category': 'Lịch sử', 'description': 'Tài liệu lịch sử', 'isbn': '978-604-1001006'},
            {'title': 'Chiến tranh tranh đấu của dân tộc', 'author': 'Quỳnh Dao', 'price': 130000, 'stock': 12, 'category': 'Lịch sử', 'description': 'Lịch sử kháng chiến', 'isbn': '978-604-1001007'},
            
            # Khoa học
            {'title': 'Vũ trụ vô hạn', 'author': 'Kim Dung', 'price': 105000, 'stock': 20, 'category': 'Khoa học', 'description': 'Khoa học vũ trụ', 'isbn': '978-604-1001008'},
            {'title': 'Tiến hóa của loài người', 'author': 'Nguyễn Nhật Ánh', 'price': 98000, 'stock': 16, 'category': 'Khoa học', 'description': 'Khoa học sinh học', 'isbn': '978-604-1001009'},
            
            # Kinh tế
            {'title': 'Kinh tế vĩ mô Việt Nam', 'author': 'Tô Hoài', 'price': 115000, 'stock': 14, 'category': 'Kinh tế', 'description': 'Phân tích kinh tế', 'isbn': '978-604-1001010'},
            {'title': 'Khởi nghiệp thành công', 'author': 'Mạc Can', 'price': 85000, 'stock': 28, 'category': 'Kinh tế', 'description': 'Hướng dẫn khởi nghiệp', 'isbn': '978-604-1001011'},
            
            # Tâm lý
            {'title': 'Tâm lý học ứng dụng', 'author': 'Dạ Vệ', 'price': 95000, 'stock': 19, 'category': 'Tâm lý', 'description': 'Tâm lý học thực hành', 'isbn': '978-604-1001012'},
            {'title': 'Cảm xúc và con người', 'author': 'Thạch Lam', 'price': 88000, 'stock': 23, 'category': 'Tâm lý', 'description': 'Nghiên cứu cảm xúc', 'isbn': '978-604-1001013'},
            
            # Kỹ năng sống
            {'title': 'Kỹ năng giao tiếp hiệu quả', 'author': 'Vũ Trụ', 'price': 75000, 'stock': 32, 'category': 'Kỹ năng sống', 'description': 'Hướng dẫn giao tiếp', 'isbn': '978-604-1001014'},
            {'title': 'Quản lý thời gian thông minh', 'author': 'Quỳnh Dao', 'price': 68000, 'stock': 35, 'category': 'Kỹ năng sống', 'description': 'Kỹ năng quản lý', 'isbn': '978-604-1001015'},
            
            # Truyện tranh
            {'title': 'One Piece - Tập 1', 'author': 'Kim Dung', 'price': 45000, 'stock': 50, 'category': 'Truyện tranh', 'description': 'Truyện tranh phiêu lưu', 'isbn': '978-604-1001016'},
            {'title': 'Naruto - Tập 1', 'author': 'Nguyễn Nhật Ánh', 'price': 45000, 'stock': 48, 'category': 'Truyện tranh', 'description': 'Truyện tranh ninja', 'isbn': '978-604-1001017'},
            
            # Thơ
            {'title': 'Những bài thơ yêu thương', 'author': 'Tô Hoài', 'price': 65000, 'stock': 27, 'category': 'Thơ', 'description': 'Tuyển tập thơ lãng mạn', 'isbn': '978-604-1001018'},
            {'title': 'Thơ hay của lịch sử', 'author': 'Mạc Can', 'price': 72000, 'stock': 24, 'category': 'Thơ', 'description': 'Thơ kinh điển', 'isbn': '978-604-1001019'},
        ]
        
        for book_data in books:
            title = book_data.pop('title')
            author_name = book_data.pop('author')
            category_name = book_data.pop('category')
            
            author = Author.objects.get(name=author_name)
            category = Category.objects.get(name=category_name)
            publisher = Publisher.objects.first()
            
            Book.objects.get_or_create(
                title=title,
                defaults={
                    'author': author,
                    'category': category,
                    'publisher': publisher,
                    **book_data
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Sách được tạo'))

    def create_warehouse(self):
        """Create warehouse"""
        Warehouse.objects.get_or_create(
            name='Kho hàng chính',
            defaults={'location': 'Hồ Chí Minh', 'capacity': 10000}
        )
        self.stdout.write(self.style.SUCCESS('✓ Kho hàng được tạo'))

    def create_inventory(self):
        """Create inventory for books"""
        warehouse = Warehouse.objects.first()
        
        for book in Book.objects.all():
            Inventory.objects.get_or_create(
                book=book,
                defaults={
                    'quantity_available': book.stock,
                    'warehouse': warehouse
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Tồn kho được tạo'))

    def create_customers(self):
        """Create sample customers"""
        address = Address.objects.first()
        membership = MembershipLevel.objects.first()
        
        customers = [
            {'name': 'Trần Thị A', 'email': 'tranthia@example.com', 'password': 'pass123', 'phone': '0901234567'},
            {'name': 'Lê Văn B', 'email': 'levanb@example.com', 'password': 'pass123', 'phone': '0901234568'},
            {'name': 'Phạm Thị C', 'email': 'phamthic@example.com', 'password': 'pass123', 'phone': '0901234569'},
            {'name': 'Đỗ Văn D', 'email': 'dovand@example.com', 'password': 'pass123', 'phone': '0901234570'},
            {'name': 'Ngô Thị E', 'email': 'ngothie@example.com', 'password': 'pass123', 'phone': '0901234571'},
        ]
        
        for cust in customers:
            password = cust.pop('password')
            Customer.objects.get_or_create(
                email=cust['email'],
                defaults={
                    'password': make_password(password),
                    'address': address,
                    'membership_level': membership,
                    'loyalty_points': 500,
                    **cust
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Khách hàng được tạo'))

    def create_orders(self):
        """Create sample orders"""
        customers = Customer.objects.all()[:3]
        address = Address.objects.first()
        
        for i, customer in enumerate(customers):
            Order.objects.get_or_create(
                customer=customer,
                defaults={
                    'address': address,
                    'status': 'confirmed' if i % 2 == 0 else 'pending',
                    'total_price': 150000 + (i * 50000)
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Đơn hàng được tạo'))

    def create_ratings(self):
        """Create sample ratings"""
        books = Book.objects.all()[:10]
        customers = Customer.objects.all()[:3]
        
        rating_count = 0
        for book in books:
            for customer in customers:
                score = (rating_count % 5) + 1
                Rating.objects.get_or_create(
                    customer=customer,
                    book=book,
                    defaults={'score': score}
                )
                rating_count += 1
        
        self.stdout.write(self.style.SUCCESS('✓ Đánh giá được tạo'))

    def create_wishlists(self):
        """Create wishlists"""
        books = Book.objects.all()
        customers = Customer.objects.all()
        
        for customer in customers:
            wishlist, created = Wishlist.objects.get_or_create(customer=customer)
            
            # Add 5 random books to wishlist
            for book in books[:5]:
                WishlistItem.objects.get_or_create(wishlist=wishlist, book=book)
        
        self.stdout.write(self.style.SUCCESS('✓ Danh sách ước muốn được tạo'))

    def create_discounts(self):
        """Create sample discounts"""
        now = datetime.now()
        
        discounts = [
            {
                'name': 'Giảm giá cuối năm',
                'discount_rate': 15.0,
                'method_name': 'ENDYEAR2025',
                'description': 'Giảm giá 15% cho tất cả sách',
                'start_date': now,
                'end_date': now + timedelta(days=30)
            },
            {
                'name': 'Giảm giá sách mới',
                'discount_rate': 10.0,
                'method_name': 'NEWBOOK',
                'description': 'Giảm giá 10% cho sách mới',
                'start_date': now,
                'end_date': now + timedelta(days=60)
            },
        ]
        
        for discount in discounts:
            Discount.objects.get_or_create(**discount)
        
        self.stdout.write(self.style.SUCCESS('✓ Giảm giá được tạo'))

    def create_vouchers(self):
        """Create sample vouchers"""
        vouchers = [
            {
                'voucher_code': 'WELCOME50K',
                'max_usage': 100,
                'current_usage': 10,
                'discount_value': 50000
            },
            {
                'voucher_code': 'SUMMER30PERCENT',
                'max_usage': 50,
                'current_usage': 5,
                'discount_value': 100000
            },
            {
                'voucher_code': 'FREESHIP100K',
                'max_usage': 200,
                'current_usage': 20,
                'discount_value': 30000
            },
        ]
        
        for voucher in vouchers:
            Voucher.objects.get_or_create(**voucher)
        
        self.stdout.write(self.style.SUCCESS('✓ Voucher được tạo'))
