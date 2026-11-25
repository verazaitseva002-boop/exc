import math
a=int(input())
b=float(input())
print("Сумма=", a+b)
print("Разность=", a-b)
print("Произведение=", a*b)
print("Частное=", a/b)
if a%b==0:
    print("тип: целочисленное")
else:
    print("тип: с остатком")
R=5
sk=math.pi * R**2
q=round(sk,2)
print("Площадь круга=", q)
