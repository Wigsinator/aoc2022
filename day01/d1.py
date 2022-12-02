f = open("d1_input.txt", 'r')

elves = [0]

for line in f:
    if line == "\n":
        elves.append(0)
    else:
        elves[-1] += int(line)

print("Problem 1 answer")
print(max(elves))

# Problem 2
elves.sort(reverse=True)

print("Problem 2 answer")
print(sum(elves[:3]))