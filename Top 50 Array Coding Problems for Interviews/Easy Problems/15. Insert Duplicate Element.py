a = [1, 0, 2, 3, 0, 4, 5, 0]

k = 0
final =[]

for i in a:
    final.append(i)
    if i==k:
        final.append(k)

print(final[:len(a)])