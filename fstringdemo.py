def print_phone(number: str) -> None:
    areacode = number[:3]   # First three digits
    exchange = number[3:6]  # Next three digits
    line = number[6:]       # Last four digits
    
    print(f'{areacode}-{exchange}-{line}') # Standard, with dashes
    print(f'{areacode}.{exchange}.{line}') # Converse, with dots
    print(f'({areacode}) {exchange}-{line}') # Historic, area code parenthesized
    print(f'+1 {areacode}-{exchange}-{line}') # With country code
    print()

def print_ssn_zip(ssn: str) -> None:
    print(f'{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}') # SSN
    print(f'{ssn[:5]}') # Zip code
    print(f'{ssn[:5]}-{ssn[5:]}') # Zip+4
    print()

def print_date(day: int, month: int, year: int) -> None:
    print(f'{month}/{day}/{year}') # American m/d/y
    print(f'{month}/{day}/{year % 100}') # Short American m/d/y (2-digit year)
    print(f'{day}/{month}/{year}') # British d/m/y
    print(f'{day}/{month}/{year % 100}') # Short British d/m/y (2-digit year)
    print(f'{day}.{month}.{year}') # European d.m.y
    print(f'{day}.{month}.{year % 100}') # Short European d.m.y (2-digit year)
    print(f'{year}-{month:02}-{day:02}') # ISO 8601 yyyy-mm-dd    

def main(args: list[str]) -> int:
    print_phone('8648675309')
    print_ssn_zip('123456789')
    print_date(3, 1, 2026)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
