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

    def run(self, destroy=False):
        # print(self)
        print("Running...")
        runs = 1
        while True:
            for cartPos in sorted(self.carts.keys())[:]:
                # Has the cart been removed in the mean time?
                if not cartPos in self.carts:
                    continue

                # Pop the cart
                cart = self.carts[cartPos]
                del self.carts[cartPos]

                # Move it
                nextPos = cart.nextPos(cartPos)
                y, x = nextPos
                assert self.tiles[y][x], f"There is a tile at ({x},{y})"

                # Check for collisions
                if nextPos in self.carts:
                    # Should we continue after a collision?
                    if not destroy:
                        print(f"Collision in run #{runs}")
                        return nextPos
                    else:
                        # Would there be carts left after the collision?
                        print(f"Collision in run #{runs} ({len(self.carts)-1} left)")
                        if len(self.carts) >= 2:
                            del self.carts[(y,x)]

                # If there were no collisions
                else:

                    # Rotate due to the track
                    self.tiles[y][x].rotate(cart)

                    # Reinsert
                    self.carts[nextPos] = cart

            # Stop if there is one cart left
            if len(self.carts) <= 1:
                return list(self.carts.keys())[0]

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
