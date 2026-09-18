# 5. Fibonacci Sequence
# Write a program to generate the first n numbers in the Fibonacci sequence.

number = int(input(""))
a = 0
b = 1
for _ in range(number):
    print(a)
    a , b = b , a+b