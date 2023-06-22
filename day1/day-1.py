input = open('input.txt')

data = input.read().splitlines()
index = 0
results = []
for item in data:
    if item:
        if len(results) > index:
            value = results[index]
            results[index] = value + int(item)
        else:
            results.insert(index, int(item))
    else:
        index += 1

print(max(results))
input.close()
