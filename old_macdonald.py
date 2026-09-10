def makeVerse(animal: str, noise: str) -> None:
    # Function to print one verse of "Old MacDonald", given an ANIMAL
    #   and the NOISE it makes
    double_noise: str = noise + ', ' + noise
    noise = noise + ','
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print('And on that farm he had a ' + animal + ', E-I-E-I-O!')
    print('With a', double_noise, 'here and a', double_noise, 'there,')
    print('Here a', noise, 'there a', noise, 'everywhere a',
          (double_noise + ','))
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print()
    
def main(args: list[str]) -> int:
    # With the function, adding an animal is *one* line, not *7*
    makeVerse('cow', 'moo')
    makeVerse('duck', 'quack')
    makeVerse('pig', 'oink')
    makeVerse('sheep', 'baa')
    
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print('And on that farm he had a cow, E-I-E-I-O!')
##    print('With a moo, moo here and a moo, moo there,')
##    print('Here a moo, there a moo, everywhere a moo, moo,')
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print()
##
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print('And on that farm he had a duck, E-I-E-I-O!')
##    print('With a quack, quack here and a quack, quack there,')
##    print('Here a quack, there a quack, everywhere a quack, quack,')
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print()
##    
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print('And on that farm he had a pig, E-I-E-I-O!')
##    print('With an oink, oink here and an oink, oink there,')
##    print('Here an oink, there an oink, everywhere an oink, oink,')
##    print('Old MacDonald had a farm, E-I-E-I-O!')
##    print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
