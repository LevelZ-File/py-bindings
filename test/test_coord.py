from levelz import Dimension, Coordinate2D, Coordinate3D
import unittest

class TestDimension(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(Dimension.TWO, 2)
        self.assertEqual(Dimension.THREE, 3)

        self.assertTrue(Dimension.TWO.is2D)
        self.assertFalse(Dimension.TWO.is3D)
    
    def test_dimension_eq(self):
        self.assertEqual(Dimension.TWO, 2)
        self.assertEqual(Dimension.TWO, Dimension.TWO)
        self.assertEqual(Dimension.THREE, 3)
        self.assertEqual(Dimension.THREE, Dimension.THREE)
        self.assertEqual(Dimension.TWO, "2")
        self.assertEqual(Dimension.THREE, "3")

        self.assertNotEqual(Dimension.TWO, 3)
        self.assertNotEqual(Dimension.TWO, Dimension.THREE)
        self.assertNotEqual(Dimension.THREE, 2)
        self.assertNotEqual(Dimension.THREE, Dimension.TWO)
        self.assertNotEqual(Dimension.THREE, "2")
        self.assertNotEqual(Dimension.TWO, "3")
        self.assertNotEqual(Dimension.TWO, None)

    
    def test_dimension_str(self):
        self.assertEqual(str(Dimension.TWO), "2")
        self.assertEqual(str(Dimension.THREE), "3")

class TestCoordinate2D(unittest.TestCase):
    def test_magnitude(self):
        c = Coordinate2D(3, 4)
        self.assertEqual(c.magnitude, 5)
    
    def test_dimension(self):
        c = Coordinate2D(17, 32)
        self.assertEqual(c.dimension, Dimension.TWO)

    def test_from_string(self):
        c1 = Coordinate2D.from_string("[0, 0]")
        self.assertEqual(c1.x, 0)
        self.assertEqual(c1.y, 0)

        c2 = Coordinate2D.from_string("[3, 4]")
        self.assertEqual(c2.x, 3)
        self.assertEqual(c2.y, 4)

        c3 = Coordinate2D.from_string("[-7, 9]")
        self.assertEqual(c3.x, -7)
        self.assertEqual(c3.y, 9)

        c4 = Coordinate2D.from_string("[93.14, -72.71]")
        self.assertEqual(c4.x, 93.14)
        self.assertEqual(c4.y, -72.71)
    
    def test_eq(self):
        c1 = Coordinate2D(-3, 4)
        c2 = Coordinate2D(-3, 4)
        self.assertEqual(c1, c2)

        c3 = Coordinate2D(3, -4)
        self.assertNotEqual(c1, c3)

        c4 = Coordinate2D(-3, -4)
        self.assertEqual(c4, [-3, -4])
        self.assertEqual(c4, "[-3, -4]")
        self.assertEqual(c4, (-3, -4))

        self.assertNotEqual(c1, None)

class TestCoordinate3D(unittest.TestCase):
    def test_magnitude(self):
        c = Coordinate3D(2, 3, 6)
        self.assertEqual(c.magnitude, 7)

    def test_dimension(self):
        c = Coordinate3D(17, 32, 8)
        self.assertEqual(c.dimension, Dimension.THREE)

    def test_from_string(self):
        c1 = Coordinate3D.from_string("[0, 0, 0]")
        self.assertEqual(c1.x, 0)
        self.assertEqual(c1.y, 0)
        self.assertEqual(c1.z, 0)

        c2 = Coordinate3D.from_string("[3, 4, 5]")
        self.assertEqual(c2.x, 3)
        self.assertEqual(c2.y, 4)
        self.assertEqual(c2.z, 5)

        c3 = Coordinate3D.from_string("[-7, 9, 10]")
        self.assertEqual(c3.x, -7)
        self.assertEqual(c3.y, 9)
        self.assertEqual(c3.z, 10)

        c4 = Coordinate3D.from_string("[93.14, -72.71, 746.847]")
        self.assertEqual(c4.x, 93.14)
        self.assertEqual(c4.y, -72.71)
        self.assertEqual(c4.z, 746.847)

    def test_eq(self):
        c1 = Coordinate3D(-3, 4, 5)
        c2 = Coordinate3D(-3, 4, 5)
        self.assertEqual(c1, c2)

        c3 = Coordinate3D(3, -4, 5)
        self.assertNotEqual(c1, c3)

        c4 = Coordinate3D(-3, 4, -5)
        self.assertNotEqual(c1, c4)

        c5 = Coordinate3D(-3, -4, 5)
        self.assertEqual(c5, [-3, -4, 5])
        self.assertEqual(c5, "[-3, -4, 5]")
        self.assertEqual(c5, (-3, -4, 5))

        self.assertNotEqual(c1, None)
