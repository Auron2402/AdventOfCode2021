import re
from collections import Counter

def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
        lines = f.read().splitlines()

        # generate map
        pattern = re.compile(r"(\S\S) -> (\S)")
        map = {}
        for line in lines:
            search = pattern.match(line)
            if search is not None:
                map[search.group(1)] = search.group(2)


        # step through
        max_steps = 10
        f.seek(0)
        working_string = f.readline().strip()
        for step in range(max_steps):
            new_string = ""
            pair = ""
            for i in range(len(working_string) - 1):  # ioob? -1?
                pair = working_string[i] + working_string[i+1]
                insert = map.get(pair)
                new_string += pair[0]
                new_string += insert
            new_string += pair[1]
            working_string = new_string
            print(f" After step {step + 1}: {working_string}")
        counter = Counter(working_string)
        sorted_counter = counter.most_common()
        result = sorted_counter[0][1] - sorted_counter[len(counter) - 1][1]
        print(result)




if __name__ == '__main__':
    main()
