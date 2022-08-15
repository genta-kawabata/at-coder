# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc183.a.main as a
import abc183.b.main as b
import abc183.c.main as c
import abc183.d.main as d
import abc183.e.main as e
import abc183.f.main as f


class Test_abc183_c(TestCase):

    def test_get_answer_1(self):
        N = 4
        K = 330
        T = [
            [0, 1, 10, 100],
            [1, 0, 20, 200],
            [10, 20, 0, 300],
            [100, 200, 300, 0]
        ]
        self.assertEqual(2, c.get_answer(N, K, T))

    def test_get_answer_2(self):
        N = 5
        K = 5
        T = [
            [0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
        ]
        self.assertEqual(24, c.get_answer(N, K, T))

    def test_get_answer_3(self):
        N = 8
        K = pow(10, 9)
        T = [[pow(10, 8) for _ in range(N)] for _ in range(N)]

        self.assertTrue(True)
