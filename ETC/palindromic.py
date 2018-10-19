import time

s = time.time()

largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if product > largest:
            l3 = str(product % 10) + str((product // 10) % 10) + str((product // 100) % 10)
            f3 = str((product // 100000) % 10) + str((product // 10000) % 10) + str(((product // 1000) % 10))
            if l3 == f3:
                largest = product
            else:
                continue
        else:
            continue

print(largest)

e = time.time()
time = e - s
print(time)
