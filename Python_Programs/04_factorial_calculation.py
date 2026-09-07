# 4. Factorial Calculation
# Write a program to calculate the factorial of a given number using recursion.

def fact(n):
    if n == 0 or n ==1:
        return 1
    return n * fact(n-1)

print(fact(6))