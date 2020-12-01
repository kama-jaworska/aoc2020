import itertools


## PART 1
entries = open("01/input.txt", "r").read().splitlines()

for pair in itertools.permutations(entries, 2):
    int1 = int(pair[0])
    int2 = int(pair[1])
    if int1 + int2 == 2020:
        print("Found the Part 1 pair! ", int1, int2)
        print("Part 1 product: ", str(int1*int2))
        break

## PART 2
for triple in itertools.permutations(entries, 3):
    int1 = int(triple[0])
    int2 = int(triple[1])
    int3 = int(triple[2])
    if int1 + int2 + int3 == 2020:
        print("Found the Part 2 triplet! ", int1, int2, int3)
        print("Part 2 product: ", str(int1*int2*int3))
        break