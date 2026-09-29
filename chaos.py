# File: chaos.py
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    # Accumulator variable
    try:
        x = float(input("Enter a number between 0 and 1: "))
        if x < 0 or x > 1:
            raise ValueError
    except ValueError:
        print('The input needs to be a number greater than 0 and less than 1.')
    else:
        print('Seed value, clamped to interval [0, 1]:', x)
        # Loop
        for i in range(10): # type: ignore
            # Each time around the loop, update the accumulator variable
            x = 3.9 * x * (1 - x)
            print(x)
    
main()
