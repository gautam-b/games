"""
Monopoly board game simulation.

Steps:
x Simple simulation
x Jail rule for three time double roll and "GO TO JAIL" square
- Incorporate community and chance rules ((https://monopoly.fandom.com/wiki/Community_Chest))
"""

import random
from tqdm import trange
from prob_on_board import draw_prob


ITERATION = 1000_000

# Position of jail square on monopoly board, starting count from 1 at GO square
JAIL = 11


def two_dice_roll():
    double = False
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    value = dice1 + dice2
    if dice1 == dice2:
        double = True
    return value, double


def print_result(counts):
    sum_of_counts = sum(counts)
    print(sum_of_counts)
    print(f"Number of iteration: {ITERATION:,}", end="\n\n")
    print("Position | Frequency (%)")
    print("-" * 26)

    for i, count in enumerate(counts):
        print(f"{i+1:8d} | {(count/sum_of_counts)*100:5.2f}")


def main():
    double_dice_count = 0
    counts = [0] * 40
    current_pos = 1

    for _ in trange(ITERATION):
        dice_value, double = two_dice_roll()
        if double:
            double_dice_count += 1
        else:
            double_dice_count = 0

        if double_dice_count == 3:
            current_pos = JAIL
            counts[current_pos - 1] += 1
            double_dice_count = 0
            continue

        current_pos = current_pos + dice_value

        if current_pos > 40:
            current_pos -= 40

        counts[current_pos - 1] += 1

        # Check for Go to jail square
        if current_pos == 31:
            current_pos = JAIL
            counts[current_pos - 1] += 1
            continue

    return counts


if __name__ == "__main__":
    counts = main()
    print_result(counts)
    sum_of_counts = sum(counts)
    prob = [(num / sum_of_counts) * 100 for num in counts]
    file_name = f"{__file__.split('.')[0]}.jpg"
    draw_prob(prob, file_name=file_name)
