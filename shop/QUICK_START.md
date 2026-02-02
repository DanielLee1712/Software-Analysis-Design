# 🚀 Quick Start Guide - BookShop

## **Bước 1: Khởi Động Server**
```bash
cd "/Users/RichardLee/Desktop/Năm 4/Software-Analysis-Design/shop"
python3 manage.py runserver
```
✅ Truy cập: http://localhost:8000

---

## **Bước 2: Tài Khoản Mẫu**

### Khách hàng mẫu (đã có sẵn):
| Email | Password | Tên |
|-------|----------|-----|
| tranthia@example.com | pass123 | Trần Thị A |
| levanb@example.com | pass123 | Lê Văn B |
| phamthic@example.com | pass123 | Phạm Thị C |
| dovand@example.com | pass123 | Đỗ Văn D |
| ngothie@example.com | pass123 | Ngô Thị E |

### Admin (tạo bằng):
```bash
python3 manage.py createsuperuser
```
Truy cập: http://localhost:8000/admin/

---

## **Bước 3: Tính Năng Chính**

### 📚 **Xem Sách**
- URL: http://localhost:8000/ hoặc /books/
- **Bộ lọc**: Danh mục, tìm kiếm, sắp xếp
- **Grid layout**: Hiển thị 20+ quyển sách mẫu
- **Click sách**: Xem chi tiết, đánh giá, thêm vào danh sách

### 🛒 **Giỏ Hàng**
- **Thêm vào**: Click nút "🛒 Thêm" trên sách
- **Xem giỏ**: Menu → "🛒 Giỏ" (hiển thị số lượng)
- **Cập nhật**: Thay đổi số lượng → Tự cập nhật
- **Xóa**: Click nút 🗑️
- **Thanh toán**: Click "💳 Thanh toán"

### 💳 **Thanh Toán**
- **Phương thức**: Thẻ tín dụng, chuyển khoản, ví điện tử
- **Xác nhận**: Order được tạo, xem trong tài khoản
- **Tracking**: /account/ → xem lịch sử đơn hàng

### ❤️ **Danh Sách Ước Muốn**
- **Thêm**: Vào sách chi tiết → Click "❤️"
- **Xem**: Menu → "❤️ Danh sách ước muốn"
- **Mua**: Click "🛒" để thêm vào giỏ từ danh sách

### ⭐ **Đánh Giá**
- **Đánh giá**: Sách chi tiết → Chọn sao (1-5) → Gửi
- **Xem**: Tất cả đánh giá hiển thị dưới

### 👤 **Tài Khoản**
- **Xem info**: Email, điện thoại, cấp độ, điểm tích lũy
- **Chỉnh sửa**: Tên, điện thoại (email không đổi được)
- **Đơn hàng**: Xem tất cả đơn hàng + trạng thái

### 🔐 **Xác Thực**
- **Đăng ký**: /register/ → Tạo tài khoản mới
- **Đăng nhập**: /login/ → Email + Password
- **Đăng xuất**: Menu → Đăng xuất

---

## **Bước 4: Menu Navigation**

```
Header (Sticky):
├── 📚 BookShop (logo) → Home
├── Sách → /books/
├── (Nếu logged in)
│   ├── ❤️ Danh sách ước muốn
│   ├── 🛒 Giỏ (N) [số lượng]
│   ├── 👤 Tài khoản
│   └── Đăng xuất
└── (Nếu chưa login)
    ├── Đăng nhập
    └── Đăng ký
```

---

## **Bước 5: URL Map**

| Tính năng | URL |
|----------|-----|
| Danh sách sách | `/` hoặc `/books/` |
| Chi tiết sách | `/book/<id>/` |
| Đăng ký | `/register/` |
| Đăng nhập | `/login/` |
| Giỏ hàng | `/cart/` |
| Thanh toán | `/checkout/` |
| Danh sách ước muốn | `/wishlist/` |
| Tài khoản | `/account/` |
| Chỉnh sửa TK | `/account/edit/` |
| Admin panel | `/admin/` |

---

## **Bước 6: Dữ Liệu Mẫu**

### 📖 Sách (20 quyển)
- **Tiểu thuyết**: 5 cuốn (Nguyễn Nhật Ánh, Tô Hoài, Mạc Can, Dạ Vệ, Thạch Lam)
- **Lịch sử**: 2 cuốn (Vũ Trụ, Quỳnh Dao)
- **Khoa học**: 2 cuốn (Kim Dung, Nguyễn Nhật Ánh)
- **Kinh tế**: 2 cuốn (Tô Hoài, Mạc Can)
- **Tâm lý**: 2 cuốn (Dạ Vệ, Thạch Lam)
- **Kỹ năng**: 2 cuốn (Vũ Trụ, Quỳnh Dao)
- **Truyện tranh**: 2 cuốn (Kim Dung, Nguyễn Nhật Ánh)
- **Thơ**: 2 cuốn (Tô Hoài, Mạc Can)

