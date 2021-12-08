import re


def ssd_input_is_zero(glowies):
    pass


def ssd_input_is_one(glowies):
    if len(glowies) == 2:
        return True
    return False


def ssd_input_is_two(glowies):
    pass


def ssd_input_is_three(glowies):
    pass


def ssd_input_is_four(glowies):
    if len(glowies) == 4:
        return True
    return False


def ssd_input_is_five(glowies):
    pass


def ssd_input_is_six(glowies):
    pass


def ssd_input_is_seven(glowies):
    if len(glowies) == 3:
        return True
    return False


def ssd_input_is_eight(glowies):
    if len(glowies) == 7:
        return True
    return False


def ssd_input_is_nine(glowies):
    pass


def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:

        lines = f.readlines()

        pattern = re.compile(r"(\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) (\S*) \| (\S*) (\S*) (\S*) (\S*)")
        counter = 0

        for line in lines:
            # order inputs
            search = pattern.match(line)
            input_array = [search.group(1), search.group(2), search.group(3), search.group(4), search.group(5),
                           search.group(6), search.group(7), search.group(8), search.group(9), search.group(10)]
            output_array = [search.group(11), search.group(12), search.group(13), search.group(14)]

            # count 1, 4 7 and 8s
            for number in output_array:
                if ssd_input_is_one(number):
                    counter += 1
                elif ssd_input_is_four(number):
                    counter += 1
                elif ssd_input_is_seven(number):
                    counter += 1
                elif ssd_input_is_eight(number):
                    counter += 1
        print(f"Counter: {counter}")


if __name__ == '__main__':
    main()
