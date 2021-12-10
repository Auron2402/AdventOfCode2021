import statistics

# translation dicts
counterparts = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def remove_lines_with_syntax_errors(lines):
    # find syntax errors

    syntax_errors = []
    corrupt_lines = []
    lineindex = 0
    for line in lines:
        bracket_stack = []
        temp_syntax_errors = []
        for bracket in line:
            if bracket in counterparts:
                bracket_stack.append(bracket)
            else:
                if bracket == counterparts.get(bracket_stack[-1]):
                    bracket_stack.pop()
                else:
                    syntax_errors.append(bracket)
                    bracket_stack.pop()
                    corrupt_lines.append(lineindex)
        lineindex += 1

    # remove duplicate corrupt lines
    corrupt_lines = list(dict.fromkeys(corrupt_lines))

    # remove lines with syntax error
    new_lines = {}
    j = 0
    for i in range(len(lines)):
        if i not in corrupt_lines:
            new_lines[j] = lines[i]
            j += 1

    return new_lines


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
        lines = f.read().splitlines()

        lines = remove_lines_with_syntax_errors(lines)

        scores = []
        for null, line in lines.items():
            # get missing brackets
            bracket_stack = []
            for bracket in line:
                if bracket in counterparts:
                    bracket_stack.append(bracket)
                else:
                    if bracket == counterparts.get(bracket_stack[-1]):
                        bracket_stack.pop()
            missing_brackets = []
            for i in range(len(bracket_stack)):
                missing_brackets.append(counterparts.get(bracket_stack.pop()))

            # generate score
            score = 0
            for bracket in missing_brackets:
                score = score * 5
                score += score_map.get(bracket)
            scores.append(score)

        # didnt think it would be that easy to get median #justPythonThings
        median = statistics.median(scores)
        print(f"median is {median}")


if __name__ == '__main__':
    main()
