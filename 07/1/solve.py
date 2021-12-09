import numpy as np

def get_min_max_from_list(list):
    # get ranges
    min = 9999999
    max = 0

    for number in list:
        if number > max:
            max = number
        if number < min:
            min = number

    return int(min), int(max)

def main():
    #with open("../example.txt") as f:
    with open("../input.txt") as f:
        numbers = np.loadtxt(f, delimiter=",")
        numbers = numbers.tolist()

        # get range
        min, max = get_min_max_from_list(numbers)

        # setup empty field
        layout = [0 for x in range(max+1)]

        # fill field
        for number in numbers:
            layout[int(number)] += 1

        # move field
        all_on_one_field = False
        fuel_spent = 0
        final_position = 0
        while not all_on_one_field:  # could be while true
            # check from left
            on_left_side = 0
            left_position = 0
            for i in range(max):
                if not layout[i] == 0:
                    on_left_side = layout[i]
                    left_position = i
                    break
            print(f"{left_position} is {on_left_side}")

            # check from right
            on_right_side = 0
            right_position = 0
            for i in range(max, 0, -1):  # IOOB?
                if not layout[i] == 0:
                    on_right_side = layout[i]
                    right_position = i
                    break
            print(f"{right_position} is {on_right_side}")

            # move cost eficient field
            if on_right_side == 0 or on_left_side == 0:
                print("sumting went wrung")
            elif left_position == right_position:
                all_on_one_field = True
                final_position = left_position
                print("found it!")
                break
            else:
                if on_left_side >= on_right_side:
                    layout[right_position - 1] += layout[right_position]
                    fuel_spent += layout[right_position]
                    layout[right_position] = 0
                    print(f"{on_left_side} > {on_right_side}")
                if on_right_side > on_left_side:
                    layout[left_position + 1] += layout[left_position]
                    fuel_spent += layout[left_position]
                    layout[left_position] = 0
                    print(f"{on_left_side} < {on_right_side}")

        print(f"Position: {final_position}\nFuel spent: {fuel_spent}")


if __name__ == '__main__':
    main()
