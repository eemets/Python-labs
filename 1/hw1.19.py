from math import sqrt

a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

d = b**2 - 4*a*c
x1 = (-b + sqrt(d)) / (2*a)
x2 = (-b - sqrt(d)) / (2*a)

print(f'd = {d}; x1 = {x1}; x2 = {x2}.')
