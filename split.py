
s = input("stroke: ")

strArray = s.split()
result = []

for i in strArray:
    if i == ''.join(reversed(i)):
        result.append(i)

print(result)

