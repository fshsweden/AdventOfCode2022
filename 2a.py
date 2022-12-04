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

def sum_scores(rows):
    scores = []
    for row in rows:
        his_move = row[0]
        my_best_move = row[1]
        score = calc_score(his_move, my_best_move)
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