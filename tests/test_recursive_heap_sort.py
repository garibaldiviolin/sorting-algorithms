from unittest import TestCase

from algorithms.recursive_heap_sort import recursive_heap_sort
from tests.timed_tests import TimedSortingTestCase


class RecursiveHeapSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(recursive_heap_sort)
