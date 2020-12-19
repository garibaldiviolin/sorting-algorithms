from unittest import TestCase

from algorithms.selection_sort import selection_sort
from tests.timed_tests import TimedSortingTestCase


class SelectionSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(selection_sort)
