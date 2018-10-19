'''
2018-01526
5_3 Polynomial Addition
'''

t = int(input())

while t > 0:
    p = input()
    q = input()
    p = [int(i) for i in p.split()]
    q = [int(i) for i in q.split()]
    r = []

    if (p[0] == q[0] == 0) and (p[1] + q[1] == 0):
        sum = '0x^0'
    else:
        if p[0] > q[0]:
            hterm = p[0]
            lterm = q[0]
            for i in range(hterm - lterm):
                q.append(0)
        elif p[0] < q[0]:
            hterm = q[0]
            lterm = p[0]
            for i in range(hterm - lterm):
                p.append(0)
        else:
            hterm = p[0]

        for i in range(1, hterm + 2):
            r.append(p[i] + q[i])

        for i in range(hterm, -1, -1):
            j = 1
            while r[i] == r[hterm] == 0:
                hterm = hterm - j
                j += 1
            if r[i] == r[hterm]:
                sum = str(r[i]) + 'x^' + str(i)
                curterm = ''
            else:
                if r[i] < 0:
                    curterm = ' - ' + str(r[i] * -1) + 'x^' + str(i)
                elif r[i] > 0:
                    curterm = ' + ' + str(r[i]) + 'x^' + str(i)
                else:
                    continue
            sum = sum + curterm

    print(sum)

    t -= 1
