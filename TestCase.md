# Danh sách Test Case - Bài thực hành 03

## Bài 1: Tính chu vi hình chữ nhật

- **Đầu vào:** Chiều dài `a`, chiều rộng `b` (kiểu số thực).
- **Đầu ra mong đợi:** Giá trị chu vi `P = (a + b) * 2`. Báo lỗi nếu dữ liệu sai.
- **Kỹ thuật áp dụng:** Phân lớp tương đương & Phân tích giá trị biên.

| Mã TC | Loại dữ liệu | Đầu vào (a, b) | Đầu ra mong đợi          | Kỹ thuật kiểm thử                   |
| ----- | ------------ | -------------- | ------------------------ | ----------------------------------- |
| TC1.1 | Hợp lệ       | a=5, b=3       | 16.0                     | Phân lớp tương đương (Trong khoảng) |
| TC1.2 | Biên hợp lệ  | a=0.1, b=0.1   | 0.4                      | Giá trị biên (Nhỏ nhất có thể)      |
| TC1.3 | Không hợp lệ | a=0, b=5       | Lỗi: Cạnh phải lớn hơn 0 | Giá trị biên (Biên lỗi)             |
| TC1.4 | Không hợp lệ | a=-2, b=4      | Lỗi: Cạnh phải lớn hơn 0 | Phân lớp tương đương (Ngoài khoảng) |
| TC1.5 | Ngoại lệ     | a="abc", b=5   | Lỗi: Đầu vào phải là số  | Dữ liệu ngoại lệ (Sai kiểu)         |
