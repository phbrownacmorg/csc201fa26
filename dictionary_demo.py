def print_dict(d: dict[Any, Any]) -> None:
    for key in d:
        print(str(key) + ':')
        for value in d[key]:
            print('\t', value)

def make_deck() -> dict[str, tuple[str]]:
    deck: dict[str, tuple[str]] = {}
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    ranks = ('Ace',) + tuple([str(x) for x in range(2, 10)]) \
                + ('Jack', 'Queen', 'King')
    for suit in suits:
        cards = tuple([f"{rank} of {suit}" for rank in ranks])
        deck[suit] = cards
        print_dict(deck)
        print()
    return deck

def main(args: list[str]) -> int:
    deck = make_deck()
    print('Final result:')
    print_dict(deck)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
