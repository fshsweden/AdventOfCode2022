def calc_score(his_move, my_move):

    points = 0

    MYMOVES_SCORE = {
        "X": 1, # ROCK
        "Y": 2, # PAPER
        "Z": 3, # SCISSORS
    }   
    
    points += MYMOVES_SCORE[my_move]

    if (his_move == "A" and my_move == "X") or (his_move == "B" and my_move == "Y") or (his_move == "C" and my_move == "Z"):
        points += 3
    elif his_move == "A": # ROCK
        points += 0 if my_move == "Z" else 6
    elif his_move == 'B': # PAPER
        points += 0 if my_move == "X" else 6
    elif his_move == 'C': # SCISSORS
        points += 0 if my_move == "Y" else 6
    else:
        raise Exception("Invalid move")

    return points

def get_winning_move(his_move):
    if his_move == "A": # ROCK
        return "Y" # PAPER
    elif his_move == 'B': # PAPER
        return "Z" # SCISSORS
    elif his_move == 'C': # SCISSORS
        return "X" # ROCK
    else:
        raise Exception("Invalid move")

def get_losing_move(his_move):
    if his_move == "A": # ROCK
        return "Z" # SCISSORS
    elif his_move == 'B': # PAPER
        return "X" # ROCK
    elif his_move == 'C': # SCISSORS
        return "Y" # PAPER
    else:
        raise Exception("Invalid move")

def calculate_my_move(his_move, command):
    if command == "X": # "Need to lose!"
        return get_losing_move(his_move)
    elif command == "Y": # "Need to draw!"
        return "X" if his_move == "A" else "Y" if his_move == "B" else "Z"
    elif command == "Z": # "Need to win!"
        return get_winning_move(his_move)
    else:
        raise Exception("Invalid command")

def sum_scores(rows):
    scores = []
    for row in rows:
        his_move = row[0]
        command = row[1]

        my_move = calculate_my_move(his_move, command)

        score = calc_score(his_move, my_move)
        scores.append(score)

    return sum(scores)

def test_solve():
    test_rows = [
        ["A","Y"],
        ["B","X"],
        ["C","Z"]
    ]
    print(sum_scores(test_rows))


def solve():
    
    # create an array of arrays
    with open('input-2.txt') as f:
        rows = [row.split() for row in f]

    print(sum_scores(rows))

solve()
