# Import choice from module random for randomization and clear for clearing
from interface import clear
from random import choice

# 1 Seeding words
def get_filename():
    clear()
    filename = input("Enter dictionary filename: ")
    foldered = "dictionaries/" + filename
    return foldered, filename

def generate_dictionary():
    filename = get_filename()
    with open(filename[0]) as dictionary:
        dictionary = tuple(line.strip() for line in dictionary)
        return dictionary, filename[1]

# 2 Picking words
def pick_words(gamemode, dictionary):
    if gamemode == '1':
        word = choice(dictionary)
        return word
    elif gamemode == '2':
        x = []
        words = []
        for i in range(3):
            x.append(choice(dictionary))
        for i in x:
            words.append(i)
        return words

# 3 Searching for anagrams
def find_anagrams(word, dictionary):
    anagrams = []
    for i in range(0, len(dictionary)):
        if sorted(word) == sorted(dictionary[i]) and word != dictionary[i]:
            anagrams.append(dictionary[i])
    return anagrams

def anagram_chars(anagrams):
    achars = []
    for i in range(0, len(anagrams)):
        achars += list(anagrams[i])
    return achars

# 4 Combining words
def merge(words):
    for i in range(0, len(words)):
        if i == 0:
            chars = list(words[i])
        else:
            for j in range(0, len(words[i])):
                tmp = list(words[i])
                if tmp.count(tmp[j]) > chars.count(tmp[j]):
                    for k in range(0, tmp.count(tmp[j]) - chars.count(tmp[j])):
                        chars.append(tmp[j])
    chars = ''.join(sorted(chars))
    return chars

# 5 Checking words

def wh_answers(dictionary, chars):
    answers = []
    for j in dictionary:
        word = list(j)
        for i in word:
            if word.count(i) <= chars.count(i):
                inside = True
            else:
                inside = False
                break

        if inside == True:
            answers.append(j)
    return answers

# 6 Scrabble
def scrabble():
    pointgroups = {
    ('e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u') : 1,
    ('d', 'g') : 2,
    ('b', 'c', 'm', 'p') : 3,
    ('f', 'h', 'v', 'w', 'y') : 4,
    ('k') : 5,
    ('j', 'x') : 8,
    ('q', 'z') : 10
    }

    return pointgroups

def count(pointgroups, chars):
    score = 0
    for j in pointgroups:
        for i in range(0, len(j)):
            if j[i] in chars:
                score += pointgroups[j] * chars.count(j[i])
    return score

def hps(chars):
    achars = []
    for i in range(0, len(chars)):
        achars += list(chars[i])
    chars = achars

    pointgroups = scrabble()
    score = count(pointgroups, chars)
    return score

def points(chars):
    pointgroups = scrabble()
    score = count(pointgroups, chars)
    return score
