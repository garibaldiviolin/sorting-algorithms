from unittest import TestCase

from algorithms.iteractive_quick_sort import iteractive_quick_sort
from tests.timed_tests import TimedSortingTestCase


class IteractiveQuickSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(iteractive_quick_sort)
