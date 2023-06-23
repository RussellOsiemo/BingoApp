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
def mark_number(matrix, number):
    for row in matrix.bingo_matrix:
        if number in row:
            row[row.index(number)] = -1
    
    for column in range(5):
        for row in range(5):
            if matrix.bingo_matrix[row][column] == number:
                matrix.bingo_matrix[row][column] = -1

# playing_matrix = create_master_matrix()
# print(playing_matrix)

bingo_players = []
for player in range(40):
    player_matrix = Matrix()
    for i in range(5):
        random_bingo_numbers = random.sample(
            range(player_matrix.ranges[i][0], player_matrix.ranges[i][1] + 1), 5
        )
        player_matrix.bingo_matrix[i] = random_bingo_numbers
    bingo_players.append(player_matrix)

while True:
    picked_number = random.choice(playing_matrix)
    for player_matrix in bingo_players:
        mark_number(player_matrix, picked_number)
        full_house = all(number == -1 for row in player_matrix.bingo_matrix for number in row)
        if full_house:
            print("Player achieved full house!")
            print(player_matrix.bingo_matrix)
            exit()
