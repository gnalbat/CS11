# Initialize dictionary from text file, create tuple
def GetFilename():
    filename = input()
    return filename

def GenerateDictionary():
    with open(GetFilename()) as dictionary:
        dictionary = tuple(line.strip() for line in dictionary)
        return dictionary

# Get anagrams
def main():
    dictionary = GenerateDictionary()
    t = int(input())
    while t > 0:
        word = input()
        word = word.lower()
        anagrams = []
        for i in range(0, len(dictionary)):
            if sorted(word) == sorted(dictionary[i]):
                anagrams.append(dictionary[i])
        anagrams = sorted(anagrams)
        anagramslex = ''
        for i in range(0, len(anagrams)):
            if i == 0:
                anagramslex += anagrams[i]
            else:
                anagramslex += ' ' + anagrams[i]
        print(anagramslex)
        t -= 1

# Run main
main()
