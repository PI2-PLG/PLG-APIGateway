import unittest
from unittest.mock import patch, Mock
#Class used to mock the values passed from atmosphericdata.py
import atmosphericdata

class TestAtmosphere(unittest.TestCase):
    def test_atmospheric_data(self):
        mock_atmosphere = Mock()
        atmosphericdata.atmospheric(1,1,34,409,0.75,-12.238877,-43.963241)

    def test_atmospheric_data2(self):
        mock_atmosphere = Mock()
        atmosphericdata.atmospheric(2,2,30,402,0.50,-72.244877,-83.213241)


if __name__ == '__main__':
    unittest.main()
