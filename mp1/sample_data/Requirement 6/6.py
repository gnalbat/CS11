# Initialize dictionary from text file, create tuple
def GetFilename():
    filename = input()
    return filename

def GenerateDictionary():
    with open(GetFilename()) as dictionary:
        dictionary = tuple(line.strip() for line in dictionary)
        return dictionary

# Get scrabble values

def score(chars):
    p1 = ('e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u')
    p2 = ('d', 'g')
    p3 = ('b', 'c', 'm', 'p')
    p4 = ('f', 'h', 'v', 'w', 'y')
    p5 = ('k')
    p8 = ('j', 'x')
    p10 = ('q', 'z')
    pointgroups = {p1 : 1, p2 : 2, p3 : 3, p4 : 4, p5 :5, p8 : 8, p10 : 10}

    score = 0
    for j in pointgroups:
        for i in range(0, len(j)):
            if j[i] in chars:
                score += pointgroups[j] * chars.count(j[i])
    return(score)

# Get words
def main():
    dictionary = GenerateDictionary()
    t = int(input())
    while t > 0:
        jumbled = input()
        jumbled = jumbled.lower()
        jumbled = list(jumbled)
        chars = []
        for i in range(0, len(dictionary)):
            tmp = list(dictionary[i])
            for j in range(0, len(tmp)):
                if tmp.count(tmp[j]) <= jumbled.count(tmp[j]):
                    inside = True
                else:
                    inside = False
                    break

            if inside == True:
                for i in tmp:
                    chars.append(i)
        print(score(chars))
        t -= 1

# Run main
main()
