# Nhập vào
a = float(input("Nhập vào điểm toán của bạn: "))
if float(a>10):
    print("Bạn chỉ có thể nhập nhỏ hơn  hoặc bằng 10 điểm")
    exit()
b = float(input("Nhập vào điểm tin của bạn: "))
if float(a>10):
    print("Bạn chỉ có thể nhập nhỏ hơn  hoặc bằng 10 điểm")
    exit()
print("")

# Xuất Ra
print("Bạn vừa nhập " + str(a) + " điểm toán")
print("Bạn vừa nhập " + str(b) + " điểm tin")
print("")

# Điểm trung bình
c = (a + b) / 2

# In điểm trung bình
print("Công thức: " + "(" + str(a) + " + " + str(b) + ")" + " / " + "2 ")
print("Điểm trung bình của bạn là: " + str(c))

print("")
print("Xếp hạng học lực:")
if float(c)>=9:
    print("Bạn là học sinh xuất sắc")
elif float(c)<=8 and float(c)>=7.5:
    print("Bạn là học sinh giỏi")
elif float(c)<=7.4 and float(c)>=6:
    print("Bạn là học sinh khá")
elif float(c)<=5.9 and float(c)>=3.6:
    print("Bạn là học sinh trung bình")
elif float(c)<=3.5:
    print("Bạn là học sinh yếu")
