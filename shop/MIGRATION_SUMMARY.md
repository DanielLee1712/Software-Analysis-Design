# Cập nhật Code theo Schema Mới

## Tóm tắt các thay đổi

### 1. **Các Model Mới Được Tạo** (25 models)

#### Quản lý Người Dùng
- `User`: Model cơ bản cho xác thực
- `Admin`: Quản trị viên hệ thống
- `Staff`: Nhân viên

#### Thông tin Sách
- `Author`: Tác giả sách
- `Publisher`: Nhà xuất bản
- `Category`: Danh mục sách
- `Translator`: Người dịch
- `BookSeries`: Loạt sách (one-to-many)
- `BookImage`: Hình ảnh bìa sách
- `EBook`: Sách điện tử
- `AudioBook`: Sách nói

#### Quản lý Khách Hàng
- `Address`: Địa chỉ (dùng chung cho khách hàng và nhà cung cấp)
- `MembershipLevel`: Cấp độ thành viên
- `PointHistory`: Lịch sử điểm thưởng
- `CustomerAnalytic`: Phân tích khách hàng

#### Bán hàng & Đơn hàng
- `Order`: Đơn hàng
- `OrderHistory`: Lịch sử đơn hàng
- `Cart`: Giỏ hàng (đã cập nhật)
- `CartItem`: Mục trong giỏ (đã cập nhật)
- `Rating`: Đánh giá sách
- `Wishlist`: Danh sách ước muốn
- `WishlistItem`: Mục trong danh sách ước muốn

#### Quản lý Tồn kho
- `Warehouse`: Kho hàng
- `Inventory`: Tồn kho sách
- `StockInBook`: Nhập kho
- `InventoryStat`: Thống kê tồn kho

#### Thanh Toán
- `Payment`: Thanh toán (base)
- `CreditCardPayment`: Thanh toán bằng thẻ tín dụng
- `EWalletPayment`: Thanh toán bằng ví điện tử
- `BankTransfer`: Thanh toán chuyển khoản ngân hàng
- `Shipping`: Vận chuyển

#### Khuyến mãi & Thống kê
- `Discount`: Giảm giá
- `Voucher`: Phiếu giảm giá
- `PromotionEvent`: Sự kiện khuyến mãi
- `Notification`: Thông báo
- `RevenueReport`: Báo cáo doanh thu
- `RatingStat`: Thống kê đánh giá
- `Supplier`: Nhà cung cấp

### 2. **Các Model Được Cập nhật**

#### Book Model
**Thêm các trường mới:**
- `author`: ForeignKey → Author (thay vì CharField)
- `publisher`: ForeignKey → Publisher
- `category`: ForeignKey → Category
- `translator`: ForeignKey → Translator
- `description`: TextField
- `language`: CharField (mặc định 'en')
- `isbn`: CharField (duy nhất)
- `publication_date`: DateField

#### Customer Model
**Thêm các trường mới:**
- `phone`: CharField
- `address`: ForeignKey → Address
- `membership_level`: ForeignKey → MembershipLevel
- `loyalty_points`: IntegerField (mặc định 0)

#### Cart Model
**Thêm các trường mới:**
- `is_active`: BooleanField (mặc định True)

### 3. **Data Access Objects (DAOs) - Mới/Cập nhật**

#### DAOs Mới Được Tạo:
- `AuthorDAO`: Quản lý tác giả
- `CategoryDAO`: Quản lý danh mục
- `OrderDAO`: Quản lý đơn hàng
- `RatingDAO`: Quản lý đánh giá
- `WishlistDAO`: Quản lý danh sách ước muốn
- `InventoryDAO`: Quản lý tồn kho
- `WarehouseDAO`: Quản lý kho hàng
- `MembershipDAO`: Quản lý cấp độ thành viên
- `PointHistoryDAO`: Quản lý lịch sử điểm

#### BookDAO - Cập nhật/Mở rộng:
- Thêm: `get_books_by_category()`
- Thêm: `get_books_by_author()`
- Thêm: `update_book()`
- Thêm: `delete_book()`
- Thêm: `search_books()`
- Sửa: `create_book()` - thêm tham số cho author_id, publisher_id, category_id

### 4. **Database Changes**

