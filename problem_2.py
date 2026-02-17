# 2. Check palindrome
# ----------------------
def is_palindrome(s):
    # Compare string with its reverse
    return s == s[::-1]

print(is_palindrome("madam"))  # True