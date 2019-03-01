a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

if ((a+b) > c) and ((a+c) > b) and ((c+b) > a):
    print("Треугольник существует")
    if(a**2+b**2==c**2):
        print("Прямоугольный")     
else:
    print("Треугольника не существует")
