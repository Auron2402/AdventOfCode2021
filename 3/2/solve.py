def determine_oxygen_from_log(bitlist):
    for i in range(12):
        # find most common bit
        maxcount = 0
        bitcount = 0
        for line in bitlist:
            maxcount += 1
            if int(line[i]) == 1:
                bitcount += 1
        # new list with only most common bitsequence
        newlist = []
        if bitcount >= maxcount / 2:
            for line in bitlist:
                if int(line[i]) == 1:
                    newlist.append(line)
        else:
            for line in bitlist:
                if int(line[i]) == 0:
                    newlist.append(line)
        # return if only one sequence left
        bitlist = newlist
        if len(bitlist) == 1:
            print(bitlist)
            return bitlist[0]


def determine_coo_scrubber_from_log(bitlist):
    for i in range(12):
        # find least common bit
        maxcount = 0
        bitcount = 0
        for line in bitlist:
            maxcount += 1
            if int(line[i]) == 1:
                bitcount += 1
        # new list with only least common bitsequence
        newlist = []
        if bitcount >= maxcount / 2:
            for line in bitlist:
                if int(line[i]) == 0:
                    newlist.append(line)
        else:
            for line in bitlist:
                if int(line[i]) == 1:
                    newlist.append(line)
        # return if only one sequence left
        bitlist = newlist
        if len(bitlist) == 1:
            print(bitlist)
            return bitlist[0]


def main():
    with open("../input.txt") as f:
        bitlist = f.read().splitlines()
        oxy = determine_oxygen_from_log(bitlist)
        cos = determine_coo_scrubber_from_log(bitlist)

        result = int(oxy, 2) * int(cos, 2)
        print(f"\nresult: {result}")


if __name__ == '__main__':
    main()
