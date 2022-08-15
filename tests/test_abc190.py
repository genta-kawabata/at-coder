# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc190.a.main as a
import abc190.b.main as b
import abc190.c.main as c
import abc190.d.main as d
import abc190.e.main as e
import abc190.f.main as f


class Test_abc190_c(TestCase):

    def test_get_answer_1(self):
        N = 4
        M = 4
        L_A = [1, 1, 2, 3]
        L_B = [2, 3, 4, 4]
        K = 3
        L_C = [1, 1, 2]
        L_D = [2, 3, 3]

        self.assertEqual(2, c.get_answer(N, M, K, L_A, L_B, L_C, L_D))

    def test_get_answer_1(self):
        import random
        N = 100
        M = 100
        L_A = [random.randrange(1, N) for _ in range(M)]
        L_B = [random.randrange(1, N) for _ in range(M)]
        K = 16
        L_C = [random.randrange(1, N) for _ in range(K)]
        L_D = [random.randrange(1, N) for _ in range(K)]

        self.assertTrue(True)

    def test_dec_to_bin_7(self):
        result = c.dec_to_bin(7, 3)
        self.assertEqual([1, 1, 1], result)

    def test_dec_to_bin_3(self):
        result = c.dec_to_bin(3, 3)
        self.assertEqual([0, 1, 1], result)

    def test_dec_to_bin_6(self):
        result = c.dec_to_bin(6, 3)
        self.assertEqual([1, 1, 0], result)


class Test_abc190_b(TestCase):

    def test_get_answer_1(self):
        N = 100
        S = pow(10, 9)
        D = pow(10, 9)

        import random

        L_X = [random.randrange(1, pow(10, 9)) for _ in range(100)]
        L_Y = [random.randrange(1, pow(10, 9)) for _ in range(100)]

        print(b.get_answer(N, S, D, L_X, L_Y))

        self.assertTrue(True)