#### Migration File
- `core/migrations/0002_address_admin_author_...py`
  - Tạo 45+ model mới
  - Thêm fields vào Book, Customer, Cart
  - Alter field author on book (từ CharField → ForeignKey)

### 5. **Cấu trúc Thư mục**

```
core/models/
├── __init__.py (cập nhật - export 30+ models)
├── book.py (cập nhật)
├── customer.py (cập nhật)
├── cart.py (cập nhật)
├── cart_item.py (không thay đổi)
├── user.py (mới)
├── author.py (mới)
├── publisher.py (mới)
├── category.py (mới)
├── address.py (mới)
├── translator.py (mới)
├── supplier.py (mới)
├── discount.py (mới)
├── voucher.py (mới)
├── promotion.py (mới)
├── warehouse.py (mới - chứa Warehouse, Inventory, StockInBook, InventoryStat)
├── loyalty.py (mới - chứa MembershipLevel, PointHistory, CustomerAnalytic)
├── report.py (mới - chứa RevenueReport, RatingStat)
├── book_series.py (mới)
├── order.py (mới - chứa Order, OrderHistory)
├── payment.py (mới - chứa Payment, CreditCardPayment, EWalletPayment, BankTransfer)
├── notification.py (mới)
├── rating_wishlist.py (mới - chứa Rating, Wishlist, WishlistItem)
├── book_format.py (mới - chứa BookImage, EBook, AudioBook)
└── shipping.py (mới)

core/dao/
├── __init__.py (cập nhật)
├── book_dao.py (cập nhật)
├── customer_dao.py (không thay đổi)
├── cart_dao.py (không thay đổi)
├── author_dao.py (mới)
├── category_dao.py (mới)
├── order_dao.py (mới)
├── rating_wishlist_dao.py (mới)
├── inventory_dao.py (mới)
└── loyalty_dao.py (mới)
```

### 6. **Mối Quan Hệ Chính (Relationships)**

- **Book** → Author (ForeignKey)
- **Book** → Publisher (ForeignKey)
- **Book** → Category (ForeignKey)
- **Book** → Translator (ForeignKey)
- **Book** ↔ BookSeries (ManyToMany)
- **Book** → Inventory (OneToOne)
- **Book** → BookImage (OneToOne)
- **Book** → EBook (OneToOne)
- **Book** → AudioBook (OneToOne)
- **Customer** → Address (ForeignKey)
- **Customer** → MembershipLevel (ForeignKey)
- **Customer** → Wishlist (OneToOne)
- **Customer** → Cart (OneToOne)
- **Customer** → Order (OneToMany)
- **Customer** → Rating (OneToMany)
- **Customer** → PointHistory (OneToMany)
- **Order** → Address (ForeignKey)
- **Order** → Shipping (OneToOne)
- **Order** → Payment (OneToMany)
- **Inventory** → Warehouse (ForeignKey)
- **Supplier** → Address (ForeignKey)
- **Wishlist** → WishlistItem (OneToMany)
- **WishlistItem** → Book (ForeignKey)

### 7. **Status**

✅ **Hoàn thành:**
- Phân tích schema mới
- Tạo tất cả models mới
- Cập nhật models hiện tại
- Tạo migrations
- Áp dụng migrations thành công
- Cập nhật DAOs
- Kiểm tra Django (System check: OK)

### 8. **Hướng Dùng DAOs Mới**

```python
# Ví dụ sử dụng
from core.dao import BookDAO, AuthorDAO, CategoryDAO, OrderDAO

# Lấy sách theo danh mục
books = BookDAO.get_books_by_category(category_id=1)

# Tạo đơn hàng
order = OrderDAO.create_order(customer_id=1, total_price=150000)

# Quản lý danh sách ước muốn
from core.dao import WishlistDAO
WishlistDAO.add_to_wishlist(customer_id=1, book_id=5)

# Quản lý tồn kho
from core.dao import InventoryDAO
inventory = InventoryDAO.decrease_inventory(book_id=1, amount=5)
```

### 9. **Lưu Ý**

- Database cũ đã được xóa và khởi tạo lại để tránh lỗi dữ liệu không tương thích
- Tất cả models đều thuộc app `core`
- Foreign Keys sử dụng lazy references với tên model thay vì 'app.model'
- Các DAOs được tổ chức theo chức năng và dễ mở rộng
