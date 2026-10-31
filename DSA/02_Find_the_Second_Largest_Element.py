# 2. Find the Second Largest Element 
 
# Input: [10, 5, 20, 8, 20] 
# Output: 10 

a = [10, 5, 20, 8, 20] 
def SecondHighest(a):
    first = float('-inf')
    second = float('-inf')

    for i in a:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i

    return second

print(SecondHighest(a))