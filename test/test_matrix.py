from levelz import Dimension, Coordinate2D, Coordinate3D, CoordinateMatrix2D, CoordinateMatrix3D
import unittest

class TextCoordinateMatrix2D(unittest.TestCase):
    def test_constructor(self):
        cm = CoordinateMatrix2D(0, 1, 0, 1, Coordinate2D(0, 0))
        self.assertEqual(cm.dimension, Dimension.TWO)
        self.assertEqual(cm.coordinates.__len__(), 4)
    
    def test_str(self):
        cm = CoordinateMatrix2D(0, 1, 0, 1, Coordinate2D(0, 0))
        self.assertEqual(str(cm), "(0, 1, 0, 1)^[0, 0]")
    
    def test_eq(self):
        cm1 = CoordinateMatrix2D(0, 1, 0, 1, Coordinate2D(0, 0))
        cm2 = CoordinateMatrix2D(0, 1, 0, 1, Coordinate2D(0, 0))
        self.assertEqual(cm1, cm2)
    
    def test_from_string(self):
        cm = CoordinateMatrix2D.from_string("(0, 2, 0, 2)^[2, 3]")
        self.assertEqual(cm.minX, 0)
        self.assertEqual(cm.maxX, 2)
        self.assertEqual(cm.minY, 0)
        self.assertEqual(cm.maxY, 2)
        self.assertEqual(cm.start, Coordinate2D(2, 3))

class TestCoordinateMatrix3D(unittest.TestCase):
    def test_constructor(self):
        cm = CoordinateMatrix3D(0, 1, 0, 1, 0, 1, Coordinate3D(0, 0, 0))
        self.assertEqual(cm.dimension, Dimension.THREE)
        self.assertEqual(cm.coordinates.__len__(), 8)
    
    def test_str(self):
        cm = CoordinateMatrix3D(0, 1, 0, 1, 0, 1, Coordinate3D(0, 0, 0))
        self.assertEqual(str(cm), "(0, 1, 0, 1, 0, 1)^[0, 0, 0]")
    
    def test_eq(self):
        cm1 = CoordinateMatrix3D(0, 1, 0, 1, 0, 1, Coordinate3D(0, 0, 0))
        cm2 = CoordinateMatrix3D(0, 1, 0, 1, 0, 1, Coordinate3D(0, 0, 0))
        self.assertEqual(cm1, cm2)
    
    def test_from_string(self):
        cm = CoordinateMatrix3D.from_string("(0, 2, 0, 2, 0, 2)^[2, 3, 4]")
        self.assertEqual(cm.minX, 0)
        self.assertEqual(cm.maxX, 2)
        self.assertEqual(cm.minY, 0)
        self.assertEqual(cm.maxY, 2)
        self.assertEqual(cm.minZ, 0)
        self.assertEqual(cm.maxZ, 2)
        self.assertEqual(cm.start, Coordinate3D(2, 3, 4))