def repetition() -> None:
    print('xyzzy' * 3)
    print(5 * 'cat')

def iteration(s: str) -> None:
    # Positions
    for i in range(len(s)):
        print(f"{i:>2}", end=' ')
    print()

    # Iterate over the string
    for c in s:
        print(f'{c:>2}', end=' ')
    print()

    # Iterate over the string using subscripts
    for i in range(len(s)):
        print(f'{s[i]:>2}', end=' ')
    print()
    
    # Iterate over the string using subscripts, counting from the end
    for i in range(-len(s), 0):
        print(f'{s[i]:>2}', end=' ')
    print()
    
    # Iterate over the string using integer expressions for subscripts
    for i in range(5, 2*len(s)+5, 2):
        print(f'{s[(i-5)//2]:>2}', end=' ')
    print()

    # Positions, counting from the end
    for i in range(-len(s), 0):
        print(i, end=' ')
    print()

def slicing(s: str) -> None:
    # Simple slicing
    print(s[3:-3])

    # Slicing with a missing subscript
    for i in range(len(s)):
        print(s[:i], s[i:])

    # Slicing with a step
    for i in range(len(s)):
        print(s[i::2])

def main(args: list[str]) -> int:
    repetition()
    iteration('computer')
    slicing('computer science')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
