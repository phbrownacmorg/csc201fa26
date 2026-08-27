from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Graphics demo', 800, 800)

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
