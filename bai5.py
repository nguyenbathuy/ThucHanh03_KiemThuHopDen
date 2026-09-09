import math

def kiem_tra_nguyen_to(n):
    try:
        # Ép kiểu sang số nguyên (nếu nhập string '5.5' sẽ nhảy vào except)
        n = int(n)
        
        # Kiểm tra điều kiện đầu vào
        if n <= 1:
            return "Không phải số nguyên tố (hoặc không hợp lệ vì n <= 1)"
            
        # Thuật toán kiểm tra số nguyên tố
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return "Không phải số nguyên tố"
                
        return "Là số nguyên tố"
        
    except ValueError:
        return "Lỗi: Đầu vào phải là số nguyên"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 5: KIỂM TRA SỐ NGUYÊN TỐ")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ & BIÊN]:")
print(f"TC5.1 (n = 7):      Kết quả = {kiem_tra_nguyen_to(7)}")
print(f"TC5.2 (n = 9):      Kết quả = {kiem_tra_nguyen_to(9)}")
print(f"TC5.3 (n = 2):      Kết quả = {kiem_tra_nguyen_to(2)}")
print(f"TC5.4 (n = 1):      Kết quả = {kiem_tra_nguyen_to(1)}")

print("\n[TEST DỮ LIỆU KHÔNG HỢP LỆ & NGOẠI LỆ]:")
print(f"TC5.5 (n = -3):     Kết quả = {kiem_tra_nguyen_to(-3)}")
print(f"TC5.6 (n = '5.5'):  Kết quả = {kiem_tra_nguyen_to('5.5')}")
print("======================================================\n")