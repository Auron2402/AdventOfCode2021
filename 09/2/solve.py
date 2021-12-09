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
            above = self.board[y - 1][x]
        else:
            above = 10

        # get below
        below = 11
        if y < self.get_board_height() - 1:
            below = self.board[y + 1][x]
        else:
            below = 10

        # get left
        left = 11
        if x > 0:
            left = self.board[y][x - 1]
        else:
            left = 10

        # get right
        right = 11
        if x < self.get_board_width() - 1:
            right = self.board[y][x + 1]
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

    def get_coords_of_neighbors(self, y, x):
        # get above
        above = 11
        if y > 0:
            above = [y - 1, x]
        else:
            above = [-1, -1]

        # get below
        below = 11
        if y < self.get_board_height() - 1:
            below = [y + 1, x]
        else:
            below = [-1, -1]

        # get left
        left = 11
        if x > 0:
            left = [y, x - 1]
        else:
            left = [-1, -1]

        # get right
        right = 11
        if x < self.get_board_width() - 1:
            right = [y, x + 1]
        else:
            right = [-1, -1]

        return [above, right, below, left]

    def check_if_in_basin(self, y, x):
        if y == -1 or x == -1:
            return False
        elif self.checked[y][x]:
            return False
        elif self.board[y][x] == 9:
            return False
        else:
            self.checked[y][x] = True
            return True

    # i hate recursion, this could probably made much better
    def scan_basin_of(self, y, x):
        # check self
        size = 0
        if self.check_if_in_basin(y, x):
            size += 1
            # get neighbors
            neighbors = self.get_coords_of_neighbors(y, x)
            for neighbor_coords in neighbors:
                # if neighbor not checked
                if not self.checked[neighbor_coords[0]][neighbor_coords[1]]:
                    # scan basin
                    size += self.scan_basin_of(neighbor_coords[0], neighbor_coords[1])
        return size


def get_all_lowpoint_heights(layout: Matrix):
    height = layout.get_board_height()
    width = layout.get_board_width()
    lowpoint_heights = []
    for y in range(height):
        for x in range(width):
            if layout.is_low_point(y, x):
                lowpoint_heights.append(layout.board[y][x])
    return lowpoint_heights


def get_all_lowpoint_coords(layout: Matrix):
    height = layout.get_board_height()
    width = layout.get_board_width()
    lowpoint_x = []
    lowpoint_y = []
    for y in range(height):
        for x in range(width):
            if layout.is_low_point(y, x):
                lowpoint_x.append(x)
                lowpoint_y.append(y)
    return lowpoint_y, lowpoint_x


def scan_all_basins(layout: Matrix):
    ys, xs = get_all_lowpoint_coords(layout)
    basin_sizes = []
    for i in range(len(ys)):
        basin_sizes.append(layout.scan_basin_of(ys[i], xs[i]))
    return basin_sizes


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
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

        # scan basins
        basin_sizes = scan_all_basins(layout)
        sorted_sizes = sorted(basin_sizes)
        biggest_three = sorted_sizes[-3:]
        mul_three = 1
        for number in biggest_three:
            mul_three = mul_three * number
        print(f"{biggest_three[0]} * {biggest_three[1]} * {biggest_three[2]} = {mul_three}")


if __name__ == '__main__':
    main()
