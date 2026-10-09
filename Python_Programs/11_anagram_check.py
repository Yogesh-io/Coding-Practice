# 11. Anagram Check
# Write a program to check if two given strings are anagrams of each other.

s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")