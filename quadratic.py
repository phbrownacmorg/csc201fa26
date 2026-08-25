import math

def main(args: list[str]) -> int:
    # Read a, b, c
    print('Please enter the coefficients for a quadratic system.')
    a: float = float(input('\ta: '))
    b: float = float(input('\tb: '))
    c: float = float(input('\tc: '))
    print('The system is',a, '* x**2 +',b,'* x +',c,'= 0')

    # Find the roots
    det: float = b**2 - 4 * a * c
    # print(det)
    root1 = (-b + math.sqrt(det)) / (2*a)
    root2 = (-b - math.sqrt(det)) / (2*a)

    # Output
    print('The roots are', root1, 'and', root2)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
