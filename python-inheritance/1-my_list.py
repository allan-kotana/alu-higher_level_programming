#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """Class that inherits from list and adds print_sorted."""

    def print_sorted(self):
        """Print the list elements sorted in ascending order."""
        print(sorted(self))
