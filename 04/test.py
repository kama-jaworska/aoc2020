import re

test1 = "#1d2a5c"
test2 = "112233"


def validate_hcl(hcl_value):
    return bool(re.match(r'#[0-9a-f]{6}', hcl_value))


# print(validate_hcl(test1))
# print(validate_hcl(test2))

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

def validate_ecl(ecl_value):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl_value in valid_ecl


def validate_pid(pid_value):
    return bool(re.match(r'[0-9]{9}$', pid_value))