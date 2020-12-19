from unittest import TestCase

from algorithms.bubble_sort import bubble_sort
from tests.timed_tests import TimedSortingTestCase


class IteractiveBubbleSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(bubble_sort)
