from unittest import TestCase

from algorithms.recursive_quick_sort import recursive_quick_sort
from tests.timed_tests import TimedSortingTestCase


class RecursiveQuickSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(recursive_quick_sort)
