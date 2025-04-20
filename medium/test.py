a = [1, 2, 3, 4, 5]
b = [1] * len(a)

for x, y in zip(b, a):
    print((x, y))
