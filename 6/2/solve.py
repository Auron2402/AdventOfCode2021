import numpy as np


# --------------- Part 2 is part 1 with bigger number so needs optimisation
def main():
    with open("../input.txt") as f:
        numbers = np.loadtxt(f, delimiter=",")
        numbers = numbers.tolist()

        # sort fishes into day-buckets
        fishbuckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for fish in numbers:
            fishbuckets[int(fish)] += 1

        print(f"Day 0: {fishbuckets}")

        days = 256
        for day in range(days):
            # breeding time
            fishbuckets[9] = fishbuckets[0]

            # pass a day
            for i in range(10):
                if i == 0:
                    fishbuckets[7] = fishbuckets[7] + fishbuckets[0]
                fishbuckets[i - 1] = fishbuckets[i]

            # printing time
            result = fishbuckets[0] + fishbuckets[1] + fishbuckets[2] + fishbuckets[3] + fishbuckets[4] + fishbuckets[
                5] + fishbuckets[6] + fishbuckets[7] + fishbuckets[8]
            print(f"Day {day + 1}: {fishbuckets} = {result}")


if __name__ == '__main__':
    main()
