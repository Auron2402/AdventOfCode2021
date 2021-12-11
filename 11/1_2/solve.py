class Matrix:

    def __init__(self, lines: list) -> None:
        # create board
        width = len(lines[0])
        height = len(lines)
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.flashed = [[0 for x in range(width)] for y in range(height)]
        self.flash_number = 0

        # fill board with starting values
        for row in range(height):
            for col in range(width):
                self.board[row][col] = int(lines[row][col])

    def __getitem__(self, tup):
        y, x = tup
        return self.board[y][x]

    def get_board_height(self):
        return len(self.board)

    def get_board_width(self):
        return len(self.board[0])

    def reset_flashed(self):
        # cooldown flashed fishes
        for row in range(self.get_board_height()):
            for col in range(self.get_board_width()):
                if self.board[row][col] > 9:
                    self.board[row][col] = 0

        # reset the flashed matrix and number
        self.flashed = [[0 for x in range(self.get_board_width())] for y in range(self.get_board_height())]
        self.flash_number = 0

    def inc_board_by_(self, number: int):
        for row in range(self.get_board_height()):
            for col in range(self.get_board_width()):
                self.board[row][col] += number

    def inc_coords_by_(self, coords, number: int):
        self.board[coords[0]][coords[1]] += number

    def get_coords_of_flashing(self):
        coord_list = []
        for row in range(self.get_board_height()):
            for col in range(self.get_board_width()):
                if self.board[row][col] < 9 and self.flashed[row][col] == 0:
                    coord_list.append([row, col])

    def set_flashed(self, coords):
        self.flashed[coords[0]][coords[1]] = 1

    def is_flashed(self, coords):
        if self.flashed[coords[0]][coords[1]] == 1:
            return True
        return False

    def get_circle_around(self, coords):
        coord_list = []
        row = coords[0]
        col = coords[1]

        if row > 0:
            # top-mid
            coord_list.append([row - 1, col])
            if col > 0:
                # top-left
                coord_list.append([row - 1, col - 1])
            if col < self.get_board_width() - 1:
                # top right
                coord_list.append([row - 1, col + 1])

        if col > 0:
            # mid-left
            coord_list.append([row, col - 1])
        if col < self.get_board_width() - 1:
            # mid-right
            coord_list.append([row, col + 1])

        if row < self.get_board_height() - 1:
            # bot-mid
            coord_list.append([row + 1, col])
            if col > 0:
                # bot-left
                coord_list.append([row + 1, col - 1])
            if col < self.get_board_width() - 1:
                # bot-right
                coord_list.append([row + 1, col + 1])

        return coord_list

    def flash_coords(self, coords):
        if not self.is_flashed(coords):
            self.set_flashed(coords)
            self.flash_number += 1
            circle_coords = self.get_circle_around(coords)
            for coords in circle_coords:
                self.inc_coords_by_(coords, 1)
                if self.board[coords[0]][coords[1]] > 9:
                    self.flash_coords(coords)


def get_flashes_for_one_step(layout):
    # Phase 1
    layout.inc_board_by_(1)
    # Phase 2
    for row in range(layout.get_board_height()):
        for col in range(layout.get_board_width()):
            if layout.board[row][col] > 9:
                layout.flash_coords([row, col])
    flashes = layout.flash_number
    # Phase 3
    layout.reset_flashed()
    return flashes


def main():
    with open("../input.txt") as f:
        # with open("../example.txt") as f:
        lines = f.read().splitlines()

        layout = Matrix(lines)

        cumulative_flashes = 0
        simulated_steps = 100
        fishcount = layout.get_board_width() * layout.get_board_height()
        steps = 0
        while True:
            flashing = get_flashes_for_one_step(layout)
            cumulative_flashes += flashing
            steps += 1
            # Answer part 1
            if steps == simulated_steps:
                print(f"Flashes after {simulated_steps} steps: {cumulative_flashes}")
            # Answer part 2
            if fishcount == flashing:
                print(f"All Synchronized after {steps} Steps")
                break


if __name__ == '__main__':
    main()
