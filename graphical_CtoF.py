from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Graphics demo', 600, 100)
    w.setCoords(-1, -1, 1, 1)

    font_size = 20

    instructions: Text = Text(Point(0, 0.5),
                              'Enter a Celsius temperature and click to convert')
    instructions.setSize(font_size)
    instructions.draw(w)

    celsius = Entry(Point(-0.5, -0.3), 5)
    celsius.setSize(font_size)
    celsius.setFill('lightgray')
    celsius.draw(w)

    celsius_label = Text(Point(0,-0.3), '\u00b0C =')
    celsius_label.setSize(font_size)
    celsius_label.draw(w)

    w.getMouse() # Click to convert
    degC: float = float(celsius.getText())
    degF: float = (9/5) * degC + 32
    fahrenheit_label = Text(Point(0.5, -0.3), str(round(degF, 1)) + '\u00b0 F')
    fahrenheit_label.setSize(font_size)
    fahrenheit_label.draw(w)

    instructions.setText('Click once more to exit')

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
