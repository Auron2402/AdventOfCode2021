import re
from typing import List

possible_paths = {}
valid_paths = []
ended_paths = 0


def get_next_valid_step(previous_path: List[str]):
    last_step = previous_path[-1]

    # get all possible steps
    possible_steps = possible_paths.get(last_step)

    # filter out steps that are invalid (small caves visited twice)
    valid_steps = []
    for step in possible_steps:
        if not (step in previous_path and step.islower()):
            valid_steps.append(step)

    # filter out steps that you did already
    filtered_steps = []

    for step in valid_steps:
        seq_is_in = False
        for index, value in enumerate(previous_path):
            if value == step:
                if previous_path[index - 1] == last_step:
                    seq_is_in = True
        if not seq_is_in:
            filtered_steps.append(step)

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
    print(f"Found paths: {len(valid_paths)}")
    for path in valid_paths:
        text = ""
        for step in path:
            text += step
            if not step == "end":
                text += ","
        print(text)


def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:
        lines = f.read().splitlines()

        generate_possible_paths(lines)
        print(possible_paths)
        # I still cant recursion
        get_next_valid_step(["start"])
        print_paths_like_example()

if __name__ == '__main__':
    main()
