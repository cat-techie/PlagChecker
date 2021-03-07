# Created by Morozov Pavel
# Date 16.09.2020
# Task Description: Решить в целых числах уравнение: (ax+b)/(cx+d) = 0

try:
    a = int(input("Введите переменную a: "))
    b = int(input("Введите переменную b: "))
    c = int(input("Введите переменную c: "))
    d = int(input("Введите переменную d: "))
except ValueError:
    exit(1)

if a == 0 and b == 0:
    print("INF")
else:
    x = -b / a
    if c * x + d == 0 or x != round(x):
        print("NO")
    else:
        print(x)
