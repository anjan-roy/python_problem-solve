# Find lcm
# ----------------------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
print(lcm(34,12))
print(lcm(3,9))
