import random

def print_game_state(a_score: int, b_score: int, a_serves: bool) -> None:
    serving_side: str = 'A'
    if not a_serves:
        serving_side = 'B'
    print(f'Score: A: {a_score} B: {b_score}  {serving_side} is serving')

def rallyAWon(pA: float, pB: float) -> bool:
    """Takes a probability PA that team A wins when they serve and a
        probability PB that team B wins when they serve.  Simulates a
        volleyball game using rally scoring, and returns True if
        team A won the game or False if team B won the game."""
    # Starts out 0-0.
    a_score: int = 0
    b_score: int = 0
    a_serves: bool = (random.random() < 0.5) # Simulates a coin flip
    winning_score: int = 25
    
    while max(a_score, b_score) < winning_score or abs(a_score - b_score) < 2:
        # Simulate a point
        if a_serves:
            a_won_point: bool = (random.random() < pA)
            if a_won_point:
                a_score += 1
            else:
                b_score += 1
                a_serves = False
        else: # B is serving
            b_won_point: bool = (random.random() < pB)
            if b_won_point:
                b_score += 1
            else:
                a_score += 1
                a_serves = True
        print_game_state(a_score, b_score, a_serves)
    return a_score > b_score # True if and only if A won

def sideOutAWon(pA: float, pB: float) -> bool:
    """Takes a probability PA that team A wins when they serve and a
        probability PB that team B wins when they serve.  Simulates a
        volleyball game using side-out scoring, and returns True if
        team A won the game or False if team B won the game."""
    # Starts out 0-0.
    a_score: int = 0
    b_score: int = 0
    a_serves: bool = (random.random() < 0.5) # Simulates a coin flip
    winning_score: int = 15

    while max(a_score, b_score) < winning_score or abs(a_score - b_score) < 2:
        # Simulate a point
        if a_serves:
            a_won_point: bool = (random.random() < pA)
            if a_won_point:
                a_score += 1
            else:
                a_serves = False
        else: # B is serving
            b_won_point: bool = (random.random() < pB)
            if b_won_point:
                b_score += 1
            else:
                a_serves = True
        print_game_state(a_score, b_score, a_serves)
    return a_score > b_score # True if and only if A won

def main(args: list[str]) -> int:
    random.seed() # Initialize the random-number generator.  Supplying
                  #   a seed value makes the simulation repeatable.
    # Constants:
    pA: float = 0.56 # Probability that team A wins if they serve
    pB: float = 0.5604 # Probability that team B wins if they serve

    if rallyAWon(pA, pB):
        print('Team A won.')
    else:
        print('Team B won.')
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
