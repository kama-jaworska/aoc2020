def parse_input_file(filename):
    records = open(filename, "r").read().splitlines()
    return [record.split(" ") for record in records]

def parse_record(record):
    limits = [int(limit) for limit in record[0].split("-")]
    letter = record[1][:-1]
    password = record[2]
    return limits, letter, password

def solve_part_1(record_list):
    valid_passwords = 0

    for record in record_list:
        limits, letter, password = parse_record(record)

        if password.count(letter) in range(limits[0], limits[1]+1):
            valid_passwords += 1
    
    return valid_passwords

def solve_part_2(record_list):
    valid_passwords = 0

    for record in record_list:
        limits, letter, password = parse_record(record)
        letter_used_counter = 0

        for limit in limits:
            if password[limit-1] == letter:
                letter_used_counter += 1
        
        if letter_used_counter == 1:
            valid_passwords += 1
    
    return valid_passwords

print("Part 1: ", solve_part_1(parse_input_file("02/input.txt")))
print("Part 2: ", solve_part_2(parse_input_file("02/input.txt")))
