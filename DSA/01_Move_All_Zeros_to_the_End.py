# 1. Move All Zeros to the End 
# Example 
 
# Input: [0, 1, 0, 3, 12] 
# Output: [1, 3, 12, 0, 0]


a = [0, 1, 0, 3, 12] 

def move_zeros(a):
    j = 0

    for i in range(len(a)):

        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j +=1
    return a

print(move_zeros(a))