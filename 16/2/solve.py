import binascii
import math
import re

# dont want to pull binary through every method so i made it global
binary = ""
current_depth = 0
version_sum = 0

expr = ""


# ---------- EVAL HELPERS
def my_sum(*args):
    return math.fsum(args)


def my_min(*args):
    return min(args)


def my_max(*args):
    return max(args)


def my_mul(*args):
    return math.prod(args)


def my_gt(first, second):
    if first > second:
        return 1
    return 0


def my_lt(first, second):
    if first < second:
        return 1
    return 0


def my_eq(first, second):
    if first == second:
        return 1
    return 0


# --------- REAL CODE
def binary_is_done():
    global binary
    if binary is None:
        return True
    else:
        if binary == "":
            return True
        else:
            if int(binary) == 0:
                return True
    return False


def get_literal_value_of_bin():
    literal = ""
    count = 0
    while True:
        count += 1
        bits = pop_bits_from_bin(5)
        literal += bits[1:]
        if bits[0] == "0":
            break
    value = int(literal, 2)
    return value, count * 5


def pop_bits_from_bin(count: int):
    ret_str = ""
    global binary

    # pop dem bits
    for i in range(count):
        ret_str += binary[i]
    binary = binary[count:]
    return ret_str


def get_packets_by_bit_len(length_in_bits):
    global expr
    working_bits = length_in_bits
    while working_bits > 0:
        poped_bits = extract_package()
        working_bits -= poped_bits
        expr += ", "
    expr = expr[:-2]


def get_packets_by_num(num_of_sub_packets):
    global expr
    poped_bits = 0
    for i in range(num_of_sub_packets):
        curr_poped = extract_package()
        poped_bits += curr_poped
        expr += ", "
    expr = expr[:-2]
    return poped_bits


def extract_package():
    # go deeper
    global current_depth, version_sum, expr
    current_depth += 1

    poped_bits = 6
    # get header
    header_version = int(pop_bits_from_bin(3), 2)
    header_type = int(pop_bits_from_bin(3), 2)
    version_sum += header_version
    if header_type == 4:
        value, curr_poped = get_literal_value_of_bin()
        poped_bits += curr_poped
        depth_formation = " - " * current_depth
        print(f"{depth_formation}{value}")
        expr += str(value)
    else:
        # add expr
        if header_type == 0:
            expr += "my_sum("
        elif header_type == 1:
            expr += "my_mul("
        elif header_type == 2:
            expr += "my_min("
        elif header_type == 3:
            expr += "my_max("
        elif header_type == 5:
            expr += "my_gt("
        elif header_type == 6:
            expr += "my_lt("
        elif header_type == 7:
            expr += "my_eq("
        else:
            expr += "("
        # print("BIN: " + binary)
        length_type_id = pop_bits_from_bin(1)
        poped_bits += 1
        if length_type_id == "0":
            # next 15 bits say total length
            length_in_bits = int(pop_bits_from_bin(15), 2)
            poped_bits += 15
            print(" - " * current_depth + "SUB_LEN_IN")
            get_packets_by_bit_len(length_in_bits)
            poped_bits += length_in_bits
            print(" - " * current_depth + "SUB_LEN_OUT")
        elif length_type_id == "1":
            # next 11 bits say number of packets
            num_of_sub_packets = int(pop_bits_from_bin(11), 2)
            poped_bits += 11
            print(" - " * current_depth + "SUB_NUM_IN")
            curr_poped = get_packets_by_num(num_of_sub_packets)
            poped_bits += curr_poped
            print(" - " * current_depth + "SUB_NUM_OUT")
        else:
            print("This should not happen, packet is 1 or 0!")
        expr += ")"
    # go back out
    current_depth -= 1
    return poped_bits


def run_for_line(line):
    global binary, current_depth, expr
    expr = ""
    # convert hex_str to binary
    num_of_bits = len(line) * 4
    binary = bin(int(line, 16))[2:].zfill(num_of_bits)
    print(binary)

    while not binary_is_done():
        extract_package()
    print(f"VERSION SUM: {version_sum}")
    print(expr)
    # I DIDNT EVEN NEED TO DO THIS! I HAD A ERROR IN MY HEADERTYPE!
    # constant_folding()
    print(eval(expr))


def fold_sum():
    global expr
    search = re.search(r"my_sum\((\d*(?:, *\d*)*)\)", expr)
    if search is not None:
        sum = 0
        numbers = search.group(1).split(", ")
        for number in numbers:
            sum += int(number)
        expr = expr.replace(search.group(0), str(sum))
        return True
    return False


def fold_mul():
    global expr
    search = re.search(r"my_mul\((\d*(?:, *\d*)*)\)", expr)
    if search is not None:
        sum = 1
        numbers = search.group(1).split(", ")
        for number in numbers:
            sum *= int(number)
        expr = expr.replace(search.group(0), str(sum))
        return True
    return False


def fold_bracket():
    global expr
    search = re.search(r"\W(\((\d*(?:, *\d*)*)\))", expr)
    if search is not None:
        if search.group(0)[0] == " ":
            expr = expr.replace(search.group(1), " " + search.group(2))
        else:
            expr = expr.replace(search.group(1), search.group(2))
        return True
    return False


def constant_folding():
    # WHY DO I NEED TO IMPLEMENT CONSTANT FOLDING FROM COMPILERS SO I DONT RUN OUT OF MEMORY? COMMON!
    # EDIT: I DIDNT EVEN NEED TO DO THIS, I HATE MYSELF
    still_folding = True
    while still_folding:
        bracket_folding = fold_bracket()
        print("- ( - " + expr)
        sum_folding = fold_sum()
        print("- + - " + expr)
        mul_folding = fold_mul()
        print("- * - " + expr)
        if not (sum_folding or mul_folding or bracket_folding):
            still_folding = False
    print(expr)


def main():
    with open("../input.txt") as f:
        # with open("../example4.txt") as f:
        line = f.readline().strip()
        run_for_line(line)


def test():
    lines = [
        "C200B40A82",
        "04005AC33890",
        "880086C3E88112",
        "CE00C43D881120",
        "D8005AC2A8F0",
        "F600BC2D8F",
        "9C005AC2F8F0",
        "9C0141080250320F1802104A08",
    ]

    for line in lines:
        run_for_line(line)


if __name__ == '__main__':
    main()
    # test()
