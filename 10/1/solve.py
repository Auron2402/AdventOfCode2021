def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:
        lines = f.read().splitlines()

        # find syntax errors
        counterparts = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">"
        }
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
            lineindex += 1


        print(syntax_errors)

        # generate syntax error score
        score_map = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }
        sum = 0
        for syntax_error in syntax_errors:
            sum += score_map.get(syntax_error)

        print(f"Score: {sum}")








if __name__ == '__main__':
    main()