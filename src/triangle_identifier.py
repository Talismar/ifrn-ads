class TriangleIdentifier:
    def __init__(self, side_x, side_y, side_z):
        self.side_x = side_x
        self.side_y = side_y
        self.side_z = side_z

    def is_triangle(self):
        if (self.side_x > 0 and self.side_y > 0 and self.side_z > 0) and \
           (self.side_x + self.side_y > self.side_z and \
            self.side_x + self.side_z > self.side_y and \
            self.side_y + self.side_z > self.side_x):
            return True
        else:
            return False