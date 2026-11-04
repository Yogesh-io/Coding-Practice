# 4. Count Character Frequency 
 
# Input: "programming"
# Output:  p:1 r:2 o:1 g:2 a:1 m:2 i:1 n:1

a = "programming"
def CountFrq(a):
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch,0) + 1

    return freq
print(CountFrq(a))