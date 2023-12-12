import unittest

from Box import Box
from Item import Item
from ItemCategory import ItemCategory


class ItemTest(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        box = Box(12, 3, 4)
        self.item1 = Item('test1', 23, 12.2, box, ItemCategory('TestCat1'))
        self.item2 = Item('test2', 34.4, 33, box, ItemCategory('TestCat2'))
        self.item3 = Item('test3', 1, 1, box, ItemCategory('TestCat3'))

    def test_init(self):
        self.assertEqual(type(self.item1), Item)
        self.assertEqual(type(self.item2), Item)
        self.assertEqual(type(self.item3), Item)

    def test_get_name(self):
        self.assertEqual(self.item1.get_name(), 'test1')
        self.assertEqual(self.item2.get_name(), 'test2')
        self.assertEqual(self.item3.get_name(), 'test3')

    def test_get_cost(self):
        self.assertEqual(self.item1.get_cost(), 23)
        self.assertEqual(self.item2.get_cost(), 34.4)
        self.assertEqual(self.item3.get_cost(), 1)

    def test_get_weight(self):
        self.assertEqual(self.item1.get_weight(), 12.2)
        self.assertEqual(self.item2.get_weight(), 33)
        self.assertEqual(self.item3.get_weight(), 1)

    def test_get_box(self):
        self.assertEqual(self.item1.get_box().get_width(), 12)
        self.assertEqual(self.item1.get_box().get_length(), 3)
        self.assertEqual(self.item1.get_box().get_height(), 4)

        self.assertEqual(self.item2.get_box().get_width(), 12)
        self.assertEqual(self.item2.get_box().get_length(), 3)
        self.assertEqual(self.item2.get_box().get_height(), 4)

        self.assertEqual(self.item3.get_box().get_width(), 12)
        self.assertEqual(self.item3.get_box().get_length(), 3)
        self.assertEqual(self.item3.get_box().get_height(), 4)

    def test_get_category(self):
        self.assertEqual(self.item1.get_category().get_name(), "TestCat1")
        self.assertEqual(self.item2.get_category().get_name(), "TestCat2")
        self.assertEqual(self.item3.get_category().get_name(), "TestCat3")

    def test_set_name(self):
        self.item1.set_name("1")
        self.item2.set_name("2")
        self.item3.set_name("3")

        self.assertEqual(self.item1.get_name(), "1")
        self.assertEqual(self.item2.get_name(), "2")
        self.assertEqual(self.item3.get_name(), "3")

    def test_set_cost(self):
        self.item1.set_cost(111)
        self.item2.set_cost(222)
        self.item3.set_cost(333)

        self.assertEqual(self.item1.get_cost(), 111)
        self.assertEqual(self.item2.get_cost(), 222)
        self.assertEqual(self.item3.get_cost(), 333)

    def test_set_weight(self):
        self.item1.set_weight(1.1)
        self.item2.set_weight(2.2)
        self.item3.set_weight(3.3)

        self.assertEqual(self.item1.get_weight(), 1.1)
        self.assertEqual(self.item2.get_weight(), 2.2)
        self.assertEqual(self.item3.get_weight(), 3.3)

    def test_set_box(self):
        self.item1.set_box(Box(1, 1, 1))
        self.item2.set_box(Box(2.2, 2.2, 2.2))
        self.item3.set_box(Box(3, 3, 3))

        self.assertEqual(self.item1.get_box().get_width(), 1)
        self.assertEqual(self.item1.get_box().get_length(), 1)
        self.assertEqual(self.item1.get_box().get_height(), 1)

        self.assertEqual(self.item2.get_box().get_width(), 2.2)
        self.assertEqual(self.item2.get_box().get_length(), 2.2)
        self.assertEqual(self.item2.get_box().get_height(), 2.2)

        self.assertEqual(self.item3.get_box().get_width(), 3)
        self.assertEqual(self.item3.get_box().get_length(), 3)
        self.assertEqual(self.item3.get_box().get_height(), 3)

    def test_set_category(self):
        self.item1.set_category(ItemCategory('T1'))
        self.item2.set_category(ItemCategory('T2'))
        self.item3.set_category(ItemCategory('T3'))

        self.assertEqual(self.item1.get_category().get_name(), 'T1')
        self.assertEqual(self.item2.get_category().get_name(), 'T2')
        self.assertEqual(self.item3.get_category().get_name(), 'T3')

    def test_str(self):
        self.assertEqual(str(self.item1), 'Name: test1 of TestCat1 category, Cost: 23, Weight: 12.2')
        self.assertEqual(str(self.item2), 'Name: test2 of TestCat2 category, Cost: 34.4, Weight: 33')
        self.assertEqual(str(self.item3), 'Name: test3 of TestCat3 category, Cost: 1, Weight: 1')

        self.item1.set_name("1")
        self.item1.set_category(ItemCategory("T1"))
        self.item1.set_cost(1)
        self.item1.set_weight(1.1)

        self.item2.set_name("2")
        self.item2.set_category(ItemCategory("T2"))
        self.item2.set_cost(2)
        self.item2.set_weight(2.2)

        self.item3.set_name("3")
        self.item3.set_category(ItemCategory("T3"))
        self.item3.set_cost(3)
        self.item3.set_weight(3.3)

        self.assertEqual(str(self.item1), 'Name: 1 of T1 category, Cost: 1, Weight: 1.1')
        self.assertEqual(str(self.item2), 'Name: 2 of T2 category, Cost: 2, Weight: 2.2')
        self.assertEqual(str(self.item3), 'Name: 3 of T3 category, Cost: 3, Weight: 3.3')

