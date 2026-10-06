# 8. Check Prime Number
# Write a program to check if a given number is a prime number.

n = int(input(""))
count = 0
if n <= 1:
    print("Not Prime Number")
else:
    for i in range(2,n):
        if n % i == 0:
            count+=1
            print("Not Prime Number")
            break
    if count == 0:
        print("Prime Number")