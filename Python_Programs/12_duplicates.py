# 12. Remove Duplicates from Array
# Write a program to remove duplicate elements from an array.
l1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
print(list(set(l1)))


unique = []
for num in l1:
    if num not in unique:
        unique.append(num)
print(unique)