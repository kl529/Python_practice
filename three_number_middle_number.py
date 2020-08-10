a = input()
b = a.split(" ")

for i in range(3):
    b[i] = int(b[i])

b = list(b)
b.pop(b.index(min(b)))
b.pop(b.index(max(b)))

print(b[0])
