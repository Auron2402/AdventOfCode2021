import re


class Matrix:

    def __init__(self, w: int, h: int) -> None:
        self.board = [[0 for x in range(w)] for y in range(h)]

    def __getitem__(self, tup):
        x, y = tup
        return self.board[x][y]

    def draw_point(self, x: int, y: int):
        self.board[x][y] += 1

    def draw_line(self, start_x: int, start_y: int, end_x: int, end_y: int, with_diagonals=False):
        if start_x == end_x:
            self.draw_vertical_line(start_x, start_y, end_y)
        elif start_y == end_y:
            self.draw_horizontal_line(start_y, start_x, end_x)
        elif with_diagonals:
            self.draw_diagonal_line(start_x, start_y, end_x, end_y)
        else:
            pass  # dont draw diagonal lines

    def draw_horizontal_line(self, start_y: int, start_x: int, end_x: int):
        if end_x > start_x:
            draw_range = end_x - start_x + 1
            for i in range(draw_range):
                self.draw_point(start_x + i, start_y)
        else:
            draw_range = start_x - end_x + 1
            for i in range(draw_range):
                self.draw_point(start_x - i, start_y)

    def draw_vertical_line(self, start_x: int, start_y: int, end_y: int):
        if end_y > start_y:
            draw_range = end_y - start_y + 1
            for i in range(draw_range):
                self.draw_point(start_x, start_y + i)
        else:
            draw_range = start_y - end_y + 1
            for i in range(draw_range):
                self.draw_point(start_x, start_y - i)

    def print_board(self, x, y):
        for i in range(x):
            print("")
            for j in range(y):
                if self.board[i][j] == 0:
                    print(" ", end='')
                else:
                    print(f"{self.board[i][j]}", end='')

    def draw_diagonal_line(self, start_x, start_y, end_x, end_y):
        if end_x > start_x and end_y > start_y:
            # print("right down")
            size = end_y - start_y + 1
            self.draw_diagonal_right_down(start_x, start_y, size)
        elif end_x > start_x and end_y < start_y:
            # print("right up")
            size = end_x - start_x + 1
            self.draw_diagonal_right_up(start_x, start_y, size)
        elif end_x < start_x and end_y > start_y:
            # print("left down")
            size = end_y - start_y + 1
            self.draw_diagonal_left_down(start_x, start_y, size)
        elif end_x < start_x and end_y < start_y:
            # print("left up")
            size = start_x - end_x + 1
            self.draw_diagonal_left_up(start_x, start_y, size)
        else:
            print("WAT?")

    def draw_diagonal_right_down(self, start_x, start_y, size):
        for i in range(size):
            self.draw_point(start_x + i, start_y + i)

    def draw_diagonal_right_up(self, start_x, start_y, size):
        for i in range(size):
            self.draw_point(start_x + i, start_y - i)

    def draw_diagonal_left_down(self, start_x, start_y, size):
        for i in range(size):
            self.draw_point(start_x - i, start_y + i)

    def draw_diagonal_left_up(self, start_x, start_y, size):
        for i in range(size):
            self.draw_point(start_x - i, start_y - i)


def solve_game(with_diagonals: bool):
    # with open("../example.txt") as f:
    with open("../input.txt") as f:
        # draw all lines into board
        vectors = f.readlines()
        field_height, field_with = 1000, 1000
        field = Matrix(field_with, field_height)
        prog = re.compile(r'(?P<start_x>\d*),(?P<start_y>\d*) -> (?P<end_x>\d*),(?P<end_y>\d*)')
        for line in vectors:
            pattern = prog.match(line)
            start_x = int(pattern.group("start_x"))
            start_y = int(pattern.group("start_y"))
            end_x = int(pattern.group("end_x"))
            end_y = int(pattern.group("end_y"))
            field.draw_line(start_x, start_y, end_x, end_y, with_diagonals)

        # check dangerous areas and add up
        count = 0
        for x in range(field_with):
            for y in range(field_height):
                if field[x, y] > 1:
                    count += 1

        print(f"count: {count}\n")


def main():
    print("Part 1 (without diagonals): ")
    solve_game(False)
    print("Part 2 (with diagonals):")
    solve_game(True)
    # field.print_board(field_with, field_height)


if __name__ == '__main__':
    main()
