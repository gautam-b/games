"""Program to simulate Monty Hall Experiment"""

import random
from tqdm import trange


def main():
    num_of_rounds = 1_000_000

    print(f"Starting Montly Hall Simulation with {num_of_rounds:,} rounds.")
    print()

    print("Simulating the case where player do not switch the door")
    win_pct_not_switched = monty_hall_simulation(num_of_rounds, switch=False)
    print(f"When player does not switch the door, his probability to win is {win_pct_not_switched:.4f}%")
    print()

    print("Simulating the case where player switch the door")
    win_pct_switched = monty_hall_simulation(num_of_rounds, switch=True)
    print(f"When player switch the door, his probability to win is {win_pct_switched:.4f}%")


def monty_hall_simulation(num_of_rounds=10_000, switch=False):
    win_count = 0

    for _ in trange(num_of_rounds):
        doors = ["A", "B", "C"]

        # Host choose a door and put the prize behind that door
        host_choice = random.choice(doors)

        # Player choose a door
        player_choice = random.choice(doors)

        # Host opens a door
        while True:
            open_door = random.choice(doors)
            if open_door == host_choice or open_door == player_choice:
                continue
            break

        # Host gives player an option to switch door
        if switch:  # Player choice
            doors.remove(open_door)
            player_choice = random.choice(doors)

        # Host open the remaining two door and player sees if it wins or not
        if player_choice == host_choice:
            win_count += 1

    win_pct = win_count / num_of_rounds

    return win_pct


if __name__ == "__main__":
    main()
