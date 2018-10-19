'''
2018-01526
5_4 Finite Continued Fractions
'''

t = int(input())

while t > 0:
    line = input()
    a = [int(i) for i in line.split()]
    n = len(a) - 1
    sum = 0
    while n > 0:
        sum = 1 / (a[n] + sum)
        n -= 1
    sum += a[0]
    print(round(sum,6))

    t -= 1
