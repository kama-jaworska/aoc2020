import copy


def get_boot_code(input_file):
    return [line.split() for line in open(input_file, "r").read().splitlines()]


def parse_instruction(idx, operation, arg):
    if operation == "nop":
        next_idx = idx+1
        increment = 0
    elif operation == "acc":
        next_idx = idx+1
        increment = int(arg)
    elif operation == "jmp":
        next_idx = idx + int(arg)
        increment = 0
    else:
        print("Unknown operation", operation)

    return next_idx, operation, increment


def solve_part_1(boot_code):
    idx = 0
    completed_ops = [False] * (len(boot_code))
    accumulator = 0

    while not completed_ops[idx]:
        next_idx, _, increment = parse_instruction(idx, boot_code[idx][0], boot_code[idx][1])
        completed_ops[idx] = True
        accumulator += increment
        idx = next_idx

    return False, accumulator


def part_2_crawler(boot_code):
    idx = 0
    completed_ops = [False] * (len(boot_code))
    accumulator = 0

    while not completed_ops[idx]:
        next_idx, _, increment = parse_instruction(idx, boot_code[idx][0], boot_code[idx][1])
        completed_ops[idx] = True
        accumulator += increment
        if next_idx == len(boot_code):
            return True, accumulator
        idx = next_idx

    return False, accumulator


def get_operation_indexes(operation_name, boot_code):
    return [idx for idx, line in enumerate(boot_code) if line[0] == operation_name]


def swap_operation(boot_code, old_op, new_op, idx):
    swapped_boot_code = boot_code
    if swapped_boot_code[idx][0] != old_op:
        print("Debug! Wrong op sent for swap!!", swapped_boot_code[idx][0])
    swapped_boot_code[idx][0] = new_op

    return swapped_boot_code


def iterate_thru_swaps(boot_code, old_op, new_op):
    operation_indexes = get_operation_indexes(old_op, boot_code)
    for idx in operation_indexes:
        code_copy = copy.deepcopy(boot_code)
        swapped_boot_code = swap_operation(code_copy, old_op, new_op, idx)
        terminated, accumulator = part_2_crawler(swapped_boot_code)

        if terminated:
            print("Found the lucky boy!", old_op, new_op, idx, terminated, accumulator)
            return True, accumulator
    return False, None


def solve_part_2(boot_code):
    terminated, accumulator = iterate_thru_swaps(boot_code, "nop", "jmp")
    if not terminated:
        terminated, accumulator = iterate_thru_swaps(boot_code, "jmp", "nop")

    return terminated, accumulator


if __name__ == "__main__":
    boot_code = get_boot_code("input.txt")
    print("PART 2:", solve_part_2(boot_code))
    print("PART 1:", solve_part_1(boot_code))

