import re


def ssd_input_is_zero(glowies: str, d: str):
    if len(glowies) == 6 and d not in glowies:
        return True
    return False


def ssd_input_is_one(glowies):
    if len(glowies) == 2:
        return True
    return False


def ssd_input_is_two(glowies: str, f: str):
    if len(glowies) == 5 and f not in glowies:
        return True
    return False


def ssd_input_is_three(glowies, c, f):
    if len(glowies) == 5 and c in glowies and f in glowies:
        return True
    return False


def ssd_input_is_four(glowies):
    if len(glowies) == 4:
        return True
    return False


def ssd_input_is_five(glowies, c):
    if len(glowies) == 5 and c not in glowies:
        return True
    return False


def ssd_input_is_six(glowies, c):
    if len(glowies) == 6 and c not in glowies:
        return True
    return False


def ssd_input_is_seven(glowies):
    if len(glowies) == 3:
        return True
    return False


def ssd_input_is_eight(glowies):
    if len(glowies) == 7:
        return True
    return False


def ssd_input_is_nine(glowies, e):
    if len(glowies) == 6 and e not in glowies:
        return True
    return False


def determine_ssd_six(inputarray: list, one: str):
    for glowies in inputarray:
        if len(glowies) == 6:
            for letter in one:
                if not letter in glowies:
                    return glowies
    print("we got a problem in sector six")


def determine_ssd_a(seven: str, one: str):
    seven_return = seven
    for letter in one:
        seven_return = seven_return.replace(letter, "")
    return seven_return


def determine_ssd_b(d_or_e: str, d_or_b: str):
    b = d_or_b
    for letter in d_or_e:
        b = b.replace(letter, "")
    return b


def determine_ssd_c(one: str, six: str):
    one_return = one
    for letter in six:
        one_return = one_return.replace(letter, "")
    return one_return


def determine_ssd_d(d_or_b: str, b: str):
    return d_or_b.replace(b, "")


def determine_ssd_e(d_or_e: str, d: str):
    return d_or_e.replace(d, "")


def determine_ssd_f(one: str, c: str):
    return one.replace(c, "")


def determine_ssd_g(eight, a, b, c, d, e, f):
    eight_return = eight
    eight_return = eight_return.replace(a, "")
    eight_return = eight_return.replace(b, "")
    eight_return = eight_return.replace(c, "")
    eight_return = eight_return.replace(d, "")
    eight_return = eight_return.replace(e, "")
    eight_return = eight_return.replace(f, "")
    return eight_return


def determine_ssd_d_or_e(input_array: list, eight: str, six: str):
    de = ""
    for glowies in input_array:
        if len(glowies) == 6 and not glowies == six:
            eight_edit = eight
            for letter in glowies:
                eight_edit = eight_edit.replace(letter, "")
            de += eight_edit
    return de


def determine_ssd_d_or_b(four: str, one: str):
    four_return = four
    for letter in one:
        four_return = four_return.replace(letter, "")
    return four_return


def find_out_wiring(input_array):
    # save what we already know from part one
    one = "XXX"
    four = "XXX"
    seven = "XXX"
    eight = "XXX"
    for text in input_array:
        if ssd_input_is_one(text):
            one = text
        if ssd_input_is_four(text):
            four = text
        if ssd_input_is_seven(text):
            seven = text
        if ssd_input_is_eight(text):
            eight = text

    # try to find more numbers
    six = determine_ssd_six(input_array, one)

    # find out wiring
    a = determine_ssd_a(seven, one)
    c = determine_ssd_c(one, six)
    f = determine_ssd_f(one, c)
    d_or_e = determine_ssd_d_or_e(input_array, eight, six)
    d_or_b = determine_ssd_d_or_b(four, one)
    b = determine_ssd_b(d_or_e, d_or_b)
    d = determine_ssd_d(d_or_b, b)
    e = determine_ssd_e(d_or_e, d)
    g = determine_ssd_g(eight, a, b, c, d, e, f)
    wiring = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g}
    return wiring


def find_out_number(output_array: list, wiring: dict):
    number = ""
    for glowies in output_array:
        if ssd_input_is_zero(glowies, wiring["d"]):
            number += "0"
        elif ssd_input_is_one(glowies):
            number += "1"
        elif ssd_input_is_two(glowies, wiring["f"]):
            number += "2"
        elif ssd_input_is_three(glowies, wiring["c"], wiring["f"]):
            number += "3"
        elif ssd_input_is_four(glowies):
            number += "4"
        elif ssd_input_is_five(glowies, wiring["c"]):
            number += "5"
        elif ssd_input_is_six(glowies, wiring["c"]):
            number += "6"
        elif ssd_input_is_seven(glowies):
            number += "7"
        elif ssd_input_is_eight(glowies):
            number += "8"
        elif ssd_input_is_nine(glowies, wiring["e"]):
            number += "9"
        else:
            print("Beim herausfinden der nummern läuft was falsch")
    return number


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:

        lines = f.readlines()

        pattern = re.compile(r"(\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) \| (\S*) (\S*) (\S*) (\S*)")
        counter = 0

        result = 0
        for line in lines:
            # order inputs
            search = pattern.match(line)
            input_array = [search.group(1), search.group(2), search.group(3), search.group(4), search.group(5),
                           search.group(6), search.group(7), search.group(8), search.group(9), search.group(10)]
            output_array = [search.group(11), search.group(12), search.group(13), search.group(14)]

            wiring = find_out_wiring(input_array)
            number = find_out_number(output_array, wiring)
            result += int(number)
            print(wiring)
            print(number)

        print(f"Result: {result}")


if __name__ == '__main__':
    main()
