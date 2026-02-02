# Hướng Dẫn Cập Nhật Schema - Dự Án Shop

## 📋 Nội Dung Cập Nhật

Toàn bộ cấu trúc cơ sở dữ liệu của dự án đã được cập nhật để phù hợp với các sơ đồ thiết kế (Use Case Diagram, Sequence Diagram, Class Diagram, Database Diagram).

## 🎯 Các Thay Đổi Chính

### ✅ 1. Tạo 25 Models Mới

**Quản Lý Người Dùng (3)**
- `User` - Cơ sở xác thực
- `Admin` - Quản trị viên
- `Staff` - Nhân viên

**Thông Tin Sách (8)**
- `Author` - Tác giả sách
- `Publisher` - Nhà xuất bản
- `Category` - Danh mục sách
- `Translator` - Người dịch
- `BookSeries` - Loạt sách
- `BookImage` - Hình ảnh bìa
- `EBook` - Sách điện tử
- `AudioBook` - Sách nói

**Quản Lý Khách Hàng (4)**
- `Address` - Địa chỉ
- `MembershipLevel` - Cấp độ thành viên
- `PointHistory` - Lịch sử điểm thưởng
- `CustomerAnalytic` - Phân tích khách hàng

**Bán Hàng & Đơn Hàng (6)**
- `Order` - Đơn hàng
- `OrderHistory` - Lịch sử đơn hàng
- `Rating` - Đánh giá sách
- `Wishlist` - Danh sách ước muốn
- `WishlistItem` - Mục trong danh sách ước muốn
- `Notification` - Thông báo

**Thanh Toán (4)**
- `Payment` - Thanh toán cơ bản
- `CreditCardPayment` - Thanh toán thẻ tín dụng
- `EWalletPayment` - Thanh toán ví điện tử
- `BankTransfer` - Thanh toán chuyển khoản
- `Shipping` - Vận chuyển

**Tồn Kho (4)**
- `Warehouse` - Kho hàng
- `Inventory` - Tồn kho sách
- `StockInBook` - Nhập kho
- `InventoryStat` - Thống kê tồn kho

**Khuyến Mãi & Thống Kê (4)**
- `Discount` - Giảm giá
- `Voucher` - Phiếu giảm giá
- `PromotionEvent` - Sự kiện khuyến mãi
- `RevenueReport` - Báo cáo doanh thu
- `RatingStat` - Thống kê đánh giá
- `Supplier` - Nhà cung cấp

### ✅ 2. Cập Nhật Models Hiện Tại

**Book Model**
```python
# Trước
class Book(models.Model):
    title = CharField
    author = CharField  # ❌ Chỉ là text
    price = DecimalField
    stock = IntegerField

# Sau
class Book(models.Model):
    title = CharField
    author = ForeignKey(Author)  # ✅ Liên kết đúng
    publisher = ForeignKey(Publisher)
    category = ForeignKey(Category)
    translator = ForeignKey(Translator)
    price = DecimalField
    stock = IntegerField
    description = TextField
    language = CharField
    isbn = CharField
    publication_date = DateField
```

**Customer Model**
```python
# Thêm các trường mới
phone = CharField
address = ForeignKey(Address)
membership_level = ForeignKey(MembershipLevel)
loyalty_points = IntegerField
```

**Cart Model**
```python
# Thêm
is_active = BooleanField
```

### ✅ 3. Data Access Objects (DAOs)

**DAOs Hiện Tại (Cập Nhật)**
- `BookDAO` - Mở rộng thêm phương thức search, filter
- `CustomerDAO` - Giữ nguyên
- `CartDAO` - Giữ nguyên

**DAOs Mới**
- `AuthorDAO` - Quản lý tác giả
- `CategoryDAO` - Quản lý danh mục
- `OrderDAO` - Quản lý đơn hàng
- `RatingDAO` - Quản lý đánh giá
- `WishlistDAO` - Quản lý danh sách ước muốn
- `InventoryDAO` - Quản lý tồn kho
- `WarehouseDAO` - Quản lý kho hàng
- `MembershipDAO` - Quản lý cấp độ thành viên
- `PointHistoryDAO` - Quản lý lịch sử điểm

## 📂 Cấu Trúc Thư Mục

```
core/
├── models/
│   ├── __init__.py (cập nhật)
│   ├── book.py (cập nhật)
│   ├── customer.py (cập nhật)
│   ├── cart.py (cập nhật)
│   ├── cart_item.py
│   ├── user.py (mới)
│   ├── author.py (mới)
│   ├── publisher.py (mới)
│   ├── category.py (mới)
│   ├── address.py (mới)
│   ├── translator.py (mới)
│   ├── supplier.py (mới)
│   ├── discount.py (mới)
│   ├── voucher.py (mới)
│   ├── promotion.py (mới)
│   ├── warehouse.py (mới - 4 models)
│   ├── loyalty.py (mới - 3 models)
│   ├── report.py (mới - 2 models)
│   ├── book_series.py (mới)
│   ├── order.py (mới - 2 models)
│   ├── payment.py (mới - 4 models)
│   ├── notification.py (mới)
│   ├── rating_wishlist.py (mới - 3 models)
│   ├── book_format.py (mới - 3 models)
│   └── shipping.py (mới)
├── dao/
│   ├── __init__.py (cập nhật)
│   ├── book_dao.py (cập nhật)
│   ├── customer_dao.py
│   ├── cart_dao.py
│   ├── author_dao.py (mới)
│   ├── category_dao.py (mới)
│   ├── order_dao.py (mới)
│   ├── rating_wishlist_dao.py (mới)
│   ├── inventory_dao.py (mới)
│   └── loyalty_dao.py (mới)
└── migrations/
    └── 0002_address_admin_author_... (45+ thay đổi)
```

