from unittest import TestCase

from algorithms.insertion_sort import insertion_sort
from tests.timed_tests import TimedSortingTestCase


class InsertionSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(insertion_sort)
