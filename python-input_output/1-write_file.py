#!/usr/bin/python3
"""Module that defines the write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
