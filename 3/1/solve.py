import re

def main():
    with open("../input.txt") as f:
        bitlist = f.readlines()
        # count 1 bits in list
        count = 0
        bitcounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        prog = re.compile(r'(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)(\d)')
        for line in bitlist:
            search = prog.match(line)
            count += 1
            for i in range(12):
                if int(search.group(i+1)) == 1:
                    bitcounter[i] += 1

        # get most common bit for each
        gammavalue = ""
        epsilonvalue = ""
        for i in range(12):
            if count/2 > bitcounter[i]:
                gammavalue += "0"
                epsilonvalue += "1"
            else:
                gammavalue += "1"
                epsilonvalue += "0"

        result = int(gammavalue, 2) * int(epsilonvalue, 2)
        print(f'count: {count} \ngamma: {gammavalue} \nepsilon: {epsilonvalue} \nresult: {result}')


if __name__ == '__main__':
    main()
