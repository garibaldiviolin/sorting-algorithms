from unittest import TestCase

from tests.timed_tests import TimedSortingTestCase


class StandardPythonSortTestCase(TimedSortingTestCase, TestCase):
    algorithm = staticmethod(sorted)
