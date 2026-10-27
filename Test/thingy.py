import math

list = []
thing = 4

for i in range(2, thing):
    n = thing / i
    if thing % i == 0:
        list.append(int(i))
        if n == i:
            list.append(int(n))
    print(list)
