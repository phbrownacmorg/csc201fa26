def article(following_word: str) -> str:
    # Given a FOLLOWING_WORD, return the proper article ('a' or 'an')
    result = 'a'
    if following_word[0] in 'aeiou':
        result = 'an'
    return result

def makeVerse(animal: str, noise: str) -> None:
    # Function to print one verse of "Old MacDonald", given an ANIMAL
    #   and the NOISE it makes
    animal = article(animal) + ' ' + animal
    double_noise: str = article(noise) + ' ' + noise + ', ' + noise
    noise = article(noise) + ' ' + noise + ','
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print('And on that farm he had ' + animal + ', E-I-E-I-O!')
    print('With', double_noise, 'here and', double_noise, 'there,')
    print('Here', noise, 'there', noise, 'everywhere',
          (double_noise + ','))
    print('Old MacDonald had a farm, E-I-E-I-O!')
    print()
    
def main(args: list[str]) -> int:
    # With the function, adding an animal is *one* line, not *7*
    makeVerse('cow', 'moo')
    makeVerse('duck', 'quack')
    makeVerse('pig', 'oink')
    makeVerse('sheep', 'baa')
    makeVerse('alpaca', 'hum')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
