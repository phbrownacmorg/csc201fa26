from graphics import *
import math

# Replace the mouse with a list of GraphicsObject items.
# The first item on the list supports getCenter(); that is the center
# of the compound object.


def makeHead(radius: float, color: str) -> Circle:
    # Make and return a "head" (circle) of the given RADIUS and COLOR
    head = Circle(Point(0, 0), radius)
    head.setFill(color)
    head.setOutline(color)
    return head

def makeEyes(radius: float, color: str) -> list[GraphicsObject]:
    # Make and return eyes of the given COLOR for a head of radius RADIUS.
    eyes: list[GraphicsObject] = []
    angle = math.radians(55)
    outer = 0.9
    for side in [-1, 1]:
        eye: Oval = Oval(Point(0.07 * radius * side, 0),
                         Point(side * outer * radius * math.cos(angle),
                                outer * radius * math.sin(angle)))
        eye.setFill(color)
        eyes.append(eye)
    return eyes

def makeMouseEars(radius: float, color: str) -> list[GraphicsObject]:
    # Make and return mouse ears of the given COLOR for a head of radius RADIUS.
    ears: list[GraphicsObject] = []
    # Distance to the center of the ears / radius
    ear_center: float = 1.4
    ear_radius: float = 0.6
    angle = math.radians(55)
    for side in [-1, 1]:
        ear: Circle = Circle(Point(side * ear_center * radius * math.cos(angle),
                              ear_center * radius * math.sin(angle)),
                             ear_radius * radius)
        ear.setFill(color)
        ear.setOutline(color)
        ears.append(ear)
    return ears

def makeCatEars(radius: float, color: str) -> list[GraphicsObject]:
    # Make and return cat ears of the given COLOR for a head of radius RADIUS
    ears: list[GraphicsObject] = []
    outer_r: float = 1.8
    central_angle = math.radians(55)
    half_angle = math.radians(25)
    for side in [-1, 1]:
        tip = Point(side * radius * outer_r * math.cos(central_angle),
                    radius * outer_r * math.sin(central_angle))
        high = Point(side * radius * math.cos(central_angle + half_angle),
                     radius * math.sin(central_angle + half_angle))
        low = Point(side * radius * math.cos(central_angle - half_angle),
                     radius * math.sin(central_angle - half_angle))
        ear = Polygon(high, tip, low)
        ear.setFill(color)
        ear.setOutline(color)
        ears.append(ear)
    return ears

def makeMouse() -> list[GraphicsObject]:
    # Make and return a list of GraphicsObjects representing a "mouse"
    animal: list[GraphicsObject] = []

    radius = 0.05
    color = 'gray'
    animal.append(makeHead(radius, color))
    animal.extend(makeEyes(radius, 'black'))
    animal.extend(makeMouseEars(radius, color))

    return animal

def makeCat() -> list[GraphicsObject]:
    # Make and return a list of GraphicsObjects representing a cat
    animal: list[GraphicsObject] = []

    radius = 0.2
    color = 'orange'
    animal.append(makeHead(radius, color))
    animal.extend(makeEyes(radius, 'green'))
    animal.extend(makeCatEars(radius, 'orange'))

    return animal

def animalCenter(animal: list[GraphicsObject]) -> Point:
    return animal[0].getCenter()    # type: ignore
    
def drawList(objects: list[GraphicsObject],
             win: GraphWin) -> list[GraphicsObject]:
    # Takes a list of GraphicsObjects, and draws them on the given WIN.
    # Returns the list, now drawn.
    for item in objects:
        item.draw(win)
    return objects

def moveTo(objects: list[GraphicsObject], dest: Point) -> list[GraphicsObject]:
    # Moves a list of GraphicsObject OBJECTS to a Point DEST.
    # Returns the list, now moved.
    center: Point = animalCenter(objects)
    dx = dest.getX() - center.getX()
    dy = dest.getY() - center.getY()
    for item in objects:
        item.move(dx, dy)
    return objects

def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics demo', 800, 800)
    w.setCoords(-1, -1, 1, 1)

    # Instructions label
    instructions: Text = Text(Point(0, 0.95),
                              "Click to have the circle follow the mouse")
    instructions.draw(w)

    # Draw the "mouse"
    mouse = drawList(makeMouse(), w)
    cat = drawList(moveTo(makeCat(), Point(1,1)), w)

    # Chase the clicks for 5 clicks
    for i in range(5): # type: ignore
        click: Point = w.getMouse()
        mousePos: Point = animalCenter(mouse)
        moveTo(mouse, click)
        moveTo(cat, mousePos)

    # Wait for a mouse click and then close the window
    instructions.setText('Click once more to exit')
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
