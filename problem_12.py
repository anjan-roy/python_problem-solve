# Find common elements
def common_elements(a, b):
    return list(set(a) & set(b))
s1={2,3,4,5}
s2={3,4,6,9}
print(common_elements(s1,s2))