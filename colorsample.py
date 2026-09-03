from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Graphics demo', 600, 200)
    w.setCoords(-1, -1, 1, 1)

    font_size = 20
    instructions = Text(Point(0, 0.7),
                        'Enter red, green, and blue, and click to show.')
    instructions.setSize(font_size)
    instructions.draw(w)

    red_label: Text = Text(Point(-0.7, 0.3), 'R:')
    red_label.setSize(font_size)
    red_label.draw(w)

    red_blank: Entry = Entry(Point(-0.4, 0.3), 3)
    red_blank.setSize(font_size)
    red_blank.setFill('lightgray')
    red_blank.draw(w)

    green_label: Text = Text(Point(-0.7, -0.2), 'G:')
    green_label.setSize(font_size)
    green_label.draw(w)

    green_blank: Entry = Entry(Point(-0.4, -0.2), 3)
    green_blank.setSize(font_size)
    green_blank.setFill('lightgray')
    green_blank.draw(w)

    blue_label: Text = Text(Point(-0.7, -0.7), 'B:')
    blue_label.setSize(font_size)
    blue_label.draw(w)

    blue_blank: Entry = Entry(Point(-0.4, -0.7), 3)
    blue_blank.setSize(font_size)
    blue_blank.setFill('lightgray')
    blue_blank.draw(w)

    swatch: Rectangle = Rectangle(Point(0, 0.4), Point(0.9, -0.8))
    swatch.draw(w)

    # Wait for the click to display
    w.getMouse()

    # Read the color, and use it to color the swatch
    red: int = int(red_blank.getText())
    green: int = int(green_blank.getText())
    blue: int = int(blue_blank.getText())
    swatch.setFill(color_rgb(red, green, blue))


    # Wait for a mouse click and then close the window
    instructions.setText('Click once more to exit.')
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
