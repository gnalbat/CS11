t = int(input())

while t > 0:
    n = int(input())
    outerspace = ((2 * (n - 1)) + 1) * ' '
    for i in range(n):
        for j in range(n):
            pyramind = (((n - j - 1) * ' ') + ((2*j+1) * '*') + ((n - j - 1) * ' '))
            s = (n - i - 1) * outerspace
            p = (2*i + 1) * pyramind
            print(s + p.rstrip())
    print()
    t -= 1
