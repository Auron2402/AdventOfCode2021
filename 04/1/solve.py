class Bingofield:
    def __init__(self, number):
        self.number = int(number)
        self.drawn = False

    def draw(self):
        self.drawn = True


class Bingoboard:
    def __init__(self):
        self.layout = [[Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1)],
                       [Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1)],
                       [Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1)],
                       [Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1)],
                       [Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1), Bingofield(-1)]]

    def __getitem__(self, tup):
        x, y = tup
        return self.layout[x][y]

    def check_all_lines(self):
        for i in range(5):
            count = 0
            for y in range(5):
                if self.layout[i][y].drawn:
                    count += 1
            if count == 5:
                return True
        return False

    def check_all_rows(self):
        for i in range(5):
            count = 0
            for y in range(5):
                if self.layout[y][i].drawn:
                    count += 1
            if count == 5:
                return True
        return False

    def check_if_bingo(self):
        if self.check_all_lines():
            return True
        if self.check_all_rows():
            return True
        return False

    def draw_number(self, number):
        for i in range(5):
            for y in range(5):
                if self.layout[i][y].number == number:
                    self.layout[i][y].draw()

    def get_sum_of_all_unmarked_numbers(self):
        sum = 0
        for i in range(5):
            for y in range(5):
                if not self.layout[y][i].drawn:
                    sum += int(self.layout[y][i].number)
        return sum


def create_bingo_boards(bingoboardnumbers):
    allbingoboards = []
    boardline = 0
    boardcounter = 0
    for line in bingoboardnumbers:
        # skip all empty lines
        if boardline == 5:
            boardline = 0
            continue

        # create new board if needed
        if boardline == 0:
            allbingoboards.append(Bingoboard())
            boardcounter += 1

        # fill board with numbers
        numbers = line.split(" ")
        numbers = ' '.join(numbers).split()  # remove formatation spaces
        numbercounter = 0
        for number in numbers:
            allbingoboards[boardcounter - 1][boardline, numbercounter].number = number
            numbercounter += 1
        boardline += 1
    return allbingoboards


def get_winning_board_and_number(bingoboards, bingonumbers):
    for bingonumber in bingonumbers:
        for bingoboard in bingoboards:
            bingoboard.draw_number(bingonumber)
            if bingoboard.check_if_bingo():
                return bingoboard, bingonumber



def main():
    with open("../input.txt") as f:
        bingonumbers = f.readline().split(",")
        bingoboardnumbers = f.read().splitlines()
        bingoboardnumbers.pop(0)  # remove first empty line

        bingoboards = create_bingo_boards(bingoboardnumbers)
        winning_board, winning_number = get_winning_board_and_number(bingoboards, bingonumbers)
        sum_of_umarked_numbers = winning_board.get_sum_of_all_unmarked_numbers()
        result = int(sum_of_umarked_numbers) * int(winning_number)
        print(f"winning number is: {winning_number}\nresult is: {result}")


if __name__ == '__main__':
    main()
