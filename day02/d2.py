def points_per_game_for_play(opp,play):
    """
    Play    | Opponent  | Player| Points
    Rock    |    A      |   X   |   1
    Paper   |    B      |   Y   |   2
    Scissors|    C      |   Z   |   3
    """
    points = 0
    match play:
        case "X":
            points += 1
        case "Y":
            points += 2
        case "Z":
            points += 3
    if  opp == "A" and play == "X" or \
        opp == "B" and play == "Y" or \
        opp == "C" and play == "Z": # A Draw
        points += 3
    
    elif opp == "A" and play == "Y" or \
         opp == "B" and play == "Z" or \
         opp == "C" and play == "X": # A Win
         points += 6

    return points

def points_per_game_for_game_state(opp,play):
    """
    Play    | Opponent | Points
    Rock    |    A     |   1
    Paper   |    B     |   2
    Scissors|    C     |   3
    ---
    Game State  |Player
    Loss        |  X   
    Draw        |  Y   
    Win         |  Z   
    """
    points = 0
    match play:
        case "X":
            points += 0
        case "Y":
            points += 3
        case "Z":
            points += 6
    if  opp == "A" and play == "Y" or \
        opp == "B" and play == "X" or \
        opp == "C" and play == "Z": # You Play Rock
        points += 1
    
    elif opp == "A" and play == "Z" or \
         opp == "B" and play == "Y" or \
         opp == "C" and play == "X": # You Play Paper
         points += 2
    
    elif opp == "A" and play == "X" or \
         opp == "B" and play == "Z" or \
         opp == "C" and play == "Y": # You Play Scissors
         points += 3

    return points

if __name__ == "__main__":
    
    f = open("day02/d2_input.txt", 'r')
    games = [line.split(" ") for line in f.read().splitlines()]
    f.close()

    # games = [["A","Y"],["B","X"],["C","Z"]]

    total_points_for_play = 0
    total_points_for_game_state = 0
    for game in games:
        total_points_for_play += points_per_game_for_play(game[0],game[1])
        total_points_for_game_state += points_per_game_for_game_state(game[0],game[1])
    
    print("Part 1")
    print(total_points_for_play)
    print("Part 2")
    print(total_points_for_game_state)