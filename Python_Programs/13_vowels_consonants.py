# 13. Count Vowels and Consonants.

s1 = input("Enter Input: ").strip().lower()
vowels = "aeiou"
vowels_ct = 0
consonants_ct = 0

for char in s1:
    if char in vowels:
        vowels_ct+=1
    else:
        consonants_ct+=1

print(f"Vowels Count = {vowels_ct} | Consonants Count = {consonants_ct}")

