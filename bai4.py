def tinh_so_ngay(thang, nam):
    try:
        # Ép kiểu sang số nguyên
        thang = int(thang)
        nam = int(nam)
        
        # Kiểm tra điều kiện hợp lệ
        if thang < 1 or thang > 12:
            return "Lỗi: Tháng phải từ 1 đến 12"
        if nam < 1:
            return "Lỗi: Năm phải lớn hơn 0"
            
        # Kiểm tra năm nhuận
        la_nam_nhuan = (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0))
        
        # Tính số ngày
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif thang in [4, 6, 9, 11]:
            return 30
        else: # Tháng 2
            return 29 if la_nam_nhuan else 28
            
    except ValueError:
        return "Lỗi: Đầu vào phải là số nguyên"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 4: TÍNH SỐ NGÀY CỦA THÁNG")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ]:")
print(f"TC4.1 (tháng 1, 2023):   Kết quả = {tinh_so_ngay(1, 2023)} ngày")
print(f"TC4.2 (tháng 4, 2023):   Kết quả = {tinh_so_ngay(4, 2023)} ngày")
print(f"TC4.3 (tháng 2, 2024):   Kết quả = {tinh_so_ngay(2, 2024)} ngày (Năm nhuận)")
print(f"TC4.4 (tháng 2, 2023):   Kết quả = {tinh_so_ngay(2, 2023)} ngày (Không nhuận)")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ, BIÊN & NGOẠI LỆ]:")
print(f"TC4.5 (tháng 0, 2023):   Kết quả = {tinh_so_ngay(0, 2023)}")
print(f"TC4.6 (tháng 13, 2023):  Kết quả = {tinh_so_ngay(13, 2023)}")
print(f"TC4.7 (tháng 5.5, 2023): Kết quả = {tinh_so_ngay('5.5', 2023)}")
print("======================================================\n")