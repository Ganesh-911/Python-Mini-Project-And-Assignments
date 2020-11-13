class Shapes:

    def __init__(self):

        self.dimensions = 1

    def get_dimensions(self):

        return self.dimensions
        
    def set_dimensions(self, dim):

        self.dimensions = dim

class Triangle(Shapes):

    def edges(self):
        print("\nTriangle has 3 edges")

    def vertices(self):
        print("\nTriangle has 3 vertices")
        

class Square(Shapes):

    def edges(self):
        print("\nSquare has 4 edges")

    def vertices(self):
        print("\nSquare has 4 vertices")

class Rectangle(Shapes):

    def edges(self):
        print("\nRectangle has 4 edges")

    def vertices(self):
        print("\nRectangle has 4 vertices")

class Pentagon(Shapes):

    def edges(self):
        print("\nPentagon has 5 edges")

    def vertices(self):
        print("\nPentagon has 5 vertices")

class Hexagon(Shapes):

    def edges(self):
        print("\nHexagon has 6 edges")

    def vertices(self):
        print("\nHexagon has 6 vertices")

class Heptagon(Shapes):

    def edges(self):
        print("\nHeptagon has 7 edges")

    def vertices(self):
        print("\nHeptagon has 7 vertices")

class Octagon(Shapes):

    def edges(self):
        print("\nOctagon has 8 edges")

    def vertices(self):
        print("\nOctagon has 8 vertices")

class Cube(Shapes):

    def edges(self):
        print("\nCube has 12 edges")

    def vertices(self):
        print("\nCube has 8 vertices")

    def faces(self):
        print("\nCube has 6 faces")

class Cuboid(Shapes):

    def edges(self):
        print("\nCuboid has 12 edges")

    def vertices(self):
        print("\nCuboid has 8 vertices")

    def faces(self):
        print("\nCuboid has 6 faces")

class Tetrahedron(Shapes):

    def edges(self):
        print("\nTetrahedron has 6 edges")

    def vertices(self):
        print("\nTetrahedron has 4 vertices")

    def faces(self):
        print("\nTetrahedron has 4 faces")

Cube.faces(Cube)

Hexagon.edges(Hexagon)

Rectangle.vertices(Rectangle)

Triangle.set_dimensions(Triangle, 2)

print("\nTriangle is",Triangle.get_dimensions(Triangle), "dimensional shape.")