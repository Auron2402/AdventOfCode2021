import heapq


class Matrix:
    def __init__(self, width, height) -> None:
        # create board
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.path_cost = [[-1 for x in range(width)] for y in range(height)]

    def fill_board(self, lines: list):
        width = len(lines[0])
        height = len(lines)

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

    def get_price_for_field(self, coords):
        y = coords[0]
        x = coords[1]
        return self[y, x]

    def get_price_for_path(self, coords):
        y = coords[0]
        x = coords[1]
        return self.path_cost[y][x]

    def print_board(self):
        for y in range(self.get_board_height()):
            text = ""
            for x in range(self.get_board_width()):
                text += str(self[y, x])
            print(text)


def sizeup_board(board: Matrix, multiplier=5):
    width = board.get_board_width() * multiplier
    height = board.get_board_height() * multiplier
    old_width = board.get_board_width()
    old_height = board.get_board_height()

    new_board = Matrix(width, height)
    for i in range(multiplier):
        for j in range(multiplier):
            for y in range(board.get_board_height()):
                for x in range(board.get_board_width()):
                    oldrisk = board.get_price_for_field([y, x])
                    newrisk = ((oldrisk + i + j - 1) % 9) + 1
                    new_board.board[y + i * old_height][x + j * old_width] = newrisk
    return new_board


def get_next_possible_steps(coords, layout: Matrix):
    y = coords[0]
    x = coords[1]
    possibilities = []

    if y > 0:
        possibilities.append([y - 1, x])
    if x > 0:
        possibilities.append([y, x - 1])
    if y < layout.get_board_height() - 1:
        possibilities.append([y + 1, x])
    if x < layout.get_board_width() - 1:
        possibilities.append([y, x + 1])

    return possibilities


def pretty_print_queue(queue):
    for index, paths in queue.items():
        print(f"Price {index} has {len(paths)} to complete --> last coodrinate: {paths[0][-1]}")


def solve_part_two(lines):
    width = len(lines[0])
    height = len(lines)
    layout = Matrix(width, height)
    layout.fill_board(lines)

    layout = sizeup_board(layout, 5)
    layout.print_board()
    find_path(layout)


def solve_part_one(lines):
    width = len(lines[0])
    height = len(lines)
    layout = Matrix(width, height)
    layout.fill_board(lines)
    find_path(layout)


def find_path(layout):
    # finish field is bottom right
    finish = [layout.get_board_height() - 1, layout.get_board_width() - 1]
    queue = []
    # (cost, y, x)
    heapq.heappush(queue, (0, 0, 0))
    seen = []
    max_cost = 99999
    count = 0
    while queue:
        # get lowest path
        cost, y, x = heapq.heappop(queue)

        # status print every 10k?
        count += 1
        if count == 10000:
            print(f"Queue: {len(queue)} --> current: {x} {y} --> cost: {cost}")
            count = 0

        # ignore costly path
        if cost > max_cost:
            continue
        # ignore steps where we were already?
        if not layout.get_price_for_path([y, x]) == -1:
            continue

        # get possible steps
        possible_steps = get_next_possible_steps([y, x], layout)

        # add new paths to queue
        for step in possible_steps:
            nextstep_cost = layout.get_price_for_field(step) + cost

            if layout.get_price_for_path(step) == -1:
                layout.path_cost[y][x] = nextstep_cost
                heapq.heappush(queue, (nextstep_cost, step[0], step[1]))

            if step == finish:
                max_cost = nextstep_cost
                print(f"FOUND SHIT: {nextstep_cost} --> Queue: {len(queue)}")
    print("DONE")


def main():
    with open("../input.txt") as f:
    #with open("../example.txt") as f:
        lines = f.read().splitlines()

        solve_part_one(lines)
        solve_part_two(lines)


if __name__ == '__main__':
    main()
