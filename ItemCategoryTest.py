import unittest

from ItemCategory import ItemCategory


class ItemCategoryTest(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        self.category1 = ItemCategory('Drone')
        self.category2 = ItemCategory('Part')
        self.category3 = ItemCategory('Instrument')

    def test_init(self):
        self.assertEqual(type(self.category1), ItemCategory)
        self.assertEqual(type(self.category2), ItemCategory)
        self.assertEqual(type(self.category3), ItemCategory)

    def test_get_name(self):
        self.assertEqual(self.category1.get_name(), 'Drone')
        self.assertEqual(self.category2.get_name(), 'Part')
        self.assertEqual(self.category3.get_name(), 'Instrument')

    def test_set_name(self):
        self.category1.set_name('TestName1')
        self.category2.set_name('TestName2')
        self.category3.set_name('TestName3')

        self.assertEqual(self.category1.get_name(), 'TestName1')
        self.assertEqual(self.category2.get_name(), 'TestName2')
        self.assertEqual(self.category3.get_name(), 'TestName3')

    def test_str(self):
        self.assertEqual(str(self.category1), 'Drone')
        self.assertEqual(str(self.category2), 'Part')
        self.assertEqual(str(self.category3), 'Instrument')

        self.category1.set_name('TestName1')
        self.category2.set_name('TestName2')
        self.category3.set_name('TestName3')

        self.assertEqual(str(self.category1), 'TestName1')
        self.assertEqual(str(self.category2), 'TestName2')
        self.assertEqual(str(self.category3), 'TestName3')
