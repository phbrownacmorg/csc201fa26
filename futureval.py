# Calculate the future value of an investment
# Inputs: Principal amount, interest rate, number of periods
# Output: Table of the values of the investment at any given time

def main(args: list[str]) -> int:
    # Input
    ## Accumulator variable
    amount: float = float(input('Please enter an amount to invest, in dollars: $'))
    rate: float = float(input('Please enter the interest rate, in percent: ')) / 100
    periods: int = int(input('Please enter how long the investment will be for, '
                        +'in periods: '))
    print('Investing $', round(amount,2), 'at', (rate*100), '% for', periods, 'periods.')
    
    # Process and Output together
    ## Print the top of the table
    print('Period','Amount',sep='\t')
    print('-' * 30)

    ## Loop to calculate and print the values in the table
    ### (Accumulator-pattern loop)
    for i in range(periods+1):
        print(i, round(amount,2), sep="\t$")
        # Update the accumulator variable
        amount = amount + (amount * rate)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
