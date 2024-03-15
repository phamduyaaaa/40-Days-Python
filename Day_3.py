import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2-4*a*c
if delta > 0:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("phương trình có 2 nghiệm phân biệt là: x1=",x1,"x2=",x2)
elif delta == 0:
    x1 = (-b)/2*a
    print("phương trình có nghiệm kép là: x1=x2=",x1)
else:
    print("Phương trình vô nghiệm.")