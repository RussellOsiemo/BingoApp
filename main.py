import random
# Bingo Card class
class Matrix:
    # instanciate a 5x5 matrix
    bingo_matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
# ranges to be used to populate the rows
    ranges = [
        (1, 10),
        (11, 20),
        (21, 30),
        (31, 40),
        (41, 50)
    ]
# 40 players
for players in range(40):
    matrix = Matrix()
# randomize the bingo card
    for i in range(5):
        random_bingo_numbers = random.sample(range(matrix.ranges[i][0], matrix.ranges[i][1] + 1), 5)
        matrix.bingo_matrix[i] = random_bingo_numbers

    print(matrix.bingo_matrix)
# master Matrix
def create_master_matrix():
    master_matrix = []
    count = 1
    
    for _ in range(5):
        row = []
        for _ in range(10):
            row.append(count)
            count += 1
        master_matrix.append(row)
    
    return master_matrix
playing_matrix = create_master_matrix()
print(playing_matrix)
