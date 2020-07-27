import unittest
from distances import calculate_distances
from unittest.mock import patch

class TestAirroutes(unittest.TestCase):

    def test_calculate_distances(self):
        row = {'Departure_lat': 51.5, 'Departure_lon': -0.45, 'Arrival_lat': 40.64, 'Arrival_lon': -73.79}
        nm = calculate_distances(row)
        self.assertEqual(str(nm['NM']), '2999.48')

        row = {'Departure_lat': 51.5, 'Departure_lon': -0.45, 'Arrival_lat': 35.75, 'Arrival_lon': 140.39}
        nm = calculate_distances(row)
        self.assertEqual(str(nm['NM']), '5190.94')

        row = {'Departure_lat': 1.3, 'Departure_lon': 103.98, 'Arrival_lat': 22.32, 'Arrival_lon': 113.94}
        nm = calculate_distances(row)
        self.assertEqual(str(nm['NM']), '1384.12')


if __name__ == "__main__":
    unittest.main()