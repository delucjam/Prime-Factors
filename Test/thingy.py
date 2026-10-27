import math

list = []
thing = 9

for i in range(2, thing):
    n = thing / i
    if thing % i == 0:
        list.append(int(i))
        if n == i:
            list.append(int(n))
    print(list)

for j in list:
    print('j: ',j)
    for k in range(2, j):
        if j != 2:#but instead is 4 for example
            n_two = j / k #so probably n_two = 2
            if j % k == 0:
                list.append(int(k))
                list.remove(int(j))
                if n_two == k:
                    list.append(int(n_two))

print(list)


