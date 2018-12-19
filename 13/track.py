class Track:

    def __init__(self, char):
        self.type = char

    def rotate(self, cart):
        t = self.type

        # No ratating on straight tracks
        if t in ["-", "|"]:
            return

        # Two turn types
        if t == "\\":
            self.rotateTB(cart)
        elif t == "/":
            self.rotateTF(cart)
        elif t == "+":
            cart.turnIntersection()

    def rotateTB(self, cart):
        if cart.isHorizontal():
            cart.turnRight()
        else:
            cart.turnLeft()

    def rotateTF(self, cart):
        if cart.isVertical():
            cart.turnRight()
        else:
            cart.turnLeft()

    def __str__(self):
        return self.type
