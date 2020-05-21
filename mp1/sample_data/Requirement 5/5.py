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
        word = words[1]
        jumbled = list(words[0])
        chars = list(words[1])
        for i in range(0, len(chars)):
            if chars.count(chars[i]) <= jumbled.count(chars[i]):
                inside = True
            else:
                inside = False
                break

        if inside == True and word in dictionary:
            print(True)
        else:
            print(False)

        t -= 1

# Run main
main()
