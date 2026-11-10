import random

def game_state(a_score: int, b_score: int, a_serves: bool) -> str:
    serving_side: str = 'A'
    if not a_serves:
        serving_side = 'B'
    return f'Score: A: {a_score} B: {b_score}  {serving_side} is serving'

def server_wins(p_win: float) -> bool:
    """Takes a probability P_WIN that the serving side wins a volley.
    Returns True if the serving side wins and False if not."""
    return (random.random() < p_win)

def game_over(a_score: int, b_score: int, winning_score) -> bool:   
    return max(a_score, b_score) >= winning_score and \
           abs(a_score - b_score) >= 2

def sim_pt_rally(a_score: int, b_score: int, a_serves: bool, p_server: float) \
    -> tuple[int, int, bool]:
    server_won: bool = server_wins(p_server)
    if server_won:
        if a_serves:
            a_score += 1
        else:
            b_score += 1
    else:
        if a_serves:
            b_score += 1
        else:
            a_score += 1
        a_serves = not a_serves # Serving side lost, switch the serve
    return a_score, b_score, a_serves

def sim_pt_sideout(a_score: int, b_score: int, a_serves: bool, p_server: float) \
    -> tuple[int, int, bool]:
    server_won: bool = server_wins(p_server)
    if not server_won:
        a_serves = not a_serves # Serving side lost, switch the serve
    elif a_serves:
        a_score += 1
    else: # not server_won and not a_serves
        b_score += 1
    return a_score, b_score, a_serves


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
    
    while not game_over(a_score, b_score, winning_score):
        # Simulate a point
        if a_serves:
            p = pA
        else:
            p = pB
        a_score, b_score, a_serves = sim_pt_rally(a_score, b_score, a_serves, p)
        print(game_state(a_score, b_score, a_serves))
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

    while not game_over(a_score, b_score, winning_score):
        # Simulate a point
        if a_serves:
            p = pA
        else:
            p = pB
        a_score, b_score, a_serves = \
                 sim_pt_sideout(a_score, b_score, a_serves, p)
        print(game_state(a_score, b_score, a_serves))
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
