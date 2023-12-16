import unittest
from Address import Address


class AddressTest(unittest.TestCase):

    def test_str(self):
        address = Address("Koszykowa 86", "02-008", "Warszawa", "Polska", "225844500")
        self.assertEqual(address.__str__(), "Koszykowa 86, 02-008, Warszawa, Polska, 225844500")


if __name__ == '__main__':
    unittest.main()
