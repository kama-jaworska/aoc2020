def parse_input(input_file):
    return open(input_file, "r").read().splitlines()


def solve_part_1(answer_list):
    affirmatives = 0
    current_group_letters = ''

    for answer in answer_list:
        current_group_letters += answer

        if len(answer) == 0:
            affirmatives += len(set(current_group_letters))
            current_group_letters = ''

    return affirmatives


def solve_part_2(answer_list):
    affirmatives = 0
    current_group_set = set()

    for idx in range(len(answer_list)):
        answer = answer_list[idx]

        # If the line is empty, record the finished group and move on to the next line
        if len(answer) == 0:
            affirmatives += len(current_group_set)
            current_group_set = set()
            continue

        if len(current_group_set) == 0 and (len(answer_list[idx-1]) == 0 or idx == 0):
            current_group_set = set(answer)
        else:
            current_group_set = current_group_set.intersection(set(answer))

    return affirmatives


def main(input_file):
    answer_list = parse_input(input_file)

    print("PART 1:", solve_part_1(answer_list))
    print("PART 2:", solve_part_2(answer_list))


if __name__ == "__main__":
    main("input.txt")

