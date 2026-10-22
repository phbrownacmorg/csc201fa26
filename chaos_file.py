# File: chaos_file.py
# A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")

    with open('chaos-seeds.csv','r') as f:
        for line in f.readlines():
            tokens: list[str] = line.split(',')
            x: float = -1
            try:
                x = float(tokens[0])
                if x < 0 or x > 1:
                    raise ValueError                
                print('Seed value:', x)
            except ValueError:
                print('The seed needs to be greater than 0 and less than 1.')
                continue
            else:
                try:
                    n = int(tokens[1])
                    if n < 0:
                        raise ValueError
                    print('Iterations:', n)
                except ValueError:
                    print('The number of iterations must be a non-negative integer.')
                    continue                 
                else:
                    print(f'{"i":>2}\t{"x":^12}')
                    print('-' * 20)
                    # Loop
                    for i in range(n): # type: ignore
                        # Each time around the loop, update the accumulator variable
                        x = 3.9 * x * (1 - x)
                        print(f'{i+1:>2}\t{x:<12.10}')
                    print()

if __name__ == '__main__':
    main()
