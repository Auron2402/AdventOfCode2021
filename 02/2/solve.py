import re

commands = {}


def main():
    with open('../input.txt') as f:
        commandlist = f.readlines()
        prog = re.compile(r'(\S*) (\S)')
        forward = 0
        depth = 0
        aim = 0
        for line in commandlist:
            prog_res = prog.match(line)
            why_is_this_a_group_python = prog_res.group(0)
            command = prog_res.group(1)
            quantity = int(prog_res.group(2))
            if command == "forward":
                forward += quantity
                depth = depth + (aim * quantity)
            if command == "down":
                aim += quantity
            if command == "up":
                aim -= quantity
    result = forward * depth
    print(f"Destination: \nForward = {forward}\nDepth = {depth}\nResult = {result}")


if __name__ == '__main__':
    main()
