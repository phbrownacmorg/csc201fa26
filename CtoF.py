def main(args: list[str]) -> int:
    # Constant
    ABS_ZERO: float = -273.15
    # Read the Celsius temperature (input)
    try:
        degC: float = float(input('Please enter a Celsius temperature: '))
        if degC < ABS_ZERO:
            raise ValueError
    except ValueError:
        print('A Celsius temperature is a number.  It cannot be less than',
              '\n\tabsolute zero:', str(ABS_ZERO) + '.')
    else:
        # Convert to Fahrenheit (process)
        degF: float = (9/5) * degC + 32

        # Print result (output)
        print(degC, '\u00b0 C =', degF, '\u00b0 F', sep='')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
