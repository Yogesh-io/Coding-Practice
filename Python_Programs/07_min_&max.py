# 7. Find Maximum and Minimum in Array
# Write a program to find the maximum and minimum elements in an array.
l1  = [11, 22, 33, 44, 55, 66, 77, 88 ,99]
max = 0 
for i in l1 :
    if i > max:
        max = i

min = l1[0]
for i in l1 :
    if i < min:
        min = i
print(f"min : {min} | max : {max}")