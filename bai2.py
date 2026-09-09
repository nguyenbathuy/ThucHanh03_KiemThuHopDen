def tinh_dien_tich_hinh_chu_nhat(a, b):
    try:
        a = float(a)
        b = float(b)
        
        if a <= 0 or b <= 0:
            return "Lỗi: Cạnh phải lớn hơn 0"
        
        return a * b
    except ValueError:
        return "Lỗi: Đầu vào phải là số"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 2: TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ]:")
print(f"TC2.1 (a=5, b=3):        Kết quả = {tinh_dien_tich_hinh_chu_nhat(5, 3)}")
print(f"TC2.2 (a=2, b=0.5):      Kết quả = {tinh_dien_tich_hinh_chu_nhat(2, 0.5)}")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ]:")
print(f"TC2.3 (a=0, b=5):        Kết quả = {tinh_dien_tich_hinh_chu_nhat(0, 5)}")
print(f"TC2.4 (a=-3, b=4):       Kết quả = {tinh_dien_tich_hinh_chu_nhat(-3, 4)}")
print(f"TC2.5 (a='xyz', b=5):    Kết quả = {tinh_dien_tich_hinh_chu_nhat('xyz', 5)}")
print("======================================================\n")