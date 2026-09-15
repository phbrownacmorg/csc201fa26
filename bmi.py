# Beyonce: 5'7" (67"), 135 lbs. (AI estimate from Google search on "Beyonce height weight")
# LeBron James: 6'9" (81"), 250 lbs. (https://www.basketball-reference.com/players/j/jamesle01.html)
# Tom Holland: 5'8" (68"), 140 lbs. (https://app.routines.club/blogs/workouts/tom-holland-physique?srsltid=AU7gw4VHSwQ35YM7iNp5FkYjdsNi_f-32mJbqNBfsb3BAlxq8T_1eM87)
# Tom Cruise: 5'7" (67"), 155 lbs. (AI estimate from Google search on "Tom Cruise height weight")
# Erling Haaland: 6'4" (76"), 194 lbs. (https://www.foxsports.com/soccer/erling-haaland-player-bio)
# Jamie Foxx: 5'9" (69"), 190 lbs. (https://www.legit.ng/ask-legit/biographies/1598077-jamie-foxxs-net-worth-wife-children-how-health/)
# Arnold Schwarzenegger: 6'2" (74"), 250 lbs. (https://en.wikipedia.org/wiki/Arnold_Schwarzenegger)
# Naomi Campbell: 5'10" (70"), 105 lbs. (https://mediatakeout.com/supermodel-naomi-campbells-shocking-new-look-now-100-lbs/)

def get_height_weight() -> tuple[float, float]:
    # Read and return a person's height and weight in U.S. customary units
    height: float = float(input("Please enter the person's height in inches: "))
    weight: float = float(input("Please enter the person's weight in pounds: "))
    return height, weight

def calc_bmi(height: float, weight: float) -> float:
    # Calculate and return BMI, based on the given HEIGHT and WEIGHT.
    # Source: https://www.cdc.gov/growth-chart-training/hcp/using-bmi/calculating-bmi.html
    return (weight / height**2) * 703

def classify_bmi(bmi: float) -> str:
    # Takes a BMI and returns the classification for that BMI, following
    # https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html.
    result = ''
    if bmi < 18.5:
        result = 'underweight'
    elif bmi < 25:
        result = 'healthy'
    elif bmi < 30:
        result = 'overweight'
    elif bmi < 35:
        result = 'obese (class 1)'
    elif bmi < 40:
        result = 'obese (class 2)'
    else:
        result = 'obese (class 3 or severe)'
    return result

def main(args: list[str]) -> int:
    height, weight = get_height_weight()
    print('Height:', str(height) + '"; weight:', weight, 'lbs.')
    bmi: float = calc_bmi(height, weight)
    print('BMI:', round(bmi, 1))
    print('This person is classified as', classify_bmi(bmi))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
