import re
from collections import Counter

working_map = {}


def inc_in_map(pair, map=None, value=1):
    if map is None:
        global working_map
        map = working_map
    if map.get(pair) is None:
        map[pair] = value
    else:
        map[pair] += value


def dec_in_map(pair, map=None, value=1):
    if map is None:
        global working_map
        map = working_map
    prev_value = map.get(pair)
    if prev_value - value == 0:
        map.pop(pair)
    else:
        map[pair] -= value


def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:
        lines = f.read().splitlines()

        # generate map
        pattern_map = {}
        pattern = re.compile(r"(\S\S) -> (\S)")
        for line in lines:
            search = pattern.match(line)
            if search is not None:
                pattern_map[search.group(1)] = search.group(2)

        # generate map insted of string
        f.seek(0)
        working_string = f.readline().strip()
        for i in range(len(working_string) - 1):
            pair = working_string[i] + working_string[i + 1]
            inc_in_map(pair)

        global working_map

        # step it up
        max_steps = 40
        for i in range(max_steps):
            # copy map
            new_working_map = working_map.copy()
            for item in working_map.items():
                # work through map
                value = item[1]
                pair = item[0]
                converted_to = pattern_map.get(pair)
                pair_one = pair[0] + converted_to
                pair_two = converted_to + pair[1]

                dec_in_map(pair, new_working_map, value)
                inc_in_map(pair_one, new_working_map, value)
                inc_in_map(pair_two, new_working_map, value)

            # copy back so the size of the map doesnt change while iterating
            working_map = new_working_map

        # count it
        counter_map = {}
        for item in working_map.items():
            pair = item[0]
            value = item[1]
            inc_in_map(pair[0], counter_map, value)
            inc_in_map(pair[1], counter_map, value)

        # I feel bad doing this but it works so why not
        # The counter class has the same layout as my counter_map, so overwriting "self" of the Counter class with my counter_map
        sorted_map = Counter.most_common(counter_map)

        # Somewhere in this code above is a error
        # The number is always double the size it should be +/- 1
        # So I just add one if its uneven and divide by 2 to get the result
        highest = sorted_map[0][1]
        highest_letter = sorted_map[0][0]
        lowest = sorted_map[len(sorted_map)-1][1]
        lowest_letter = sorted_map[len(sorted_map)-1][0]

        if not highest % 2 == 0:
            highest += 1
        if not lowest % 2 == 0:
            lowest += 1

        correct_highest = highest / 2
        correct_lowest = lowest / 2
        result = correct_highest - correct_lowest
        # Once again, I'm Sorry, but if it works IT AINT STUPID!
        print(f"({highest_letter} {correct_highest} - ({lowest_letter}) {correct_lowest} = {result}")


if __name__ == '__main__':
    main()
