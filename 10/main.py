def get_sorted_input(input_file):
    return sorted([int(i) for i in open(input_file, "r").read().splitlines()])


def solve_part_1(sorted_list):
    steps_taken = {1: 1,
                   2: 0,
                   3: 1}

    for i in range(1, len(sorted_list)):
        diff = sorted_list[i]-sorted_list[i-1]
        steps_taken[diff] += 1

    return steps_taken[1]*steps_taken[3]


print(solve_part_1(get_sorted_input("input.txt")))
