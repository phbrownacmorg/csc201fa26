def count(listvar: list[Any], x: Any) -> int:
    total = 0
    for item in listvar:
        if item == x:
            total = total + 1
    return total

def isin(listvar: list[Any], x: Any) -> bool:
    return count(listvar, x) > 0

def index(listvar: list[Any], x: Any) -> int:
    result = -1 # Bogus index value, in order to recognize when the item
                # was not present
    for i in range(len(listvar)):
        if listvar[i] == x:
            result = i
            break # Stop.  We have our answer.
    if result < 0:
        raise ValueError(f"Value '{str(x)}' not found in list.")
    return result

def reverse(listvar: list[Any]) -> None:
    # Has to change the *actual object*, not just the name listvar
    listvar[:] = listvar[-1:-len(listvar) - 1:-1] 

def main(args: list[str]) -> int:
    list1 = list('Hello, world!')
    list2 = list(range(10))

    # Test count
    print(list1)
    print(count(list1, 'Q'), list1.count('Q'))
    print(count(list1, 'H'), list1.count('H'))
    print(count(list1, '!'), list1.count('!'))
    print(count(list1, ','), list1.count(','))
    print(count(list1, 'o'), list1.count('o'))
    print(count(list1, 'l'), list1.count('l'))
    print()

    # Test isin
    print(isin(list1, 'Q'), 'Q' in list1)
    print(isin(list1, 'H'), 'H' in list1)
    print(isin(list1, '!'), '!' in list1)
    print(isin(list1, ','), ',' in list1)
    print(isin(list1, 'o'), 'o' in list1)
    print(isin(list1, 'l'), 'l' in list1)
    print()

    # Test index
    try:
        index(list1, 'Q')
    except ValueError:
        print("'Q' is not present")
    else:
        print('Test failed.')
    #print(index(list1, 'Q'), 'Q' in list1)
    print(index(list1, 'H'), list1.index('H'))
    print(index(list1, '!'), list1.index('!'))
    print(index(list1, ','), list1.index(','))
    print(index(list1, 'o'), list1.index('o'))
    print(index(list1, 'l'), list1.index('l'))
    print()

    # Test reverse
    reverse(list1)
    print(list1)
    reverse(list2)
    print(list2)
    list3 = []
    reverse(list3)
    print(list3)
    list4 = ['Q']
    reverse(list4)
    print(list4)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
