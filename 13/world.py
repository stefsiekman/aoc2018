from track import Track
from cart import Cart

class World:

    def __init__(self, lines):
        self.width = max([len(l) for l in lines])
        self.height = len(lines)
        print(f"Scanning {self.width}x{self.height} world.")

        self.tiles = [[None]*self.width for _ in range(self.height)]
        self.carts = {}

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char in ["\\", "/", "-", "|", "+"]:
                    self.tiles[y][x] = Track(char)
                elif char in [">", "<"]:
                    self.tiles[y][x] = Track("-")
                    self.carts[(y,x)] = Cart(char)
                elif char in ["^", "v"]:
                    self.tiles[y][x] = Track("|")
                    self.carts[(y,x)] = Cart(char)

        print(f"There are {len(self.carts)} carts on the tracks.")

    def run(self):
        # print(self)
        print("Running...")
        runs = 1
        while True:
            for cartPos in sorted(self.carts.keys()):
                # Pop the cart
                cart = self.carts[cartPos]
                del self.carts[cartPos]

                # Move it
                nextPos = cart.nextPos(cartPos)
                y, x = nextPos
                assert self.tiles[y][x], f"There is a tile at ({x},{y})"

                # Check for collisions
                if nextPos in self.carts:
                    print(f"Collision in run #{runs}")
                    return nextPos

                # Rotate due to the track
                self.tiles[y][x].rotate(cart)

                # Reinsert
                self.carts[nextPos] = cart
            runs += 1
            # print(self)
        return None

    def __str__(self):
        string = ""
        for y in range(self.height):
            for x in range(self.width):
                # Draw cart?
                if (y,x) in self.carts:
                    string += str(self.carts[(y,x)])
                elif self.tiles[y][x]:
                    string += str(self.tiles[y][x])
                else:
                    string += " "

            string += "\n"

        return string
