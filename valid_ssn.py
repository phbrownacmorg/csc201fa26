def valid_ssn(ssn: str) -> bool:
    # Returns a bool indicating with the given SSN is valid.
    # The SSN can be entered with or without hyphens
    valid: bool = len(ssn) == 9 or len(ssn) == 11

    # 11-character string: hyphens in locations 3 and 6?
    if valid and len(ssn) == 11:
        valid = ssn[3] == '-' and ssn[6] == '-'
        ssn = ssn[1:3] + ssn[4:6] + ssn[-4:] # Remove the hyphens

    # Should now be just a 9-digit string
    valid = valid and ssn.isascii() and ssn.isdigit()

    # First three digits no greater than 773
    valid = valid and ssn[:3] <= '773'

    # First three digits are not 000 or 666
    valid = valid and ssn[:3] not in ['000', '666']

    # Fourth and fifth digits are not '00',
    # and the last four are not '0000'
    valid = valid and ssn[4:6] != '00' and ssn[-4:] != '0000'

    # Not '123-45-6789'
    valid = valid and ssn != '123456789'
    
    return valid

def main(args: list[str]) -> int:
    ssn: str = input('Please enter a Social Security number: ').strip()
    print(ssn, 'is', end=' ')
    if not valid_ssn(ssn):
        print('NOT', end=' ')
    print('a valid Social Security number')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
