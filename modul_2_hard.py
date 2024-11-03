n = int(input("Введите число (от 3 до 20):" ))
result = []

for i in range(1, 21):
    for j in range(1, 21):
        for p in range(3, n + 1):
            if n % p == 0:
                if (p - (i + j)) == 0:
                    if [j, i] not in result:
                        if i != j:
                            result.append([i, j])
for a in result:
    print(a[0], a[1], end=' ')






