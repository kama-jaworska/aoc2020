import itertools


def parse_input(input_file):
    return open(input_file, "r").read().splitlines()


def get_preamble_sums(preamble):
    return [int(pair[0])+int(pair[1]) for pair in itertools.permutations(set(preamble), 2)]


def find_invalid_value(value, preamble_sums):
    return int(value) not in preamble_sums


def find_valid_value(value, preamble_sums):
    return int(value) in preamble_sums


def find_weak_value(input_file, preamble_size):
    lines = parse_input(input_file)
    xmas_sum_incorrect = False
    idx_found = 0

    for value in range(preamble_size, len(lines)):
        preamble = lines[(value-preamble_size):(value)]
        #print(value, lines[value], preamble, (value-preamble_size), (value-1))

        if find_invalid_value(lines[value], get_preamble_sums(preamble)):
            xmas_sum_incorrect = True
            idx_found = value
            break

    return xmas_sum_incorrect, idx_found, lines[idx_found]


def find_p2_slice(lines, WEAK_NUMBER):

    for first_idx in range(len(lines)):
        for second_idx in range(first_idx+1, len(lines)):
            lines_slice = [int(i) for i in lines[first_idx:second_idx]]

            if sum(lines_slice) == WEAK_NUMBER:
                return "AYY", first_idx, second_idx, min(lines_slice),\
                       max(lines_slice), min(lines_slice)+max(lines_slice)



if __name__ == "__main__":
    file = "input.txt"
    lines = parse_input(file)
    preamble_p1 = 25
    WEAK_NUMBER = 69316178

    print("PART 1:", find_weak_value(file, preamble_p1))
    print(find_p2_slice(lines, WEAK_NUMBER))



