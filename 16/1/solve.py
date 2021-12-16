import binascii

# dont want to pull binary through every method so i made it global
binary = ""
current_depth = 0
version_sum = 0


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
    return value, count*5


def pop_bits_from_bin(count: int):
    ret_str = ""
    global binary

    # pop dem bits
    for i in range(count):
        ret_str += binary[i]
    binary = binary[count:]
    return ret_str


def get_packets_by_bit_len(length_in_bits):
    working_bits = length_in_bits
    while working_bits > 0:
        poped_bits = extract_package()
        working_bits -= poped_bits
        #print(working_bits)


def get_packets_by_num(num_of_sub_packets):
    poped_bits = 0
    for i in range(num_of_sub_packets):
        curr_poped = extract_package()
        poped_bits += curr_poped
    return poped_bits


def extract_package():
    # go deeper
    global current_depth, version_sum
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
    else:
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
    # go back out
    current_depth -= 1
    return poped_bits


def main():
    with open("../input.txt") as f:
    #with open("../example4.txt") as f:
        line = f.readline().strip()

        global binary, current_depth
        # convert hex_str to binary
        num_of_bits = len(line) * 4
        binary = bin(int(line, 16))[2:].zfill(num_of_bits)
        print(binary)

        while not binary_is_done():
            extract_package()
        print(f"VERSION SUM: {version_sum}")


if __name__ == '__main__':
    main()