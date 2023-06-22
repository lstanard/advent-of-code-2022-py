# 0 lost
# 3 draw
# 6 win
# 1 rock (A/X)
# 2 paper (B/Y)
# 3 scissors (C/Z)

with open('input.txt') as file:
    data = file.read().splitlines()

sum = 0
for match in data:
    moves = match.split(' ')
    # if moves[1] == 'X':
    #     sum += 1
    # if moves[1] == 'Y':
    #     sum += 2
    # if moves[1] == 'Z':
    #     sum += 3

    # if moves[0] == 'A' and moves[1] == 'Y':
    #     sum += 6
    # elif moves[0] == 'B' and moves[1] == 'Z':
    #     sum += 6
    # elif moves[0] == 'C' and moves[1] == 'X':
    #     sum += 6
    # elif moves[0] == 'A' and moves[1] == 'Z':
    #     sum += 0
    # elif moves[0] == 'B' and moves[1] == 'X':
    #     sum += 0
    # elif moves[0] == 'C' and moves[1] == 'Y':
    #     sum += 0
    # else:
    #     sum += 3

    if moves[0] == 'A' and moves[1] == 'Y':
        sum += 8
    elif moves[0] == 'A' and moves[1] == 'Z':
        sum += 0
    elif moves[0] == 'B' and moves[1] == 'X':
        sum += 8
    elif moves[0] == 'B' and moves[1] == 'Z':
        sum += 0
    elif moves[0] == 'C' and moves[1] == 'X':
        sum += 0
    elif moves[0] == 'C' and moves[1] == 'Y':
        sum += 8
    else:
        sum += 6

# part 1 solution = 12156
print(sum)
# part 2 solution = 10835
