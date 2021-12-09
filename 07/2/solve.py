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
    # with open("../example.txt") as f:
    with open("../input.txt") as f:
        numbers = np.loadtxt(f, delimiter=",")
        numbers = numbers.tolist()

        # get range
        min, max = get_min_max_from_list(numbers)

        # setup empty fields
        layout = [0 for x in range(max + 1)]
        fuelfield = [0 for x in range(max + 1)]
        vanillafield = [0 for x in range(max + 1)]

        # fill fields
        for number in numbers:
            layout[int(number)] += 1
            vanillafield[int(number)] += 1

        # move field
        all_on_one_field = False
        fuel_spent = 0
        final_position = 0
        while not all_on_one_field:  # could be while true
            # -- check fuel from left
            # get onemove fuel
            on_left_side = 0
            left_position = 0
            for i in range(max):
                if not layout[i] == 0:
                    on_left_side = layout[i]
                    left_position = i
                    break
            # print(f"{left_position} is {on_left_side}")

            # get aditional fuel
            aditional_fuel_from_left = 0
            for i in range(0, left_position):
                aditional_fuel_from_left += fuelfield[i]

            # -- check from right
            # get one move fuel
            on_right_side = 0
            right_position = 0
            for i in range(max, 0, -1):  # IOOB?
                if not layout[i] == 0:
                    on_right_side = layout[i]
                    right_position = i
                    break
            # print(f"{right_position} is {on_right_side}")

            # get aditional fuel
            aditional_fuel_from_right = 0
            for i in range(max, right_position, -1):
                aditional_fuel_from_right += fuelfield[i]

            # move cost eficient field
            if on_right_side == 0 or on_left_side == 0:
                print("sumting went wrung")
            elif left_position == right_position:
                all_on_one_field = True
                final_position = left_position
                print("found it!")
                break
            else:
                need_for_left_move = on_left_side + aditional_fuel_from_left
                need_for_right_move = on_right_side + aditional_fuel_from_right
                if need_for_left_move > need_for_right_move:
                    # move field
                    layout[right_position - 1] += layout[right_position]
                    # save fuel spent
                    fuel_spent += need_for_right_move
                    # edit fuel chart
                    for i in range(max, right_position - 1, -1):
                        fuelfield[i] += vanillafield[i]
                    # remove moved
                    layout[right_position] = 0
                    print(f"Move LEFT from {right_position}: {need_for_right_move} fuel")
                elif need_for_right_move >= need_for_left_move:
                    # move field
                    layout[left_position + 1] += layout[left_position]
                    # save fuel spent
                    fuel_spent += need_for_left_move
                    # edit fuel chart
                    for i in range(min, left_position + 1):
                        fuelfield[i] += vanillafield[i]
                    # remove moved
                    layout[left_position] = 0
                    print(f"Move RIGHT from {left_position}: {need_for_left_move} fuel")
                else:
                    print("this should not happen")

        print(f"Position: {final_position}\nFuel spent: {fuel_spent}")


if __name__ == '__main__':
    main()
