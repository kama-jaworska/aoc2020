import re


def parse_input_file(input_file):
    data = open(input_file, "r").read().splitlines()
    return [split_line for split_line in [line.split() for line in data]]


def create_passport_dict(input_file_lines):
    passports = {}
    passport_id = 0

    for line in input_file_lines:
        if passport_id not in passports:
            passports[passport_id] = {}

        if line == []:
            passport_id += 1
            continue

        for item in line:
            key_val = item.split(":")
            passports[passport_id][key_val[0]] = key_val[1]

    return passports


def check_passport_keys_present(passport, fields):
    return fields.issubset(passport.keys())


def validate_byr(byr_value):
    return 1920 <= int(byr_value) <= 2002


def validate_iyr(iyr_value):
    return 2010 <= int(iyr_value) <= 2020


def validate_eyr(eyr_value):
    return 2020 <= int(eyr_value) <= 2030


def validate_hgt(hgt_value):
    find_num_value = re.match(r'\d+', hgt_value)
    if find_num_value is None:
        return False

    height = int(find_num_value[0])
    unit = hgt_value[-2:]

    if unit == "cm":
        return 150 <= height <= 193
    elif unit == "in":
        return 59 <= height <= 76

    return False


def validate_hcl(hcl_value):
    return bool(re.match(r'#[0-9a-f]{6}', hcl_value))


def validate_ecl(ecl_value):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl_value in valid_ecl


def validate_pid(pid_value):
    return bool(re.match(r'[0-9]{9}$', pid_value))


def validate_passport_field_values(passport):
    byr = validate_byr(passport["byr"])
    iyr = validate_iyr(passport["iyr"])
    eyr = validate_eyr(passport["eyr"])
    hgt = validate_hgt(passport["hgt"])
    hcl = validate_hcl(passport["hcl"])
    ecl = validate_ecl(passport["ecl"])
    pid = validate_pid(passport["pid"])

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        return True
    else:
        return False


def solve_part_1(passport_registry, required_fields):
    valid_count = 0

    for key in passport_registry.keys():
        passport = passport_registry[key]
        if check_passport_keys_present(passport, required_fields):
            valid_count += 1

    return valid_count


def solve_part_2(passport_registry, required_fields):
    valid_count = 0

    for key in passport_registry.keys():
        passport = passport_registry[key]

        if check_passport_keys_present(passport, required_fields) and validate_passport_field_values(passport):
            valid_count += 1

    return valid_count


def main(input_file, fields):
    passport_registry = create_passport_dict(parse_input_file(input_file))

    print("PART 1: ", solve_part_1(passport_registry, fields))
    print("PART 2: ", solve_part_2(passport_registry, fields))


if __name__ == "__main__":
    filename = "input.txt"
    req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    main(filename, req_fields)