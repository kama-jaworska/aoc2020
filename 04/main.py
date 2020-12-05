def parse_input_file(input_file):
    data = open(input_file, "r").read().splitlines()
    return [split_line for split_line in [line.split() for line in data]]


def create_passport_dict(input_file_lines):
    passports = {}
    id = 0

    for line in input_file_lines:
        if id not in passports:
            passports[id] = {}

        if line == []:
            id += 1
            continue

        for item in line:
            key_val = item.split(":")
            passports[id][key_val[0]] = key_val[1]

    return passports


def check_passport_keys_present(passport, required_fields):
    return required_fields.issubset(passport.keys())


def validate_passport_field_values(passport, validation_rules):
    pass


def solve_part_1(passport_registry, required_fields):
    valid_count = 0

    for key in passport_registry.keys():
        passport = passport_registry[key]
        if check_passport_keys_present(passport, required_fields):
            valid_count += 1

    return valid_count


def solve_part_2(passport_registry, required_fields, validation_rules):
    valid_count = 0

    for key in passport_registry.keys():
        passport = passport_registry[key]

        if check_passport_keys_present(passport, required_fields) and validate_passport_field_values(
            passport, validation_rules):
                valid_count += 1

    return valid_count


def main(input_file, fields, validation):
    passport_registry = create_passport_dict(parse_input_file(input_file))

    print("PART 1: ", solve_part_1(passport_registry, fields))
    print("PART 2: ", solve_part_2(passport_registry, fields, validation))


if __name__ == "__main__":
    filename = "input.txt"
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    validation_rules = []

    main(filename, required_fields, validation_rules)