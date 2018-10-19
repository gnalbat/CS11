# Initialize dictionary from text file, create tuple
def GetFilename():
    filename = input()
    return filename

def GenerateDictionary():
    with open(GetFilename()) as dictionary:
        dictionary = tuple(line.strip() for line in dictionary)
        return dictionary

# Get words
def main():
    dictionary = GenerateDictionary()
    t = int(input())
    while t > 0:
        words = str(input())
        words = words.lower()
        words = words.split()
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
        print(chars)
        t -= 1

# Run main
main()
