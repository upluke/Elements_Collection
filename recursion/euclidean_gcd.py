# 15.0 greatest common divisor (GCD)

# init：
# def GCD(a, b):
#   if b==0:
#     return a
#   return GCD(b,a%b)
# print(GCD(270,192))

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


print(gcd(270, 192))
