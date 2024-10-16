a = [1, 32, 4, 56, 8, 75, 4, 55]

r = [2 * x if x % 2 else x for x in a]

for i, n in enumerate(r):
    print(n)

print(r)
