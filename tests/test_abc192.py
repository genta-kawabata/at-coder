# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc192.a.main as a
import abc192.b.main as b
import abc192.c.main as c
import abc192.d.main as d
import abc192.e.main as e
import abc192.f.main as f


class Test_abc192_c(TestCase):

    def test_get_answer_term_0(self):
        N, K = 0, 0
        self.assertEqual(0, c.get_answer(N, K))

    def test_get_answer_term_1(self):
        N, K = int(1e9), int(1e5)
        self.assertEqual(0, c.get_answer(N, K))

    def test_sample_1(self):
        N, K = 314, 2
        self.assertEqual(693, c.get_answer(N, K))

    def test_sample_2(self):
        N, K =1000000000, 100
        self.assertEqual(0, c.get_answer(N, K))

    def test_sample_3(self):
        N, K = 6174, 100000
        self.assertEqual(6174, c.get_answer(N, K))


class Test_abc192_d(TestCase):

    def test_get_answer_sample_1(self):
        X = "22"
        M = 10
        self.assertEqual(2, d.get_answer(X, M))

    def test_get_answer_sample_2(self):
        X = "999"
        M = 1500
        self.assertEqual(3, d.get_answer(X, M))

    def test_get_answer_sample_3(self):
        X = "100000000000000000000000000000000000000000000000000000000000"
        M = 1000000000000000000
        self.assertEqual(1, d.get_answer(X, M))

    def test_get_answer_big_1(self):
        # temp = "1234567890"
        temp = "1000000000"
        X = temp
        for _ in range(6 - 1):
            # X += temp
            X += "0000000000"

        M = int(1e18)
        self.assertEqual(1, d.get_answer(X, M))

    def test_get_answer_min_1(self):
        X = "1"
        M = int(1e18)
        self.assertEqual(1, d.get_answer(X, M))

    def test_get_answer_x_1_m_10(self):
        X = "1"
        M = 10
        self.assertEqual(1, d.get_answer(X, M))
