a = []
b = {}
while True:
    c = input()
    if not c:
        break
    a.append(c)

for element in a:
    if element in b:
        b[element] += 1
    else:
        b[element] = 1

print(b)