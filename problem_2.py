# 2. Check palindrome
# ----------------------
def is_palindrome(s):
    # Compare string with its reverse
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("sir"))  # Flase
print(is_palindrome("python"))  # Flase
print(is_palindrome("kjashe"))  # Flase
