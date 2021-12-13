import re
from typing import List
from collections import Counter

possible_paths = {}
valid_paths = []
ended_paths = 0


def get_next_valid_step(previous_path: List[str]):
    last_step = previous_path[-1]

    # get all possible steps
    possible_steps = possible_paths.get(last_step)

    # filter out steps that are invalid (small caves visited twice)
    valid_steps = []
    counter = Counter(previous_path)
    small_cave_visited_twice = False
    for key, value in counter.items():
        if key.islower() and value > 1:
            small_cave_visited_twice = True
    for step in possible_steps:
        # visit start only once
        if step == "start":
            continue
        # if uppercase, just add it
        elif step.isupper():
            valid_steps.append(step)
        # if lower do checks
        else:
            if step in previous_path and small_cave_visited_twice:
                continue
            valid_steps.append(step)

    # here i wasted min one hour to filter out already visited sequences, which i didnt even need to do
    filtered_steps = valid_steps

    if not len(filtered_steps) == 0:
        for step in filtered_steps:
            new_path = previous_path[:]  # Its all references? --> Always has been ## need to do this so its copy
            new_path.append(step)
            if step == "end":
                valid_paths.append(new_path)
            else:
                get_next_valid_step(new_path)


def generate_possible_paths(lines: list):
    pattern = re.compile(r"(\S*)-(\S*)")
    for line in lines:
        search = pattern.match(line)
        path_from = search.group(1)
        path_to = search.group(2)
        if path_from not in possible_paths:
            possible_paths[path_from] = [path_to]
        else:
            possible_paths[path_from].append(path_to)
        if path_to not in possible_paths:
            possible_paths[path_to] = [path_from]
        else:
            possible_paths[path_to].append(path_from)


def print_paths_like_example():
    for path in valid_paths:
        text = ""
        for step in path:
            text += step
            if not step == "end":
                text += ","
        print(text)
    print(f"Found paths: {len(valid_paths)}")


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
        lines = f.read().splitlines()

        generate_possible_paths(lines)
        print(possible_paths)
        # I still cant recursion
        get_next_valid_step(["start"])
        print_paths_like_example()


if __name__ == '__main__':
    main()
