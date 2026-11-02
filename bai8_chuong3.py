def cong(a, b, c, d):
    return a * d + b * c, b * d
def tru(a, b, c, d):
    return a * d - b * c, b * d
def nhan(a, b, c, d):
    return a * c, b * d
def chia(a, b, c, d):
    if c == 0:
        return "Khong the chia cho 0"
    return a * d, b * c
a = int(input("Nhap tu so phan so 1: "))
b = int(input("Nhap mau so phan so 1: "))
c = int(input("Nhap tu so phan so 2: "))
d = int(input("Nhap mau so phan so 2: "))
if b == 0 or d == 0:
    print("Mau so phai khac 0")
else:
    print("Tong:", cong(a, b, c, d))
    print("Hieu:", tru(a, b, c, d))
    print("Tich:", nhan(a, b, c, d))
    print("Thuong:", chia(a, b, c, d))
