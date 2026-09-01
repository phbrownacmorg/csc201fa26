# Calculate the future value of an investment
# Inputs: Principal amount, interest rate, number of periods
# Output: Table of the values of the investment at any given time

from graphics import *
import math

def main(args: list[str]) -> int:
    # Input
    ## Accumulator variable
    amount: float = float(input('Please enter an amount to invest, in dollars: $'))
    rate: float = float(input('Please enter the interest rate, in percent: ')) / 100
    periods: int = int(input('Please enter how long the investment will be for, '
                        +'in periods: '))
    print('Investing $', round(amount,2), 'at', (rate*100), '% for', periods, 'periods.')
    
    # Process
    ## Accumulator variable #2
    values: list[float] = []
    
    ## Loop to calculate the values in the table
    ### (Accumulator-pattern loop)
    for i in range(periods+1):
        # Update accumulator variable #2
        values.append(amount)
        # Update the accumulator variable
        amount = amount + (amount * rate)

    # Output
    ## Print the top of the table
    print('Period','Amount',sep='\t')
    print('-' * 30)

    ## Print the body of the table
    for i in range(len(values)):
        print(i, round(values[i],2), sep="\t$")

    # Output as bar graph
    w: GraphWin = GraphWin('Investment values', 800, 800)
    ## Make the coordinate system match the problem
    margin: float = 0.1 # Margin is 10% of the graph size
    min_x = len(values) * -margin
    max_x = len(values) * (1 + margin)
    max_val = max(values)
    min_y = max_val * -margin
    max_y = max_val * (1 + margin)

    w.setCoords(min_x, min_y, max_x, max_y)

    ## Axes
    x_axis: Line = Line(Point(0,0), Point(len(values)*(1+margin/2),0))
    x_axis.setArrow('last')
    x_axis.draw(w)
    y_axis: Line = Line(Point(0,0), Point(0, max_val*(1+margin/2)))
    y_axis.setArrow('last')
    y_axis.draw(w)

    ## Draw the bars
    for i in range(len(values)):
        bar = Rectangle(Point(i,0), Point(i+1,values[i]))
        bar.setFill('green')
        bar.draw(w)
      
    ## Add labels and tick-marks to the Y axis
    ### Find the spacing
    # max_ticks = 25
    # min_ticks = 5
    log_max_val = int(math.log10(max_val))
    tick_spacing = 10**log_max_val / 5
    num_ticks = int(max_val // tick_spacing) + 1
    # print(num_ticks, tick_spacing)
    for i in range(num_ticks):
        y = tick_spacing * i
        tick = Line(Point(0, y), Point(-margin * len(values) * 0.1, y))
        tick.draw(w)

        val_string = '$' + str(round(y))
        label = Text(Point(-margin * len(values) * 0.5, y), val_string)
        label.draw(w)
        

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
