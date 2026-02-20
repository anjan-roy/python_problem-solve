#  Count frequency
# ----------------------
def frequency(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return freq
l=[3,4,5,6,7,3]
print(frequency(l))