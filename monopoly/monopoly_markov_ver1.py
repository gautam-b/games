'''
Monopoly board probability computation using markov chain.

Ver 1: No rules.
'''

import numpy as np

np.set_printoptions(precision=4, threshold=2000, linewidth=140)

two_dice = {2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111, 6: 0.1389, 7: 0.1667,
            8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}

starting_pos = np.array(range(0,40), dtype="int8")

transition_prob = np.zeros((40,40), dtype=float)

for i in starting_pos:
    for k, v in two_dice.items():
        col = k + i
        if col > 39:
            col -= 40
        transition_prob[i, col] = v


print(transition_prob)
print(np.sum(transition_prob, axis=1) / 40)
