# -*- coding: utf-8 -*-

from unittest import TestCase

from .main import dp


class Test(TestCase):

    def test_fail(self):
        pass

    def test_dp_1(self):
        l_a = []
        l_b = []

        self.assertEqual(
            0,
            dp(l_a, l_b)
        )

    def test_dp_2(self):
        l_a = [3, 4, 2]
        l_b = []

        self.assertEqual(
            3,
            dp(l_a, l_b)
        )

    def test_dp_3(self):
        l_a = [3, 4, 2]
        l_b = [4, 2]

        self.assertEqual(
            1,
            dp(l_a, l_b)
        )

    def test_dp_4(self):
        l_a = [3, 3, 3, 3, 3]
        l_b = [5, 5, 5, 5, 5]

        self.assertEqual(
            5,
            dp(l_a, l_b)
        )

    def test_dp_sample1(self):
        l_a = [1, 2, 1, 3]
        l_b = [1, 3, 1]

        self.assertEqual(
            2,
            dp(l_a, l_b)
        )

    def test_dp_sample2(self):
        l_a = [1, 3, 2, 4]
        l_b = [1, 5, 2, 6, 4, 3]

        self.assertEqual(
            3,
            dp(l_a, l_b)
        )

    def test_dp_sample34(self):
        l_a = [1, 1, 1, 1, 1]
        l_b = [2, 2, 2, 2, 2]

        self.assertEqual(
            5,
            dp(l_a, l_b)
        )

