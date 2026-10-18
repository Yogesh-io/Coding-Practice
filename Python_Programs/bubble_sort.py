# 2. Sorting an Array
# Write a program to sort an array of integers using the bubble sort algorithm.

arr = [9,8,7,6,4,3,2,1]
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j] 
print(arr)