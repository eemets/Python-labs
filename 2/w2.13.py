x = float(input('Input x: '))
y = float(input('Input y: '))
z = float(input('Input z: '))

if abs(x) > abs(y) and abs(x) > abs(z):
    print(f'Найбільше за модулем {abs(x)}.')
elif abs(y) > abs(x) and abs(y) > abs(z):
    print(f'Найбільше за модулем {abs(y)}.')
else:
    print(f'Найбільше за модулем {abs(z)}.')


if abs(x) < abs(y) and abs(x) < abs(z):
    print(f'Найменше за модулем {abs(x)}.')
elif abs(y) < abs(x) and abs(y) < abs(z):
    print(f'Найменше за модулем {abs(y)}.')
else:
    print(f'Найменше за модулем {abs(z)}.')


print(f'max(x+y+z, xy-xz+yz, xyz): {max(x+y+z, x*y-x*z+y*z, x*y*z)}')

print(f'max(xy, xz, yz): {max(x*y, x*z, y*z)}')