### 📚 Tác giả (8 người)
Nguyễn Nhật Ánh, Tô Hoài, Mạc Can, Dạ Vệ, Thạch Lam, Vũ Trụ, Quỳnh Dao, Kim Dung

### 🏢 Nhà xuất bản (5 nhà)
NXB Kim Đồng, NXB Trẻ, NXB Văn Học, NXB Thế Giới, NXB Công Thương

### 👥 Khách hàng (5 người)
5 tài khoản mẫu ở trên (với mật khẩu: pass123)

---

## **Bước 7: Testing Checklist**

### ✅ Xác Thực
- [ ] Đăng ký tài khoản mới
- [ ] Đăng nhập với tài khoản mẫu
- [ ] Chuyên đổi tài khoản (logout → login khác)
- [ ] Thử URL không được phép (redirect to login)

### ✅ Sách & Browse
- [ ] Xem danh sách sách
- [ ] Lọc theo danh mục
- [ ] Tìm kiếm theo tên sách
- [ ] Tìm kiếm theo tác giả
- [ ] Sắp xếp (A-Z, giá, rating)
- [ ] Xem chi tiết sách

### ✅ Rating
- [ ] Đánh giá sách (1-5 sao)
- [ ] Xem đánh giá từ người khác
- [ ] Cập nhật đánh giá (override cũ)

### ✅ Wishlist
- [ ] Thêm sách vào danh sách
- [ ] Xem danh sách ước muốn
- [ ] Xóa khỏi danh sách
- [ ] Thêm vào giỏ từ danh sách

### ✅ Giỏ Hàng
- [ ] Thêm 1 sách → Giỏ: 1
- [ ] Thêm cùng sách lần 2 → Quantity: 2
- [ ] Thêm sách khác → Giỏ: 2 items
- [ ] Cập nhật quantity
- [ ] Xóa item
- [ ] Tính tổng tiền đúng

### ✅ Checkout
- [ ] Xem tóm tắt đơn hàng
- [ ] Chọn phương thức thanh toán
- [ ] Xác nhận → Order tạo thành công
- [ ] Redirect to confirmation page
- [ ] Giỏ trở thành inactive

### ✅ Tài Khoản
- [ ] Xem thông tin cá nhân
- [ ] Xem lịch sử đơn hàng
- [ ] Chỉnh sửa tên
- [ ] Chỉnh sửa điện thoại
- [ ] Email readonly (không chỉnh sửa được)

### ✅ Bảo Mật
- [ ] Session logout sau đăng xuất
- [ ] Không access cart người khác
- [ ] Không edit order người khác
- [ ] CSRF token trên forms
- [ ] Password hashed (không plaintext)

---

## **Bước 8: Troubleshooting**

### **Server không chạy**
```bash
# Kiểm tra port
lsof -i :8000

# Kill nếu đang chiếm
kill -9 <PID>

# Restart
python3 manage.py runserver
```

### **Static files không load**
```bash
python3 manage.py collectstatic
```

### **Database lỗi**
```bash
# Xóa & tạo lại
rm db.sqlite3
python3 manage.py migrate
python3 manage.py load_sample_data
```

### **Import lỗi**
```bash
# Kiểm tra migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Check
python3 manage.py check
```

---

## **Bước 9: Files Quan Trọng**

```
shop/
├── core/
│   ├── views.py (13 views functions)
│   ├── urls.py (25+ URL patterns)
│   ├── models/ (28 models)
│   ├── dao/ (12 DAOs)
│   ├── management/commands/load_sample_data.py
│   └── templates/core/ (10 templates)
├── db.sqlite3 (database)
├── manage.py
├── IMPLEMENTATION_COMPLETE.md (tài liệu)
├── LOGIC_FLOWS.md (chi tiết logic)
└── README_ARCHITECTURE.md (sơ đồ)
```

---

## **Bước 10: Tăng Cấp Độ (Optional)**

```bash
# Create superuser for admin
python3 manage.py createsuperuser

# Access admin
http://localhost:8000/admin/

# Browse models, add/edit data directly
```

---

## 🎯 **Success Indicators**

✅ Server chạy tại `http://localhost:8000`
✅ Database có 20 sách + 5 khách hàng
✅ Có thể đăng nhập/đăng ký
✅ Giỏ hàng hoạt động
✅ Thanh toán tạo Order
✅ Danh sách ước muốn lưu được
✅ Rating thêm được
✅ Tài khoản xem được lịch sử

---

**Ready to go! 🚀**
