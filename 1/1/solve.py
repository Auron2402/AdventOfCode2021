def main():
    with open('input.txt') as f:
        lines = f.readlines()
        prev = 99999999999999999999
        count = 0
        for sline in lines:
            line = int(sline)
            if line > prev:
                count += 1
            prev = line
    print(count)


if __name__ == '__main__':
    main()
