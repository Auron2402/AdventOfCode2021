import numpy as np


def main():
    #with open("../example.txt") as f:
    with open("../input.txt") as f:
        numbers = np.loadtxt(f, delimiter=",")
        numbers = numbers.tolist()
        size = len(numbers)
        print(f"Day 0: {size}")

        days = 256
        for day in range(days):
            # pass a day
            index = 0
            for fish in numbers:
                numbers[index] -= 1
                index += 1

            # breeding time
            index = 0
            for fish in numbers:
                if fish == -1:
                    numbers.append(8)
                    numbers[index] = 6
                index += 1

            # printing time
            print(f"Day {day + 1}: {len(numbers)}")
            # print(f"Day {day + 1}: {numbers}")


if __name__ == '__main__':
    main()
