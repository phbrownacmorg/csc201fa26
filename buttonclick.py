from graphics import *

def inButton(click: Point, button: Rectangle) -> bool:
    # Function takes a Point CLICK and a Rectangle BUTTON,
    # and returns True if and only if the CLICK is in the BUTTON.
    corner_1: Point = button.getP1()
    corner_2: Point = button.getP2()
    min_x: float = min(corner_1.getX(), corner_2.getX())
    max_x: float = max(corner_1.getX(), corner_2.getX())
    min_y: float = min(corner_1.getY(), corner_2.getY())
    max_y: float = max(corner_1.getY(), corner_2.getY())
    return min_x <= click.getX() <= max_x \
           and min_y <= click.getY() <= max_y

def drawList(objects: list[GraphicsObject], win: GraphWin) -> None:
    # Takes a list of GraphicsObject OBJECTS and a GraphWin WIN,
    # and draws all the objects in OBJECTS on WIN.
    for obj in objects:
        obj.draw(win)

def makeButton(p1: Point, p2: Point, label_text: str) -> list[GraphicsObject]:
    # Takes two Points P1 and P2 and a string LABEL_TEXT. Creates
    # and returns a list of GraphicsObject containing, first, a Rectangle
    # defined by P1 and P2, and second, a Text centered at the center of
    # the Rectangle with text LABEL_TEXT.
    button_list: list[GraphicsObject] = []
    rect = Rectangle(p1, p2)
    button_list.append(rect)
    button_list.append(Text(rect.getCenter(), label_text))
    return button_list

def main(args: list[str]) -> int:
    # Make a GraphWin and a button, and draw them.  For five mouse clicks,
    # toggle the button's background color from red to green if the click
    # is in the button.  Then wait for a sixth click and exit.
    w: GraphWin = GraphWin('Graphics demo', 800, 800)
    w.setCoords(-1, -1, 1, 1)

    # Make a button
    button = makeButton(Point(-0.3, -0.3), Point(0.3, 0.3),
                        'Click to change color')
    drawList(button, w)
    color = 'red'

    # Get five clicks, checking whether each is in the button
    for i in range(5):
        click: Point = w.getMouse()
        if inButton(click, button[0]):
            button[0].setFill(color)
            if color == 'red':
                color = 'green'
            else:
                color = 'red'

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
