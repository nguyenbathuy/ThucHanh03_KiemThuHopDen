# Hàm tính giai thừa (Yêu cầu bắt buộc của bài toán)
def tinh_giai_thua(k):
    if k == 0 or k == 1:
        return 1
    gt = 1
    for i in range(2, k + 1):
        gt *= i
    return gt

# Hàm tính tổng S
def tinh_tong_giai_thua(n):
    try:
        n = int(n)
        
        # Điều kiện: n phải là số nguyên dương (để bắt đầu từ 1!)
        if n < 1:
            return "Lỗi: n phải là số nguyên dương"
            
        S = 0
        for i in range(1, n + 1):
            S += tinh_giai_thua(i) # Gọi lại hàm tính giai thừa
            
        return S
        
    except ValueError:
        return "Lỗi: Đầu vào phải là số nguyên"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 8: TÍNH TỔNG GIAI THỪA")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ & BIÊN]:")
print(f"TC8.1 (n=3):     Kết quả = {tinh_tong_giai_thua(3)}")
print(f"TC8.2 (n=4):     Kết quả = {tinh_tong_giai_thua(4)}")
print(f"TC8.3 (n=1):     Kết quả = {tinh_tong_giai_thua(1)}")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ]:")
print(f"TC8.4 (n=0):     Kết quả = {tinh_tong_giai_thua(0)}")
print(f"TC8.5 (n=-2):    Kết quả = {tinh_tong_giai_thua(-2)}")
print(f"TC8.6 (n='abc'): Kết quả = {tinh_tong_giai_thua('abc')}")
print("======================================================\n")