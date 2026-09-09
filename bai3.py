import math

def giai_pt_bac_2(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        
        # Trường hợp a = 0, pt trở thành bx + c = 0
        if a == 0:
            if b == 0:
                if c == 0:
                    return "Vô số nghiệm"
                else:
                    return "Vô nghiệm"
            else:
                return f"x = {-c / b}"
                
        # Trường hợp a != 0, tính Delta
        delta = b**2 - 4*a*c
        
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Nghiệm kép x1 = x2 = {x}"
        else:
            return "Vô nghiệm"
            
    except ValueError:
        return "Lỗi: Đầu vào phải là số"

print("======================================================")
print("KẾT QUẢ TEST CASE BÀI 3: GIẢI PHƯƠNG TRÌNH BẬC 2")
print("======================================================")

print("\n[TEST DỮ LIỆU HỢP LỆ & BIÊN]:")
print(f"TC3.1 (a=1, b=-3, c=2):   Kết quả = {giai_pt_bac_2(1, -3, 2)}")
print(f"TC3.2 (a=1, b=-2, c=1):   Kết quả = {giai_pt_bac_2(1, -2, 1)}")
print(f"TC3.3 (a=1, b=1, c=1):    Kết quả = {giai_pt_bac_2(1, 1, 1)}")
print(f"TC3.4 (a=0, b=2, c=-4):   Kết quả = {giai_pt_bac_2(0, 2, -4)}")
print(f"TC3.5 (a=0, b=0, c=5):    Kết quả = {giai_pt_bac_2(0, 0, 5)}")
print(f"TC3.6 (a=0, b=0, c=0):    Kết quả = {giai_pt_bac_2(0, 0, 0)}")

print("\n[TEST DỮ LIỆU NGOẠI LỆ]:")
print(f"TC3.7 (a='x', b=2, c=1):  Kết quả = {giai_pt_bac_2('x', 2, 1)}")
print("======================================================\n")