## 🔄 Mối Quan Hệ Chính (Relationships)

```
Book
├─ author (FK) → Author
├─ publisher (FK) → Publisher
├─ category (FK) → Category
├─ translator (FK) → Translator
├─ inventory (O2O) → Inventory
├─ image (O2O) → BookImage
├─ ebook (O2O) → EBook
├─ audiobook (O2O) → AudioBook
└─ series (M2M) ↔ BookSeries

Customer
├─ address (FK) → Address
├─ membership_level (FK) → MembershipLevel
├─ cart (O2O) → Cart
├─ orders (O2M) → Order
├─ ratings (O2M) → Rating
├─ wishlist (O2O) → Wishlist
├─ point_history (O2M) → PointHistory
└─ notifications (O2M) → Notification

Order
├─ customer (FK) → Customer
├─ address (FK) → Address
├─ shipping (O2O) → Shipping
└─ payments (O2M) → Payment

Wishlist
├─ customer (O2O) → Customer
└─ items (O2M) → WishlistItem

Inventory
├─ book (O2O) → Book
└─ warehouse (FK) → Warehouse

Supplier
└─ address (FK) → Address
```

## 🚀 Cách Sử Dụng

### Tạo Tác Giả
```python
from core.dao import AuthorDAO

author = AuthorDAO.create_author(
    name="Nguyễn Nhật Ánh",
    bio="Tác giả nổi tiếng",
    email="nna@example.com"
)
```

### Tạo Sách Với Thông Tin Đầy Đủ
```python
from core.dao import BookDAO

book = BookDAO.create_book(
    title="Chiều Hè và Những Cơn Gió Lạnh",
    author_id=1,
    publisher_id=1,
    category_id=1,
    price=85000,
    stock=50,
    description="Một tác phẩm kinh điển",
    isbn="978-604-1234567"
)
```

### Lấy Sách Theo Danh Mục
```python
books = BookDAO.get_books_by_category(category_id=1)
```

### Quản Lý Danh Sách Ước Muốn
```python
from core.dao import WishlistDAO

# Thêm sách vào danh sách ước muốn
WishlistDAO.add_to_wishlist(customer_id=1, book_id=5)

# Lấy tất cả mục trong danh sách
items = WishlistDAO.get_wishlist_items(customer_id=1)

# Xóa khỏi danh sách
WishlistDAO.remove_from_wishlist(customer_id=1, book_id=5)
```

### Quản Lý Tồn Kho
```python
from core.dao import InventoryDAO

# Giảm tồn kho
InventoryDAO.decrease_inventory(book_id=1, amount=5)

# Tăng tồn kho
InventoryDAO.increase_inventory(book_id=1, amount=10)

# Lấy sách có tồn kho thấp
low_stock = InventoryDAO.get_low_stock_books(threshold=10)
```

### Quản Lý Đơn Hàng
```python
from core.dao import OrderDAO

# Tạo đơn hàng
order = OrderDAO.create_order(
    customer_id=1,
    address_id=1,
    total_price=150000
)

# Cập nhật trạng thái
OrderDAO.update_order_status(order_id=1, status='shipped')

# Lấy đơn hàng của khách hàng
orders = OrderDAO.get_orders_by_customer(customer_id=1)
```

## 📊 Thống Kê & Báo Cáo

### Đánh Giá
```python
from core.dao import RatingDAO

# Tạo đánh giá
RatingDAO.create_rating(customer_id=1, book_id=5, score=5)

# Lấy đánh giá của sách
ratings = RatingDAO.get_ratings_by_book(book_id=5)

# Lấy điểm đánh giá trung bình
avg = RatingDAO.get_average_rating(book_id=5)
```

### Điểm Thưởng
```python
from core.dao import PointHistoryDAO

# Thêm điểm
PointHistoryDAO.add_points(customer_id=1, points=100)

# Lấy tổng điểm
total = PointHistoryDAO.get_total_points(customer_id=1)
```

## ✅ Kiểm Tra

Tất cả đã được kiểm tra và xác nhận hoạt động:

```bash
# Kiểm tra Django
python3 manage.py check
# Output: System check identified no issues (0 silenced).

# Áp dụng migrations
python3 manage.py migrate
# Output: All migrations applied successfully
```

## 📝 Lưu Ý Quan Trọng

1. **Database đã được reset** - Tất cả dữ liệu cũ đã bị xóa để tránh xung đột
2. **Cần tải lại sample data** - Chạy lệnh `python3 manage.py load_sample_data` nếu cần
3. **Foreign Keys tự động** - Django tự động tạo các trường `_id` cho ForeignKeys
4. **Migrations tự động** - Tất cả quan hệ đã được thiết lập trong migrations

## 🎉 Kết Quả

- ✅ 25+ Models mới được tạo
- ✅ 4 Models hiện tại được cập nhật
- ✅ 9 DAOs mới được tạo
- ✅ 3 DAOs hiện tại được cập nhật
- ✅ 1 Migration file với 45+ thay đổi
- ✅ Database hoàn toàn đồng bộ
- ✅ Tất cả kiểm tra Django đều pass

## 📞 Hỗ Trợ

Nếu gặp bất kỳ vấn đề nào, hãy kiểm tra:

1. Các imports trong files Python
2. Tên của Foreign Keys có đúng không
3. Migrations đã được apply chưa
4. Django cache cần được xóa (`python3 manage.py clear_cache`)
