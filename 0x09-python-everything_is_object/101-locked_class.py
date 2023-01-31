#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Only allows instatiation of an attr called first_name
    """

    __slots__ = ["first_name"]
