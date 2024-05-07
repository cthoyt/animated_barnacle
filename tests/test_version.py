"""Trivial version test."""

import unittest

from animated_barnacle.utils.string_utils import add_ggg


class TestStringUtils(unittest.TestCase):
    """Test string utilties."""

    def test_add_ggg(self):
        """Test the add_ggg function."""
        self.assertEqual("cthggg", add_ggg("cth"))
