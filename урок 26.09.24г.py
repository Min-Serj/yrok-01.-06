 # пузырьковая сортировка

a = [9, 8, 3, 14, 55, 6, 7, 44, 54, 54, 45, 452, 2, 43]
for i in range(1, len(a) - 1):
    for element in range(len(a) - 1):
        if a[element] > a[element + 1]:  # если < то развернёт список от большего к меньшему
            a[element], a[element+1] = a[element+1], a[element]
            #break
print((a))

# сортировка выбором
for i in range(len(a) -1):
    if a[i] > a[i + 1]:      # если < то развернёт список от большего к меньшему
        a[i], a[i + 1] = a[i + 1], a[i]
        for k in range(i,0, - 1):
            if a[k] < a[k - 1]:     # если > то развернёт список от большего к меньшему
                a[k], a[k - 1] = a[k - 1], a[k]
    elif a[i] <= a[i + 1]:
        pass
print(a)
































