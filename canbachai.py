# Import thư viện
# from math import sqrt

import math

# Nhập vào
a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
print("Bạn vừa nhập vào a = " + str(a) + "; b = " + str(b) + "; c = " + str(c) + ";")

# tinh denta
delta = (b * b) - 4 * (a * c)
print("Delta: " + str(delta))


# Tính căng bậc 2
if float(delta) < 0:
    print("Phương trình vô nghiệm")
elif float(delta) == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép: " + str(x))
elif float(delta) > 0:
    print("Phương trình có 2 nghiệm phâ biệt")
    m = (-b + (math.sqrt(delta))) / (2*a)
    print("Nghiệm x1 = " + str(m))
    n = (-b - (math.sqrt(delta))) / (2*a)
    print("Nghiệm x2 = " + str(n))
