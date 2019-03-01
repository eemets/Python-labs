from math import sqrt


a = int(input('Input length of a: '))
b = int(input('Input length of b: '))
c = int(input('Input length of c: '))

p = (a + b + c) / 2
S = sqrt(p*(p - a)*(p - b)*(p - c))

la = (2/(b + c)) * sqrt(b*c*p*(p - 1))
lb = (2/(a + c)) * sqrt(a*c*p*(p - 1))
lc = (2/(a + b)) * sqrt(a*b*p*(p - 1))

ma = 0.5*sqrt(2*b**2+2*c**2-a**2)
mb = 0.5*sqrt(2*a**2+2*c**2-b**2)
mc = 0.5*sqrt(2*a**2+2*b**2-c**2)

ha = 2*S / a
hb = 2*S / b
hc = 2*S / c

print(f'a = {a}, b = {b}, c = {c}.')
print(f'S = {S}.')
print(f'la = {la}, lb = {lb}, lc = {lc}.')
print(f'ma = {ma}, mb = {mb}, mc = {mc}.')
print(f'ha = {ha}, hb = {hb}, hc = {hc}.')
