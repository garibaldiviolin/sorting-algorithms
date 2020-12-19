from time import monotonic


class TimedTestCase:
    def setUp(self):
        self.reversed_list_tests = [
            (list(reversed(range(length))), list(range(length)))
            for length in range(10, 1000, 100)  # reversed
        ]
        self.sorted_list_tests = [
            (list(range(length)), list(range(length)))
            for length in range(10, 1000, 100)  # already sorted
        ]

        self.start_time = monotonic()

    def tearDown(self):
        t = monotonic() - self.start_time
        print(f"{self.id()}: {t:.10f}")


class TimedSortingTestCase(TimedTestCase):
    algorithm = None  # must be set in the subclass

    def call_sorting_tests(self, tests_cases):
        for initial_list, expected_sorted_list in tests_cases:
            with self.subTest(
                initial_list=initial_list,
                expected_sorted_list=expected_sorted_list
            ):
                self.assertListEqual(
                    self.algorithm(initial_list), expected_sorted_list
                )

    def test_sorting_reversed_lists(self):
        self.call_sorting_tests(self.reversed_list_tests)

    def test_sorting_already_sorted_lists(self):
        self.call_sorting_tests(self.sorted_list_tests)
