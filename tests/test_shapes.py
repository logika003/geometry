import unittest
from geometry.circle import Circle
from geometry.triangle import Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), 3.14159, places=4)

    def test_triangle_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0, places=2)

    def test_triangle_is_right(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_polymorphic_area(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]
        self.assertAlmostEqual(areas[0], 12.5664, places=4)
        self.assertAlmostEqual(areas[1], 6.0, places=2)

if __name__ == "__main__":
    unittest.main()
