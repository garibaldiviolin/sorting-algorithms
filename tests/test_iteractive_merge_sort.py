from unittest import TestCase

from algorithms.iteractive_merge_sort import iteractive_merge_sort
from tests.timed_tests import TimedSortingTestCase


class IteractiveMergeSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(iteractive_merge_sort)
