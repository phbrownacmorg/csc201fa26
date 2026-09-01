from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Graphics demo', 800, 800)

    # Set pixels
    w.plot(790, 10, 'blue')

    # Use Points
    low_left: Point = Point(10, 790)
    low_left.setOutline('green')
    low_left.draw(w)

    low_right: Point = low_left.clone()
    low_right.setOutline('red')
    low_right.move(780,0)
    low_right.draw(w)

    # Line
    center: Point = Point(400, 400)
    line1: Line = Line(center, low_right)
    line1.setOutline('green')
    line1.draw(w)

    # Circle
    circle: Circle = Circle(center, 150)
    circle.setFill('purple')
    circle.draw(w)

    # Rectangle
    sse: Point = Point(600, 790)
    rect: Rectangle = Rectangle(center, sse)
    rect.setFill('orange')
    rect.draw(w)

    # Oval
    oval: Oval = Oval(center, sse)
    oval.setFill('red')
    oval.draw(w)

    # Polygon (draw a triangle)
    west: Point = Point(10, 400)
    poly: Polygon = Polygon(center, low_left, west)
    poly.setFill('blue')
    poly.draw(w)
    
    instructions: Text = Text(Point(400, 20), 'Click to exit')
    instructions.setSize(20)
    #instructions.setFace('courier')
    instructions.draw(w)

    # Aliasing
    label2: Text = instructions # Two names, one object
    label2.move(0, 760)        # Move to bottom center
    center_oval = oval.getCenter()
    label2.setText('Center of oval: (' + str(center_oval.getX()) + ','
                   + str(center_oval.getY()) + ')')
    # Changes made to label2 affect instructions as well
    anchor = instructions.getAnchor()
    instructions.setText('Anchor: (' + str(anchor.getX()) + ','
                         + str(anchor.getY()) + ')') # Not where it was!

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
