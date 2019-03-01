import math

print("1.1")
print(" x | 1 | 2 | 3 | 4 | 5")
print("---+---+---+---+---+---")
print(" у | 3 | 1 | 5 | 4 | 2 ")

print("1.2")
x = int(input("Введите число: "))
s = int(x / 100)
d = int((x / 10) % 10)
e = int((x % 10))

sum = s + d + e
print("Сумма = ", sum)

print("1.3")
x = int(input("Введите первый катет: "))
y = int(input("Введите второй катет: "))
print(math.hypot(x, y))

print("1.4")
print(3 + 1/(7 + 1/(15 + 1/(1 + 1/292))))

print("1.5")
z1 = complex(input("z1 = "))
print("f(z1) = ",4*z1**4 + 3*z1**3 + 2*z1**2 + z1 + 1)
z2 = complex(input("z2 = "))
print("f(z2) = ",z2**4 + 2*z2**2 + 1)

