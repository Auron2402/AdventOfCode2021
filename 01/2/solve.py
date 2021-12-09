def main():
    with open('../input.txt') as f:
        lines = f.readlines()
        prev_one = 99999999999999999999
        prev_two = 99999999999999999999
        prev_three = 99999999999999999999
        count = 0
        for sline in lines:
            line = int(sline)
            currslide = line + prev_one + prev_two
            prevslide = prev_one + prev_two + prev_three
            if currslide > prevslide:
                count += 1
            prev_three = prev_two
            prev_two = prev_one
            prev_one = line
    print(count)


if __name__ == '__main__':
    main()
