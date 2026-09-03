from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Graphics demo', 800, 800)
    w.setCoords(-1, -1, 1, 1)

    # Instructions label
    instructions: Text = Text(Point(0, 0.95),
                              "Click to have the circle follow the mouse")
    instructions.draw(w)

    # Draw the "mouse"
    mouse = Circle(Point(0, 0), 0.05)
    mouse.setFill('gray')
    mouse.draw(w)

    # Chase the clicks for 5 clicks
    for i in range(5):
        click: Point = w.getMouse()
        center: Point = mouse.getCenter()
        dx = click.getX() - center.getX()
        dy = click.getY() - center.getY()
        mouse.move(dx, dy)

    # Wait for a mouse click and then close the window
    instructions.setText('Click once more to exit')
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
