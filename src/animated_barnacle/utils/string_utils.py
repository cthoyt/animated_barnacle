"""Functions for mutating strings.

This module contains string mutation functions
relevant for fake DNA and protein language models.
"""


def strip_atc(s: str):
    """Strip ATC from string."""
    return s.removeprefix("atc")


def add_ggg(s: str):
    """Add GGG to the end the string."""
    return s + "ggg"
