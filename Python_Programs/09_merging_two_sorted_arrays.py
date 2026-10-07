# 9. Merge Two Sorted Arrays
# Write a program to merge two sorted arrays into a single sorted array.
l1  = [24,6,7,90,564,345,78,9,3,24,23,664,44]
l2  = [394,78,456,856,32,68,43,90,32,8,1,34]
l1.sort()
l2.sort()
# print(sorted(l1+l2))
i,j = 0, 0
merged = []
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merged.append(l1[i])
        i+=1
    else:
        merged.append(l2[j])
        j+=1

while i < len(l1):
        merged.append(l1[i])
        i += 1

while j < len(l2):
        merged.append(l2[j])
        j += 1

print(merged)
