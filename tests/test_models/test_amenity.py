#!/usr/bin/python3
"""Amenity test for testing Amenity"""


import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Nice"

    def test_type(self):
        self.assertIsInstance(Amenity.name, str)

    def test_name(self):
        self.assertEqual(self.amenity.name, "Nice")
