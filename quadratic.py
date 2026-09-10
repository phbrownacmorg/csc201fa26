import math

def read_system() -> tuple[float, float, float]:
    print('Please enter the coefficients for a quadratic system.')
    a: float = float(input('\ta: '))
    b: float = float(input('\tb: '))
    c: float = float(input('\tc: '))
    return a, b, c

def find_roots(a: float, b: float, c: float) -> tuple[float, float]:
    det: float = b**2 - 4 * a * c
    # print(det)
    root1 = (-b + math.sqrt(det)) / (2*a)
    root2 = (-b - math.sqrt(det)) / (2*a)
    return root1, root2

def main(args: list[str]) -> int:
    # Read a, b, c
    a, b, c = read_system()
    print('The system is',a, '* x**2 +',b,'* x +',c,'= 0')

    # Find the roots
    root1, root2 = find_roots(a, b, c)

    # Output
    print('The roots are', root1, 'and', root2)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
