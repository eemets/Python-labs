number = int(input('Input x: '))

s = int(number / 100)
d = int((number / 10) % 10)
e = int((number % 10))

print(f'{s}{d}{e}')
print(f'{s}{e}{d}')
print(f'{d}{s}{e}')
print(f'{d}{e}{s}')
print(f'{e}{d}{s}')
print(f'{e}{s}{d}')
