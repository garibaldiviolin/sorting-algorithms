from time import monotonic


class TimedTestCase:
    def setUp(self):
        self.tests = [
            (list(reversed(range(length))), list(range(length)))
            for length in range(10, 1000, 100)  # reversed
        ] + [
            (list(range(length)), list(range(length)))
            for length in range(10, 1000, 100)  # already sorted
        ]

        self.start_time = monotonic()

    def tearDown(self):
        t = monotonic() - self.start_time
        print(f"{self.id()}: {t:.10f}")


class TimedSortingTestCase(TimedTestCase):
    algorithm = None  # must be set in the subclass

    def test_sorting(self):
        for initial_list, expected_sorted_list in self.tests:
            with self.subTest(
                initial_list=initial_list,
                expected_sorted_list=expected_sorted_list
            ):
                self.assertListEqual(
                    self.algorithm(initial_list), expected_sorted_list
                )
