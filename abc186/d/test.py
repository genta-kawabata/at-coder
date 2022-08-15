# -*- coding: utf-8 -*-

from unittest import TestCase

import contests.abc186.d.main as main
from tests.utils import MyTimer


class Test(TestCase):

    def test_sort(self):
        L_A = [5, 1, 2]

        L_A.sort()

        self.assertEqual(
            [1, 2, 5],
            L_A
        )

    def test_get_cumulative_sum_1(self):
        L_A = [1, 2, 5]

        exp = [0, 1, 3, 8]
        act = main.get_cumulative_sum_sequential(L_A)

        self.assertEqual(exp, act)

    def test_get_cumulative_sum_2(self):
        L_A = [-2, 0, 3, 9, 15, 26]

        exp = [0, -2, -2, 1, 10, 25, 51]
        act = main.get_cumulative_sum_sequential(L_A)

        self.assertEqual(exp, act)

    def test_get_cumulative_sum_3(self):
        L_A = [1, 6, 3, 8, 4, 2, 9, 5, 7]

        exp = [0, 1, 7, 10, 18, 22, 24, 33, 38, 45]
        act = main.get_cumulative_sum_sequential(L_A)

        self.assertEqual(exp, act)

    def test_get_cumulative_sum_unsorted(self):
        L_A_orig = [5, 3, 8, 2, 9, 1]
        L_A = L_A_orig.copy()

        exp = [0, 5, 8, 16, 18, 27, 28]


        timer: MyTimer = MyTimer()
        timer.start()
        act = main.get_cumulative_sum_sequential(L_A)
        timer.stop()
        print(timer.message)

        with self.subTest(name="CumulativeSum"):
            self.assertEqual(exp, act)
        with self.subTest(name="ComparisonListBeforeAfter"):
            self.assertEqual(L_A_orig, L_A)

    def test_get_answer_measure_time(self):
        import random

        N = 2 * pow(10, 5)

        L_A = []
        for i in range(N):
            L_A.append(random.randint(0, pow(10, 8)))

        timer = MyTimer()
        timer.start()

        # ans = main._get_answer_primitive(L_A)
        ans = main._get_answer_cumulative(L_A)

        timer.stop()
        print(timer.message)

        self.assertTrue(True)
