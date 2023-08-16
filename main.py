from math import gcd

a, b, c, d = tuple(map(int, input().split()))

ara = a / b
arc = c / d

if ara == arc:
    print("0/1")
    raise SystemExit
if ara > arc:
    num = a * d - b * c
    den  = a * d
else:
    num = b * c - d * a
    den = b * c

g = gcd(num, den)
print(f"{num // g}/{den // g}")
