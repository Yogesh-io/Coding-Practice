# 14. Neon Number Program
# A neon number is a special number where the sum of the digits of its square is equal to the number itself

n = int(input())
square = n ** 2
sum = 0
while square > 0:
    sum = sum + (square % 10)
    square //=10

if sum == n:
    print("Neon")
else:
    print("Not Neon")
