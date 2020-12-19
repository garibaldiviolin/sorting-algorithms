from unittest import TestCase

from algorithms.shell_sort import shell_sort
from tests.timed_tests import TimedSortingTestCase


class ShellSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(shell_sort)
