'''
2018-01526
5_5 Histogram
'''

t = int(input())

while t > 0:
    b = int(input())
    data = input()
    data = [int(i) for i in data.split()]

    highest = 0
    for i in range(0, len(data)):
        if data[i] > highest:
            highest = data[i]

    lowest = highest
    for i in range(0, len(data)):
        if data[i] < lowest:
            lowest = data[i]
        elif len(data) == 1:
            lowest = data[i]

    bincount = ((highest - lowest) // b) + 1
    binstart = lowest

    for i in range(bincount):
        freq = [i for i in data if binstart <= i <= (binstart+(b-1))]
        print(str(binstart) + '-' + str(binstart+(b-1)), len(freq))
        binstart = binstart + b

    print()
    t -= 1
