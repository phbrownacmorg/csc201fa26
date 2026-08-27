def main(args: list[str]) -> int:
    # Read a list of numbers
    length: int = int(input('How many numbers should I read? '))

    ## Accumulator pattern #1
    ### Accumulator variable
    nums: list[float] = [] #### Identity element for appending to a list
    ### Loop
    for i in range(length):
        ### Update the accumulator variable every time through the loop
        nums.append(float(input('Please enter a number: ')))
    print('The list is', nums)

    ## Accumulator pattern #2
    ### Accumulator variable
    total = 0 #### Identity element for addition
    ### Loop
    for value in nums:
        ### Update the accumulator variable each time through the loop
        total = total + value
    print('The sum of the list is', total)

    # For illustration only, accumulator pattern #3
    ### Accumulator variables
    length = 0 #### Identity element for addition
    total = 0 #### Identity element for addition
    ### Loop
    for value in nums:
        ### Update the accumulator variables each time through the loop
        total = total + value
        length = length + 1
    print('The average of the list is', (total/length))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
