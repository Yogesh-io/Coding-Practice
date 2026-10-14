# 15. Armstrong Number
# a number that is equal to the sum of its own digits each raised to the power of the number of digits.

n = int(input())
temp = n
power = len(str(n))
sum = 0
while(n>0):
    digit = n % 10
    sum = sum +(digit ** power)
    n = n//10

if temp == sum:
    print("Armstrong")
