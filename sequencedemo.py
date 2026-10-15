from typing import Any

def indexing_and_slicing(listvar: list[int | str]) -> None:
    print(listvar)
    print(len(listvar))

    # Indexing
    for i in range(len(listvar)):
        print(f'{i:^3}', end=' ')
    print()
    for i in range(len(listvar)):
        print(f'{listvar[i]:^3}', end=' ')
    print()
    for i in range(-1, -len(listvar) - 1, -1):
        print(f'{listvar[i]:^3}', end=' ')
    print()
    for i in range(-1, -len(listvar) - 1, -1):
        print(f'{i:^3}', end=' ')
    print()
    print()
    
    # Slicing (with a list comprehension)
    for i in range(len(listvar)):
        print(listvar[:i], ' ', listvar[i:])
    print()

    # Slicing, with a beginning and an end
    for i in range(len(listvar) // 2 + 1):
        begin = len(listvar)//2 - i
        end = len(listvar)//2 + i
        print(begin, end, ':', listvar[begin:end])
    print()

    # Slicing, with step
    print('Evens:', listvar[::2])
    print('Odds:', listvar[1::2])
    print()

def operations_on_mutable(listvar: list[int | str]) -> None:
    # Iteration by value (not by index)
    for item in listvar:
        print(str(item), end='')
    print()
    
    # Assignment using index: add 1 to all the numbers
    for i in range(7, len(listvar)):
        listvar[i] = listvar[i] + 1 # Add 1 to each of the numbers
    print(listvar)

    # Adding items using "append"
    top_item = listvar[-1]
    for i in range(3):
        listvar.append(top_item - i)
    print(listvar)    

    # Growing a list with "extend"
    shorter = listvar[:5]
    shorter2 = list(range(5))
    print(shorter, shorter2)
    shorter.extend(shorter2)
    print(shorter)

    # Pop
    # Pop from end
    for i in range(3):
        value = listvar.pop()
        print(listvar, value)

    # Pop from beginning
    for i in range(3):
        value = listvar.pop(0)
        print(value, listvar)


def main(args: list[str]) -> int:
    listvar = list('Hello, ') + list(range(10))
    indexing_and_slicing(listvar)
    operations_on_mutable(listvar)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
