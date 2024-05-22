from levelz import Dimension, Scroll, Level2D, Level3D
import unittest

class TestLevel2D(unittest.TestCase):
    def test_level2d(self):
        l1 = Level2D()
        self.assertEqual(l1.dimension, Dimension.TWO)
        self.assertEqual(l1.blocks, [])

        l2 = Level2D({"scroll": "horizontal-left"}, [])
        self.assertEqual(l2.dimension, Dimension.TWO)
        self.assertEqual(l2.blocks, [])
        self.assertEqual(l2.scroll, Scroll.HORIZONTAL_LEFT)

class TestLevel3D(unittest.TestCase):
    def test_level3d(self):
        l1 = Level3D()
        self.assertEqual(l1.dimension, Dimension.THREE)
        self.assertEqual(l1.blocks, [])