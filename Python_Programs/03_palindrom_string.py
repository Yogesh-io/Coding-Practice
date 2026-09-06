# 3. Palindrome Check
# Write a program to check if a given string is a palindrome.

s1 = input()
if s1 == s1[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")