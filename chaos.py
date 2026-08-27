# File: chaos.py
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    # Accumulator variable
    x = float(input("Enter a number between 0 and 1: "))
    # Clamp the input to the interval [0, 1]
    x = min(1, max(0, x))
    print('Seed value, clamped to interval [0, 1]:', x)
    # Loop
    for i in range(10):
        # Each time around the loop, update the accumulator variable
        x = 3.9 * x * (1 - x)
        print(x)
    
main()
