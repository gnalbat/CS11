'''
2018-01526
5_2 Canonical Prime Factorization
'''

t = int(input())

while t > 0:
    N = int(input())

    # find primes from 2 to N using sieve of erastosthenes
    marked = [False for i in range(N+1)]
    marked[0] = True
    marked[1] = True
    i = 2
    while i <= N:
        if marked[i] == True:
            i += 1
            continue

        p = i
        multiple = 2*p
        while multiple <= N:
            marked[multiple] = True
            multiple += p
        i += 1

    primes = []
    for i in range(N+1):
        if not marked[i]:
            primes.append(i)

    # find factors from the list of primes
    factors = []
    for i in range(0, len(primes)):
        if N % primes[i] == 0:
            currentval = N
            k = 0
            while currentval % primes[i] == 0:
                k += 1
                currentval = currentval / primes[i]
            factors.append("(" + str(primes[i]) + "^" + str(k) + ")")
            continue
        else:
            continue

    # convert list to string
    factorstrip = ''.join(factors)
    print(factorstrip)

    t -= 1
