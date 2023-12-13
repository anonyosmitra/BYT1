import unittest

from Box import Box


class BoxTest(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        self.box1 = Box(12, 12.5, 3)
        self.box2 = Box(2, 3, 3.66)
        self.box3 = Box(5, 1.23, 4)

    def test_get_width(self):
        self.assertEqual(self.box1.get_width(), 12)
        self.assertEqual(self.box2.get_width(), 2)
        self.assertEqual(self.box3.get_width(), 5)

    def test_get_height(self):
        self.assertEqual(self.box1.get_height(), 3)
        self.assertEqual(self.box2.get_height(), 3.66)
        self.assertEqual(self.box3.get_height(), 4)

    def test_get_length(self):
        self.assertEqual(self.box1.get_length(), 12.5)
        self.assertEqual(self.box2.get_length(), 3)
        self.assertEqual(self.box3.get_length(), 1.23)

    def test_init(self):
        self.assertEqual(type(self.box1), Box)
        self.assertEqual(type(self.box2), Box)
        self.assertEqual(type(self.box3), Box)

    def test_set_width(self):
        self.assertTrue(self.box1.set_width(1))
        self.assertFalse(self.box2.set_width(-1))
        self.assertTrue(self.box3.set_width(8))

        self.assertEqual(self.box1.get_width(), 1)
        self.assertEqual(self.box2.get_width(), 2)
        self.assertEqual(self.box3.get_width(), 8)

    def test_set_height(self):
        self.assertTrue(self.box1.set_height(1))
        self.assertFalse(self.box2.set_height(-1))
        self.assertTrue(self.box3.set_height(8))

        self.assertEqual(self.box1.get_height(), 1)
        self.assertEqual(self.box2.get_height(), 3.66)
        self.assertEqual(self.box3.get_height(), 8)

    def test_set_length(self):
        self.assertTrue(self.box1.set_length(1))
        self.assertFalse(self.box2.set_length(-1))
        self.assertTrue(self.box3.set_length(8))

        self.assertEqual(self.box1.get_length(), 1)
        self.assertEqual(self.box2.get_length(), 3)
        self.assertEqual(self.box3.get_length(), 8)

    def test_volume(self):
        self.assertEqual(self.box1.volume(), 450)
        self.assertEqual(self.box2.volume(), 21.96)
        self.assertEqual(self.box3.volume(), 24.6)

        self.box1.set_width(1)
        self.box2.set_length(1)
        self.box3.set_height(1)

        self.assertEqual(self.box1.volume(), 37.5)
        self.assertEqual(self.box2.volume(), 7.32)
        self.assertEqual(self.box3.volume(), 6.15)

    def test_isValid(self):
        self.assertTrue(self.box1.is_valid())
        self.assertTrue(self.box2.is_valid())
        self.assertTrue(self.box3.is_valid())

        self.assertFalse(Box(-1, 1, 1).is_valid())
        self.assertFalse(Box(1, -1, 1).is_valid())
        self.assertFalse(Box(1, 1, -1).is_valid())
        self.assertFalse(Box(-1, -1, 1).is_valid())
        self.assertFalse(Box(-1, 1, -1).is_valid())
        self.assertFalse(Box(1, -1, -1).is_valid())
        self.assertFalse(Box(-1, -1, -1).is_valid())
