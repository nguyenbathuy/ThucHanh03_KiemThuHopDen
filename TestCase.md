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

## Bài 2: Tính diện tích hình chữ nhật

- **Đầu vào:** Chiều dài `a`, chiều rộng `b` (kiểu số thực).
- **Đầu ra mong đợi:** Giá trị diện tích `S = a * b`. Báo lỗi nếu dữ liệu sai.
- **Kỹ thuật áp dụng:** Phân lớp tương đương & Phân tích giá trị biên.

| Mã TC | Loại dữ liệu | Đầu vào (a, b) | Đầu ra mong đợi          | Kỹ thuật kiểm thử                   |
| ----- | ------------ | -------------- | ------------------------ | ----------------------------------- |
| TC2.1 | Hợp lệ       | a=5, b=3       | 15.0                     | Phân lớp tương đương (Trong khoảng) |
| TC2.2 | Biên hợp lệ  | a=2, b=0.5     | 1.0                      | Giá trị biên                        |
| TC2.3 | Không hợp lệ | a=0, b=5       | Lỗi: Cạnh phải lớn hơn 0 | Giá trị biên (Biên lỗi)             |
| TC2.4 | Không hợp lệ | a=-3, b=4      | Lỗi: Cạnh phải lớn hơn 0 | Phân lớp tương đương (Ngoài khoảng) |
| TC2.5 | Ngoại lệ     | a="xyz", b=5   | Lỗi: Đầu vào phải là số  | Dữ liệu ngoại lệ (Sai kiểu)         |

## Bài 3: Giải phương trình bậc 2 ($ax^2 + bx + c = 0$)

- **Đầu vào:** Các hệ số `a`, `b`, `c` (kiểu số thực).
- **Đầu ra mong đợi:** Nghiệm của phương trình hoặc thông báo vô nghiệm / vô số nghiệm / lỗi dữ liệu.
- **Kỹ thuật áp dụng:** Phân lớp tương đương (dựa trên các khoảng giá trị của $\Delta = b^2 - 4ac$ và hệ số $a$).

| Mã TC | Loại dữ liệu | Đầu vào (a, b, c) | Đầu ra mong đợi         | Kỹ thuật kiểm thử / Kịch bản                  |
| ----- | ------------ | ----------------- | ----------------------- | --------------------------------------------- |
| TC3.1 | Hợp lệ       | a=1, b=-3, c=2    | x1=2.0, x2=1.0          | Phân lớp $\Delta > 0$ (Có 2 nghiệm phân biệt) |
| TC3.2 | Hợp lệ       | a=1, b=-2, c=1    | x1=x2=1.0               | Phân lớp $\Delta = 0$ (Có nghiệm kép)         |
| TC3.3 | Hợp lệ       | a=1, b=1, c=1     | Vô nghiệm               | Phân lớp $\Delta < 0$ (Vô nghiệm thực)        |
| TC3.4 | Biên hợp lệ  | a=0, b=2, c=-4    | x=2.0                   | Biên $a=0$ (Trở thành phương trình bậc 1)     |
| TC3.5 | Biên hợp lệ  | a=0, b=0, c=5     | Vô nghiệm               | Biên $a=0, b=0, c \neq 0$                     |
| TC3.6 | Biên hợp lệ  | a=0, b=0, c=0     | Vô số nghiệm            | Biên $a=0, b=0, c=0$                          |
| TC3.7 | Ngoại lệ     | a="x", b=2, c=1   | Lỗi: Đầu vào phải là số | Dữ liệu ngoại lệ (Sai kiểu)                   |

## Bài 4: Tính số ngày của một tháng

- **Đầu vào:** `thang`, `nam` (kiểu số nguyên).
- **Đầu ra mong đợi:** Số ngày của tháng đó (28, 29, 30 hoặc 31 ngày). Báo lỗi nếu dữ liệu sai.
- **Kỹ thuật áp dụng:** Phân lớp tương đương & Phân tích giá trị biên.
  - Lớp hợp lệ: Tháng thuộc {1,3,5,7,8,10,12} (31 ngày), {4,6,9,11} (30 ngày), {2} (28/29 ngày tuỳ năm nhuận).
  - Lớp không hợp lệ: Tháng < 1 hoặc Tháng > 12. Năm < 1.

| Mã TC | Loại dữ liệu | Đầu vào (tháng, năm) | Đầu ra mong đợi                | Kỹ thuật kiểm thử / Kịch bản                    |
| ----- | ------------ | -------------------- | ------------------------------ | ----------------------------------------------- |
| TC4.1 | Hợp lệ       | thang=1, nam=2023    | 31                             | Phân lớp tương đương (Tháng có 31 ngày)         |
| TC4.2 | Hợp lệ       | thang=4, nam=2023    | 30                             | Phân lớp tương đương (Tháng có 30 ngày)         |
| TC4.3 | Hợp lệ       | thang=2, nam=2024    | 29                             | Phân lớp tương đương (Tháng 2, năm nhuận)       |
| TC4.4 | Hợp lệ       | thang=2, nam=2023    | 28                             | Phân lớp tương đương (Tháng 2, năm không nhuận) |
| TC4.5 | Không hợp lệ | thang=0, nam=2023    | Lỗi: Tháng phải từ 1 đến 12    | Giá trị biên (Biên dưới của tháng)              |
| TC4.6 | Không hợp lệ | thang=13, nam=2023   | Lỗi: Tháng phải từ 1 đến 12    | Giá trị biên (Biên trên của tháng)              |
| TC4.7 | Ngoại lệ     | thang=5.5, nam=2023  | Lỗi: Đầu vào phải là số nguyên | Dữ liệu ngoại lệ (Sai kiểu)                     |

## Bài 5: Kiểm tra số nguyên tố

- **Đầu vào:** Số nguyên `n`.
- **Đầu ra mong đợi:** Kết luận "Là số nguyên tố" hoặc "Không phải số nguyên tố". Báo lỗi nếu dữ liệu sai.
- **Kỹ thuật áp dụng:** Phân lớp tương đương & Phân tích giá trị biên.

| Mã TC | Loại dữ liệu      | Đầu vào (n) | Đầu ra mong đợi                | Kỹ thuật kiểm thử / Kịch bản                    |
| ----- | ----------------- | ----------- | ------------------------------ | ----------------------------------------------- |
| TC5.1 | Hợp lệ            | n = 7       | Là số nguyên tố                | Phân lớp tương đương (Số nguyên tố)             |
| TC5.2 | Hợp lệ            | n = 9       | Không phải số nguyên tố        | Phân lớp tương đương (Hợp số)                   |
| TC5.3 | Biên hợp lệ       | n = 2       | Là số nguyên tố                | Giá trị biên (Số nguyên tố nhỏ nhất)            |
| TC5.4 | Biên không hợp lệ | n = 1       | Không phải số nguyên tố        | Giá trị biên (Ngay dưới ranh giới số nguyên tố) |
| TC5.5 | Không hợp lệ      | n = -3      | Lỗi: n phải là số tự nhiên > 1 | Phân lớp tương đương (Số âm)                    |
| TC5.6 | Ngoại lệ          | n = "5.5"   | Lỗi: Đầu vào phải là số nguyên | Dữ liệu ngoại lệ (Sai kiểu)                     |
