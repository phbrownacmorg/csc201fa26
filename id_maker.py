# Program to read a name from the keyboard and generate a Converse-style ID

def make_id(name: str) -> str:

    # Split off the last name first
    nameparts: list[str] = name.split(',')
    lastname = nameparts[0]

    # Remove any unwanted characters from the last name
    unwanted = " '"
    for c in unwanted:
        lastname = lastname.replace(c, '')

    # Now split the remainder into first name, middle, and so on
    nameparts = nameparts[1].strip().split()
    #print(nameparts)
    firstname = nameparts[0]
    middle = ''
    if len(nameparts) > 1: # Person has a middle name
        middle = nameparts[1][0]
    
    return (firstname[0] + middle + lastname + '001').lower()

def main(args: list[str]) -> int:
    name: str = input('Please enter a name, last name first, separated by a comma: ')
    print('The Converse ID for this name would be', make_id(name))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
