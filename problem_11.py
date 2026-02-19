# Find second largest
# ----------------------
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]
l=[34,21,56,78,92,26]
print(second_largest(l))