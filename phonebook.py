def print_dict(d: dict[Any, Any]) -> None:
    # Iterate over the keys of a dictionary
    for key in d:
        print(str(key) + ':', d[key]) # d[key] returns the value associated with key
    print()

def make_book(names: list[str], numbers: list[str]) -> dict[str, str]:
    # names and numbers have to be the same length
    book: dict[str, str] = {}
    for i in range(len(names)):
        book[names[i]] = numbers[i] # Assign a dictionary entry
    return book

def main(args: list[str]) -> int:
    people = ['Barrera', 'P. Brown', 'Mangum', 'Sorrells']
    numbers = ['596-' + ext for ext in ('9128', '9156', '9127', '9149')]
    phonebook = make_book(people, numbers)
    print_dict(phonebook)

    
    print('Mangum:', phonebook['Mangum']) # Dictionary lookup
    print('Barrera:', phonebook['Barrera'])
    print('P. Brown:', phonebook['P. Brown'])
    print('Sorrells:', phonebook['Sorrells'])
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
