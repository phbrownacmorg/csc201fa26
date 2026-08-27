# Calculate a factorial

def main(args: list[str]) -> int:
    n: int = int(input('Please enter a positive integer: '))
    ## Accumulator variable
    fact: int = 1 ### Identity element for multiplication
    ## Loop
    for i in range(1, n+1):
        ## Update the accumulator variable each time through the loop
        fact = fact * i
    print(n, "! = ", fact, sep="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
