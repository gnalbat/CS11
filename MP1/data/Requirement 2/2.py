# Initialize dictionary from text file, create tuple
def GetFilename():
    filename = input()
    return filename

def GenerateDictionary():
    with open(GetFilename()) as dictionary:
        dictionary = tuple(line.strip() for line in dictionary)
        return dictionary

# Get indices
def main():
    dictionary = GenerateDictionary()
    t = int(input())
    while t > 0:
        indices = input()
        indices = indices.split()
        words = ''
        for i in range(0, len(indices)):
            if i == 0:
                words = dictionary[int(indices[i])]
            else:
                words += ' ' + dictionary[int(indices[i])]
        print(words)
        t -= 1

# Run main
main()
