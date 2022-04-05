# coding=utf-8
import socket
import os
import math
from binascii import hexlify

print("1 - Check Info Máy Bạn")
print("2 - Tìm IP Của Một Website")
print("3 - Chuyển đổi địa chỉ IPv4 sang địa chỉ cấp thấp")
print("4 - căn bậc 2")
try:
  a = int(input("Nhập lựa chọn: "))
  if int(a) == 1:
      hostname = socket.gethostname()
      ip_address = socket.gethostbyname(hostname)
      PublicIP = os.popen('curl -s ifconfig.me').readline()
      print("Hostname: {}".format(hostname))
      print("IP: {}".format(ip_address))
      print("IP Public: {}".format(PublicIP))
  elif int(a) == 2:
      website = input("Nhập vào website: ")
      webip = socket.gethostbyname(website)
      print("IP Của web {} Là {}".format(website, webip))
  elif int(a) == 3:
      ip_addr = input("Nhập vào địa chỉ IPv4: ")
      packed_ip_addr = socket.inet_aton(ip_addr)
      unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
      print("IPv4: {} => Packed = {}, Unpacked: {}".format(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))
  elif int(a) == 4:
      try:
        print("Tính căng bậc 2")
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
      except:
        print("Kiểu dữ liệu bạn nhập vào không hợp lệ")
except:
  print("Bạn chỉ được phép nhập số theo danh sách phía trên")
