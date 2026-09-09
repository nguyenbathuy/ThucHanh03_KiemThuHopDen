def tim_ucln(a, b):
    try:
        a = int(a)
        b = int(b)
        
        # Kiểm tra điều kiện đầu vào
        if a <= 0 or b <= 0:
            return "Lỗi: a và b phải là số nguyên dương"
            
        # Thuật toán Euclid tìm UCLN
        while b != 0:
            temp = b
            b = a % b
            a = temp
            
        return a
        
    except ValueError:
        return "Lỗi: Đầu vào phải là số nguyên"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 7: TÌM UCLN CỦA A VÀ B")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ & BIÊN]:")
print(f"TC7.1 (a=12, b=18): Kết quả = {tim_ucln(12, 18)}")
print(f"TC7.2 (a=17, b=5):  Kết quả = {tim_ucln(17, 5)}")
print(f"TC7.3 (a=15, b=15): Kết quả = {tim_ucln(15, 15)}")
print(f"TC7.4 (a=1, b=10):  Kết quả = {tim_ucln(1, 10)}")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ]:")
print(f"TC7.5 (a=0, b=8):   Kết quả = {tim_ucln(0, 8)}")
print(f"TC7.6 (a=-4, b=12): Kết quả = {tim_ucln(-4, 12)}")
print(f"TC7.7 (a='x', b=5): Kết quả = {tim_ucln('x', 5)}")
print("======================================================\n")