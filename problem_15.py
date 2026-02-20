# Find gcd
# ----------------------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(43,78))