def tinh_chu_vi_hinh_chu_nhat(a, b):
    try:
        # Ép kiểu sang số thực
        a = float(a)
        b = float(b)
        
        # Kiểm tra điều kiện hợp lệ
        if a <= 0 or b <= 0:
            return "Lỗi: Cạnh phải lớn hơn 0"
        
        return (a + b) * 2
    except ValueError:
        return "Lỗi: Đầu vào phải là số"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 1: TÍNH CHU VI HÌNH CHỮ NHẬT")
print("======================================================")

# ---- GIẢI QUYẾT ISSUE 1: TEST DỮ LIỆU HỢP LỆ ----
print("\n[ISSUE 1] TEST DỮ LIỆU HỢP LỆ:")
print(f"TC1.1 (a=5, b=3):        Kết quả = {tinh_chu_vi_hinh_chu_nhat(5, 3)}")
print(f"TC1.2 (a=0.1, b=0.1):    Kết quả = {tinh_chu_vi_hinh_chu_nhat(0.1, 0.1)}")

# ---- GIẢI QUYẾT ISSUE 2: TEST DỮ LIỆU KHÔNG HỢP LỆ, BIÊN, NGOẠI LỆ ----
print("\n[ISSUE 2] TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ:")
print(f"TC1.3 (a=0, b=5):        Kết quả = {tinh_chu_vi_hinh_chu_nhat(0, 5)}")
print(f"TC1.4 (a=-2, b=4):       Kết quả = {tinh_chu_vi_hinh_chu_nhat(-2, 4)}")
print(f"TC1.5 (a='abc', b=5):    Kết quả = {tinh_chu_vi_hinh_chu_nhat('abc', 5)}")
print("======================================================\n")