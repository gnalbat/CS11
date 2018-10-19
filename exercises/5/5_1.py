'''
2018-01526
5_1 Longest Word
'''

t = int(input())

while t > 0:
    line = input()
    words = line.split()
    longest = words[0]
    for i in range(0,len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    print(longest)

    t -= 1
