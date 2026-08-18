def main(args: list[str]) -> int:
    # Read the Celsius temperature (input)
    degC: float = float(input('Please enter a Celsius temperature: '))
    #print(degC) # For testing
    # Convert to Fahrenheit (process)
    degF: float = (9/5) * degC + 32

    # Print result (output)
    print(degC, 'degrees Celsius =', degF, 'degrees Fahrenheit')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
