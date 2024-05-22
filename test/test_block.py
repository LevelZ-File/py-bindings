from levelz import Block, LevelObject, Coordinate2D, Coordinate3D
import unittest

class TestBlock(unittest.TestCase):
    def test_block(self):
        b = Block("grass")
        self.assertEqual(b.name, "grass")
        self.assertEqual(b.properties, {})
        self.assertEqual(str(b), "grass")
    
    def test_block_properties(self):
        b = Block("grass", {"color": "green", "height": 1})
        self.assertEqual(b.name, "grass")
        self.assertEqual(b.properties, {"color": "green", "height": 1})
        self.assertEqual(str(b), "grass<color=green, height=1>")

class TestLevelObject(unittest.TestCase):
    def test_level_object(self):
        l1 = LevelObject("stone", [0, 0])
        self.assertEqual(l1.block.name, "stone")
        self.assertEqual(l1.coordinate, Coordinate2D(0, 0))

        l2 = LevelObject(Block("dirt"), Coordinate3D(1, 2, 3))
        self.assertEqual(l2.block.name, "dirt")
        self.assertEqual(l2.coordinate, Coordinate3D(1, 2, 3))

        l3 = LevelObject("wood", [4, -5, 6.25])
        self.assertEqual(l3.block.name, "wood")
        self.assertEqual(l3.coordinate, Coordinate3D(4, -5, 6.25))
    
    def test_level_object_str(self):
        l1 = LevelObject("stone", [0, 0])
        self.assertEqual(str(l1), "stone: [0, 0]")

        l2 = LevelObject(Block("dirt"), Coordinate3D(1, 2, 3))
        self.assertEqual(str(l2), "dirt: [1, 2, 3]")

        l3 = LevelObject(Block("wood", {"type": "spruce"}), [-4, -15, 26.75])
        self.assertEqual(str(l3), "wood<type=spruce>: [-4, -15, 26.75]")
