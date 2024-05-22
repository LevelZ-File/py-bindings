from levelz import Level2D, Level3D, Scroll, parse_lines, parse_file, parse_level
import unittest

class TestParser2D(unittest.TestCase):
    def test_parse_lines(self):
        l1 = [
            "@type 2",
            "@spawn [0, -1]",
            "@scroll horizontal-left",
            "---",
            "grass: [0, 0]*[0, -1]"
        ]
        l1o = parse_lines(l1)

        self.assertTrue(isinstance(l1o, Level2D))
        self.assertEqual(l1o.dimension, 2)
        self.assertEqual(l1o.scroll, Scroll.HORIZONTAL_LEFT) # type: ignore
        self.assertEqual(l1o.spawn, [0, -1])
        self.assertEqual(len(l1o.blocks), 2)

        l2 = [
            "@type 2",
            "@spawn default",
            "---",
            "grass: [0, 0]*[0, -1]",
            "stone: [1, 1]*[0, -1]*(0, 3, 0, 3)^[5, 5]"
        ]
        l2o = parse_lines(l2)

        self.assertTrue(isinstance(l2o, Level2D))
        self.assertEqual(l2o.dimension, 2)
        self.assertEqual(l2o.scroll, Scroll.NONE) # type: ignore
        self.assertEqual(l2o.spawn, [0, 0])
        self.assertEqual(len(l2o.blocks), 20)


    def test_parse_file(self):
        f1 = "test/examples/2D/grasslands/1.lvlz"
        l1 = parse_file(f1)

        self.assertTrue(isinstance(l1, Level2D))
        self.assertEqual(l1.dimension, 2)
        self.assertEqual(l1.scroll, Scroll.NONE) # type: ignore
        self.assertEqual(l1.spawn, [0, 0])
        self.assertEqual(len(l1.blocks), 10)

        f2 = "test/examples/2D/grasslands/2.lvlz"
        l2 = parse_file(f2)

        self.assertTrue(isinstance(l2, Level2D))
        self.assertEqual(l2.dimension, 2)
        self.assertEqual(l2.scroll, Scroll.NONE) # type: ignore
        self.assertEqual(l2.spawn, [0, 0])
        self.assertEqual(len(l2.blocks), 8)

        f3 = "test/examples/2D/volcano/2.lvlz"
        l3 = parse_file(f3)

        self.assertTrue(isinstance(l3, Level2D))
        self.assertEqual(l3.dimension, 2)
        self.assertEqual(l3.scroll, Scroll.NONE) # type: ignore
        self.assertEqual(l3.spawn, [-5, 0])
        self.assertEqual(len(l3.blocks), 12)

        f4 = "test/examples/2D/volcano/3.lvlz"
        l4 = parse_file(f4)

        self.assertTrue(isinstance(l4, Level2D))
        self.assertEqual(l4.dimension, 2)
        self.assertEqual(l4.scroll, Scroll.HORIZONTAL_LEFT) # type: ignore
        self.assertEqual(l4.spawn, [15, 0])
        self.assertEqual(len(l4.blocks), 42)

        f5 = "test/examples/3D/grasslands/1.lvlz"
        l5 = parse_file(f5)

        self.assertTrue(isinstance(l5, Level3D))
        self.assertEqual(l5.dimension, 3)
        self.assertEqual(l5.spawn, [0, 0, 0])
        self.assertEqual(len(l5.blocks), 222)

        f6 = "test/examples/3D/grasslands/2.lvlz"
        l6 = parse_file(f6)

        self.assertTrue(isinstance(l6, Level3D))
        self.assertEqual(l6.dimension, 3)
        self.assertEqual(l6.spawn, [4, 6, 2])
        self.assertEqual(len(l6.blocks), 501)

    def test_parse_level(self):
        l1 = "@type 3\n@spawn [0, -1, 2]\n---\ngrass: [0, 0, 0]*[0, -1, 2]\nend"
        l1o = parse_level(l1)

        self.assertTrue(isinstance(l1o, Level3D))
        self.assertEqual(l1o.dimension, 3)
        self.assertEqual(l1o.spawn, [0, -1, 2])
        self.assertEqual(len(l1o.blocks), 2)