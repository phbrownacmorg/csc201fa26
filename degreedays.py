def degree_days(temps: dict[str, dict[str, int | float]]) -> dict[str, float]:
    # Returns the heating degree days and cooling degree days for the
    # given temperature data TEMPS.  TEMPS is a dictionary mapping
    # the date to the low, high, and average temperatures for that day.
    baseline = 65    # Baseline temperature used for degree-days
    degree_days: dict[str, int] = {}

    for day in temps:
        # Heating or cooling?
        if temps[day]['average'] < baseline: # Heating
            degrees = baseline - temps[day]['average']
            if 'heating' in degree_days:
                degree_days['heating'] = degree_days['heating'] + degrees
            else:
                degree_days['heating'] = degrees
        elif temps[day]['average'] > baseline: # Cooling
            degrees = temps[day]['average'] - baseline
            if 'cooling' in degree_days:
                degree_days['cooling'] = degree_days['cooling'] + degrees
            else:
                degree_days['cooling'] = degrees
    return degree_days    
    

def get_temps() -> dict[str, dict[str, int | float]]:
    # returns the recorded low, high, and average temperatures for a set of
    # dates.  Data is from https://www.wunderground.com/history/monthly/us/sc/spartanburg/date/2026-10.
    temps: dict[str, dict[str, int | float]] = {}
    dates: list[str] = ['10/' + str(d) for d in range(1, 20)]
    highs = (84, 88, 81, 73, 79, 72, 79, 82, 73, 64,
             73, 84, 86, 86, 88, 84, 66, 63, 68)
    lows = (59, 61, 68, 59, 59, 54, 50, 52, 61, 55,
            63, 59, 52, 55, 59, 63, 46, 41, 41)
    for i in range(7): #len(dates)):
        avg = (highs[i] + lows[i])/2 # Average temperature
        day_dict = {'low': lows[i], 'high': highs[i], 'average': avg}
        temps[dates[i]] = day_dict
    return temps

def main(args: list[str]) -> int:
    temps = get_temps()
    print(temps)
    print()
    d_days = degree_days(temps)
    print(d_days)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
