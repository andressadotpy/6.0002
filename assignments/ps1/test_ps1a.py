import unittest
from unittest.mock import patch, mock_open

from ps1a import load_cows, greedy_cow_transport, brute_force_cow_transport

class TestFile(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Foo,5\n')
    def test_loading_a_file(self, mock_file):
        cows = load_cows(mock_file)
        self.assertEqual(cows, {'Foo':5})

    @patch('builtins.open', new_callable=mock_open, read_data='Foo,5\nBar,3\n')
    def test_loading_a_file_with_more_than_one_cow(self, mock_file):
        cows = load_cows(mock_file)
        self.assertEqual(cows, {'Foo':5, 'Bar':3})

class TestGreedyAlgorithm(unittest.TestCase):

    def test_greedy_algorithm(self):
        cows = {'Jesse':6,
                'Maybel':3,
                'Callie':2,
                'Maggie':5}
        trips = greedy_cow_transport(cows)
        self.assertEqual(trips, [['Jesse', 'Maybel'],
                                ['Maggie', 'Callie']])

    def test_greedy_algorithm_2(self):
        cows = {'Betsy': 9,
                'Oreo': 6,
                'Herman': 7,
                'Florence': 2,
                'Maggie': 3,
                'Moo Moo': 3,
                'Milkshake': 2,
                'Lola': 2,
                'Millie': 5,
                'Henrietta': 9}
        trips = greedy_cow_transport(cows)
        self.assertEqual(trips,
                        [['Betsy'], ['Henrietta'], ['Herman', 'Maggie'],
                        ['Oreo', 'Moo Moo'],
                        ['Millie', 'Florence','Milkshake'],
                        ['Lola']])

class TestBruteForceCowTransport(unittest.TestCase):


    @unittest.skip
    def test_brute_force_cow_transport(self):
        cows = {'Jesse': 6,
                'Maybel': 3,
                'Callie': 2,
                'Maggie': 5}
        trips = brute_force_cow_transport(cows)
        self.assertEqual(trips, [['Callie', 'Maybel', 'Maggie'], ['Jesse']])
