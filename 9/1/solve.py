class Matrix:

    def __init__(self, w: int, h: int) -> None:
        self.board = [[0 for x in range(w)] for y in range(h)]
        self.checked = [[0 for x in range(w)] for y in range(h)]

    def __getitem__(self, tup):
        y, x = tup
        return self.board[y][x]

    def get_board_height(self):
        return len(self.board)

    def get_board_width(self):
        return len(self.board[0])

    def get_height_of_neighbors(self, y, x):
        # get above
        above = 11
        if y > 0:
            above = self.board[y-1][x]
        else:
            above = 10

        # get below
        below = 11
        if y < self.get_board_height() - 1:
            below = self.board[y+1][x]
        else:
            below = 10

        # get left
        left = 11
        if x > 0:
            left = self.board[y][x-1]
        else:
            left = 10

        # get right
        right = 11
        if x < self.get_board_width() - 1:
            right = self.board[y][x+1]
        else:
            right = 10

        return [above, right, below, left]

    def is_low_point(self, y, x):
        neighbors = self.get_height_of_neighbors(y, x)
        is_low_point = True
        own_height = self.board[y][x]
        for height in neighbors:
            if height <= own_height:
                is_low_point = False
        return is_low_point


def get_all_lowpoints(layout: Matrix):
    height = layout.get_board_height()
    width = layout.get_board_width()
    lowpoint_heights = []
    for y in range(height):
        for x in range(width):
            if layout.is_low_point(y, x):
                lowpoint_heights.append(layout.board[y][x])
    return lowpoint_heights


def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:
        lines = f.read().splitlines()

        # create board
        width = len(lines[0])
        height = len(lines)
        layout = Matrix(width, height)

        # fill board
        y = 0
        for line in lines:
            x = 0
            for number in line:
                layout.board[y][x] = int(number)
                x += 1
            y += 1

        lowpoint_heights = get_all_lowpoints(layout)
        for i in range(len(lowpoint_heights)):
            lowpoint_heights[i] += 1

        sum = 0
        for height in lowpoint_heights:
            sum += height

        print(f"Sum: {sum}")





if __name__ == '__main__':
    main()