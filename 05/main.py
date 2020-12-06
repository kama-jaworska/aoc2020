
def binary_search(code, decrement_symbol, increment_symbol):
    min_row_range = 0
    max_row_range = 2**len(code)-1

    for step in range(len(code)):
        mean_point = (min_row_range + max_row_range) // 2

        if code[step] == decrement_symbol:
            max_row_range = mean_point

        elif code[step] == increment_symbol:
            min_row_range = mean_point+1

        else:
            return "search failed on unknown code " + code[step] + code + step

    if min_row_range == max_row_range:
        return min_row_range
    else:
        return "search failed to find solution, ranges not equal " + min_row_range + max_row_range


def parse_input(input_file):
    return open(input_file, "r").read().splitlines()


def solve_part_1(boarding_passes):
    max_seat_id = 0

    for boarding_pass in boarding_passes:
        row = binary_search(boarding_pass[:7], "F", "B")
        column = binary_search(boarding_pass[7:], "L", "R")
        seat_id = row*8 + column

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def solve_part_2(boarding_passes):
    seat_ids = []

    for boarding_pass in boarding_passes:
        row = binary_search(boarding_pass[:7], "F", "B")
        column = binary_search(boarding_pass[7:], "L", "R")
        seat_id = row*8 + column
        seat_ids.append(seat_id)

    for seat in range(min(seat_ids), max(seat_ids)):
        if seat not in seat_ids:
            return seat


def main(input_file):
    boarding_passes = parse_input(input_file)
    print("PART 1: ", solve_part_1(boarding_passes))
    print("PART 2: ", solve_part_2(boarding_passes))


if __name__ == "__main__":
    main("input.txt")

