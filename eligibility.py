def eligibleHR(age: int, cit: int) -> bool:
    """Returns True iff AGE and CIT meet the Constitutional requirements
    for serving in the U.S. House of Representatives."""
    if age < 0:
        raise ValueError('Age cannot be negative.')
    elif age < cit:
        raise ValueError('Years of citizenship cannot be greater than age.')
    return (age >= 25)

def eligibleSenate(age: int, cit: int) -> bool:
    """Returns True iff AGE and CIT meet the Constitutional requirements
    for serving in the U.S. Senate."""
    return False # Stub.  Replace with working code.

def main(args: list[str]) -> int:
    try:
        age = int(input("Please enter a person's age: "))
        cit = int(input("How many years has this person been a U.S. citizen? "))
    except ValueError:
        print('Age and length of citizenship must be positive whole numbers.')
    else:
        try:
            house_OK = eligibleHR(age, cit)
            senate_OK = eligibleSenate(age, cit)
        except ValueError as e:
            print(e.msg[0])
        else:
            print(f'A person {age} years old,', end=' ')
            print(f'who has been a U.S. citizen {cit} years, is:')
            outstr = '\t- '
            if not house_OK:
                outstr += 'NOT'
            outstr += ' eligible to serve in the House'
            print(outstr)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
