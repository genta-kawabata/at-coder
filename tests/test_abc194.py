# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc194.a.main as a
import abc194.b.main as b
import abc194.c.main as c
import abc194.d.main as d
import abc194.e.main as e
import abc194.f.main as f


class Test_abc194_b(TestCase):

    def test_get_answer_1(self):
        pass


class Test_abc194_c(TestCase):

    def test_get_answer_1(self):
        import random

        N = 3 * int(1e5)
        L_A = [random.randrange(0, 200, 1) for _ in range(N)]

        ans = c.get_answer(N, L_A)

        self.assertTrue(True)


class Test_abc194_d(TestCase):

    def test_get_answer_2(self):
        N = 2

        ans = d.get_answer(N)

        exp = 2
        self.assertTrue(exp - 1e-6 <= ans <= exp + 1e-6)

    def test_get_answer_3(self):
        N = 3

        ans = d.get_answer(N)

        exp = 4.5
        a1 = exp - 1e-6

        self.assertTrue(exp - 1e-6 <= ans <= exp + 1e-6)
