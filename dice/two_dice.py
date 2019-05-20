from random import randint
from tqdm import trange

counts = [0] * 13
ITERATION = 100_000

for _ in trange(ITERATION):
    dice_value = randint(1, 6) + randint(1, 6)
    counts[dice_value] += 1

print(f"Number of iteration: {ITERATION:,}", end="\n\n")
print("Dice Total | Frequency (%)")
print("-" * 26)
for i, item in enumerate(counts):
    if i > 1:
        print(f"{i:10d} | {(item/ITERATION)*100:5.2f}")
