with open('input.txt') as file:
    data = file.read().splitlines()

results = [0]
for item in data:
    results.append(results[-1] + int(item) if item else 0)

# part 1 solution = 68787
print(max(results))

# part 2 solution = 198041
results.sort()
print(results[-1] + results[-2] + results[-3])
