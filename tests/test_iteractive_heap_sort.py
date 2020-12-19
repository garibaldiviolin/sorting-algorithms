from unittest import TestCase

from algorithms.iteractive_heap_sort import iteractive_heap_sort
from tests.timed_tests import TimedSortingTestCase


class IteractiveHeapSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(iteractive_heap_sort)
