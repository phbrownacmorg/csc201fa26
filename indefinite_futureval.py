# Calculate the future value of an investment
# Inputs: Principal amount, interest rate, number of periods
# Output: Table of the values of the investment at any given time

from graphics import *
import math

def read_parameters() -> tuple[float, float]:
    amount: float = math.nan # Invalid value, will be overwritten
    rate: float = math.nan # Invalid value, will be overwritten
    try:
        amount = float(input('Please enter an amount to invest, in dollars: $'))
        rate = float(input('Please enter the interest rate, in percent: '))/100
        if amount < 0 or rate < 0:
            raise ValueError
    except ValueError:
        print('Amount and rate must both be positive numbers.')
        amount = math.nan
    return amount, rate

def calc_investment(amount: float, rate: float) -> list[float]:
    ## Accumulator variable #2
    values: list[float] = [amount] # Start with the intial amount
    ## Loop to calculate the values in the table
    ### (Accumulator-pattern loop)
    while amount < values[0] * 2:
        # Update the accumulator variable
        amount = amount + (amount * rate)
        # Update accumulator variable #2
        values.append(amount)
    return values    

def print_table(values: list[float]) -> None:
    ## Print the top of the table
    print('Period','Amount',sep='\t')
    print('-' * 30)

    ## Print the body of the table
    for i in range(len(values)):
        print(i, round(values[i],2), sep="\t$")

def draw_axes(max_x: float, max_y: float, margin: float, w: GraphWin) -> None:
    x_axis: Line = Line(Point(0,0), Point(max_x*(1+margin/2),0))
    x_axis.setArrow('last')
    x_axis.draw(w)
    y_axis: Line = Line(Point(0,0), Point(0, max_y*(1+margin/2)))
    y_axis.setArrow('last')
    y_axis.draw(w)

def draw_bars(values: list[float], w: GraphWin) -> None:
    for i in range(len(values)):
        bar = Rectangle(Point(i,0), Point(i+1,values[i]))
        bar.setFill('green')
        bar.draw(w)

def draw_y_ticks(max_x: float, max_y: float, margin: float,
                     w: GraphWin) -> None:
    ### Find the spacing
    # max_ticks = 25
    # min_ticks = 5
    log_max_y = int(math.log10(max_y))
    tick_spacing = 10**log_max_y / 5
    num_ticks = int(max_y // tick_spacing) + 1
    # print(num_ticks, tick_spacing)
    for i in range(num_ticks):
        y = tick_spacing * i
        tick = Line(Point(0, y), Point(-margin * max_x * 0.1, y))
        tick.draw(w)

        val_string = '$' + str(round(y))
        label = Text(Point(-margin * max_x * 0.5, y), val_string)
        label.draw(w)


def make_bar_graph(values: list[float]) -> None:
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
    draw_axes(len(values), max_val, margin, w)

    ## Draw the bars
    draw_bars(values, w)
    ## Add labels and tick-marks to the Y axis
    draw_y_ticks(len(values), max_val, margin, w)
    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()


def main(args: list[str]) -> int:
    # Input
    ## Accumulator variable
    amount, rate = read_parameters()
    if not math.isnan(amount):
        print('Investing $', round(amount,2), 'at', (rate*100), '% until it doubles.')
        
        # Process
        values = calc_investment(amount, rate)

        # Output
        print_table(values)
        make_bar_graph(values)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
