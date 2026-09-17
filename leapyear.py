def is_leapyear(year: int) -> bool:
    # Julian rule
    is_leap: bool = ((year % 4) == 0) # Correct 99.25% of the time
    # Gregorian correction
    if is_leap:
        is_leap = ((year % 100) != 0) or ((year % 400) == 0)
    return is_leap

def main(args: list[str]) -> int:
    # Get a year from the user
    year: int = int(input('Please enter a year: '))
    print(year, 'is', end=' ')
    if not is_leapyear(year):
        print('NOT', end=' ')
    print('a leap year.')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
