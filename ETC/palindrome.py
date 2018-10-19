w = input()

word = w.split()
combo = (''.join(word)).lower()

if combo == combo[::-1]:
        print("palindrome")
else:
        print("not a palindrome")
