def main(arguments: list[str]) -> int:
    # One-argument version, range(STOP): up to, but not including, STOP
    print('range(10) =', list(range(10)))
    print('range(8) =', list(range(8)))
    print('range(0) =', list(range(0)))
    print('range(-3) =', list(range(-3)))
    print()

    # Two-argument version, range(START, STOP): start at START, and
    #   count up to, but not including, STOP
    print('range(14, 18) =', list(range(14, 18)))
    print('range(5, 9) =', list(range(5, 9)))
    print('range(17, 20) =', list(range(17, 20)))
    print('range(-5, 9) =', list(range(-5, 9)))
    print('range(-9, -5) =', list(range(-9, -5)))
    print('range(5, 4) =', list(range(5, 4))) # STOP <= START; empty sequence
    print()

    # For-loop really does take any sequence, not just from range()
    for args in [[14, 18], [5, 9], [17, 20], [-5, 9], [-9, -5], [5, 4]]:
        print('range(', args[0], ', ', args[1],') = ',
              list(range(args[0], args[1])), sep='')
    print()

    # Three-argument version, range(START, STOP, STEP): start at START,
    #   and count by STEP until the next one would be at or beyond STOP
    print('range(-2, 11, 12) =', list(range(-2, 11, 12)))
    print('range(-2, 11, 5) =', list(range(-2, 11, 5)))
    print('range(-2, 10, 3) =', list(range(-2, 10, 3)))
    print('range(10, 0, -1) =', list(range(10, 0, -1))) # Count down
    # Actual reverse of range(10)
    print('range(9, -1, -1) =', list(range(9, -1, -1))) # Count down
    print('range(9, 15, -1) =', list(range(9, 15, -1))) # Empty sequence
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
