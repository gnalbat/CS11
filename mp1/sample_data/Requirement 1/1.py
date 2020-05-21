# Initialize
def GetFilename():
    filename = input()
    return filename

# Main mendoza
def main():
    with open(GetFilename()) as dictionary:
        for line in dictionary:
            print(line.strip())

main()
