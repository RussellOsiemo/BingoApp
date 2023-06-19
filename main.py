import random
# Bingo board class having a 5x5 matrix that is randomly filled
class Matrix:
    bingo_matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    ranges = [
        (1, 10),
        (11, 20),
        (21, 30),
        (31, 40),
        (41, 50)
    ]

for _ in range(40):
    matrix = Matrix()

    for i in range(5):
        random_bingo_numbers = random.sample(range(matrix.ranges[i][0], matrix.ranges[i][1] + 1), 5)
        matrix.bingo_matrix[i] = random_bingo_numbers

    print(matrix.bingo_matrix)
