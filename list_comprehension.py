def main(args: list[str]) -> int:
    cubes: list[int] = [(x,x**3) for x in range(10)]
    print(cubes)

    # Tuple for constants
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    # New things:
    # 1. A literal tuple containing a single item takes a comma after the item
    # 2. Tuple from list (most commonly comprehension): pass to tuple()       
    ranks = ('Ace',) + tuple([str(x) for x in range(2, 10)]) \
                + ('Jack', 'Queen', 'King')
    print(suits)
    print(ranks)
    print()
    print(tuple([f"{rank} of {suit}" for suit in suits for rank in ranks]))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
