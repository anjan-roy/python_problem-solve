# 3. Find factorial
# ----------------------
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return n * factorial(n-1)

print(factorial(5))  # 120