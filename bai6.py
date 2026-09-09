def tinh_tong_dan_dau(n):
    try:
        n = int(n)
        
        if n < 1:
            return "Lỗi: n phải là số nguyên dương"
            
        S = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                S += i  # i lẻ thì cộng
            else:
                S -= i  # i chẵn thì trừ
                
        return S
        
    except ValueError:
        return "Lỗi: Đầu vào phải là số nguyên"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 6: TÍNH TỔNG ĐAN DẤU")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ & BIÊN]:")
print(f"TC6.1 (n = 4):      Kết quả = {tinh_tong_dan_dau(4)}")
print(f"TC6.2 (n = 5):      Kết quả = {tinh_tong_dan_dau(5)}")
print(f"TC6.3 (n = 1):      Kết quả = {tinh_tong_dan_dau(1)}")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ]:")
print(f"TC6.4 (n = 0):      Kết quả = {tinh_tong_dan_dau(0)}")
print(f"TC6.5 (n = -5):     Kết quả = {tinh_tong_dan_dau(-5)}")
print(f"TC6.6 (n = 'abc'):  Kết quả = {tinh_tong_dan_dau('abc')}")
print("======================================================\n")