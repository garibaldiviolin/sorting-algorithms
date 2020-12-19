from unittest import TestCase

from algorithms.recursive_merge_sort import recursive_merge_sort
from tests.timed_tests import TimedSortingTestCase


class RecursiveMergeSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(recursive_merge_sort)
