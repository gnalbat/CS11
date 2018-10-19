word = "snake_case_to_camel_case"

words = word.split("_")

for i in range(0, len(words)):
    words[i] = words[i].capitalize()

word2 = "Camel Case To scnake Kcase"

for j in word2:
    if j.isupper():
        word2 += "_" + j.lower()
    else:
        word2 += j

print(word2)
