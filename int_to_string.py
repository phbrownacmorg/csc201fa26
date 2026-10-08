# Read an integer from the keyboard, convert it to a string, and write that out

def int_to_string(num: int) -> str:
    result: str = ''
    
    sign: str = ''
    if num < 0:
        sign = '-'
        num = -num
        
    while num > 0:
        digit: str = chr(ord('0') + (num % 10))
        result = digit + result
        num = num // 10
    
    return sign + result

def main(args: list[str]) -> int:
    num: int = int(input('Please enter an integer: '))
    print(int_to_string(num))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
