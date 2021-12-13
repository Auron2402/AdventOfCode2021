import re


class Matrix:
    def __init__(self, width, height) -> None:
        self.board = [[0 for x in range(width)] for y in range(height)]

    def __getitem__(self, tup):
        y, x = tup
        return self.board[y][x]

    def get_board_height(self):
        return len(self.board)

    def get_board_width(self):
        return len(self.board[0])

    def pretty_print(self):
        for row in self.board:
            text = ""
            for col in row:
                if col > 0:
                    text += "#"
                else:
                    text += " "
            print(text)

    def count_dots(self):
        count = 0
        for row in self.board:
            for col in row:
                if col > 0:
                    count += 1
        return count

    def copy_old_board(self, new_board, delta_x=0, delta_y=0):
        # copy part of old board
        for i in range(new_board.get_board_height()):
            for y in range(new_board.get_board_width()):
                new_board.board[i + delta_y][y + delta_x] = self.board[i][y]
        return new_board

    def fold_vertical_at(self, fold_line):
        # get size of new board
        new_height = fold_line
        delta_y = 0
        if (self.get_board_height() / 2) < fold_line:
            new_height = self.get_board_height() - fold_line - 1
            delta_y = new_height - fold_line - 1
        new_width = self.get_board_width()

        # copy old board
        new_board = Matrix(new_width, new_height)
        new_board = self.copy_old_board(new_board, delta_y=delta_y)

        # fold up
        for i in range(fold_line):
            for y in range(new_width):
                new_board.board[new_height - i - 1][y] += self.board[fold_line + i + 1][y]

        return new_board

    def fold_horizontal_at(self, fold_line: int):
        # get size of new board
        new_width = fold_line
        delta_x = 0
        if (self.get_board_width() / 2) < fold_line:
            new_width = self.get_board_width() - fold_line - 1
            delta_x = new_width - fold_line - 1
        new_height = self.get_board_height()

        # copy old board
        new_board = Matrix(new_width, new_height)
        new_board = self.copy_old_board(new_board, delta_x=delta_x)

        # fold left
        for i in range(new_height):
            for y in range(fold_line):
                new_board.board[i][new_width - y - 1] += self.board[i][fold_line + y + 1]

        return new_board


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
        lines = f.read().splitlines()
        pattern = re.compile(r"(\d*),(\d*)")

        # create empty board
        max_x = 0
        max_y = 0
        for line in lines:
            search = pattern.match(line)
            if search is not None:
                num_one = int(search.group(1))
                num_two = int(search.group(2))
                if num_one > max_x:
                    max_x = num_one
                if num_two > max_y:
                    max_y = num_two
        layout = Matrix(width=max_x + 1, height=max_y + 1)

        # fill board
        for line in lines:
            search = pattern.match(line)
            if search is not None:
                num_one = int(search.group(1))
                num_two = int(search.group(2))
                layout.board[num_two][num_one] = 1

        # get folding
        pattern = re.compile(r"fold along (.)=(\d*)")
        foldcounter = 0
        for line in lines:
            search = pattern.match(line)
            if search is not None:
                if search.group(1) == "x":
                    layout = layout.fold_horizontal_at(int(search.group(2)))
                elif search.group(1) == "y":
                    layout = layout.fold_vertical_at(int(search.group(2)))
                else:
                    print("WAT?")
                foldcounter += 1
            if foldcounter == 1:
                print(f"Number of dots after one fold: {layout.count_dots()}")

        layout.pretty_print()


if __name__ == '__main__':
    main()
