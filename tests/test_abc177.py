# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc177.a.main as a
import abc177.b.main as b
import abc177.c.main as c
import abc177.d.main as d
import abc177.e.main as e
import abc177.f.main as f


class Test_abc177_c(TestCase):

    def test_get_answer_1(self):
        N = 2
        L_A = [1, 3]
        self.assertEqual(3, c.get_answer(N, L_A))

    def test_get_answer_2(self):
        N = int(2 * 1e5)
        L_A = [rd.randrange(int(1e8), int(1e9), 1) for _ in range(N)]
        ans = c.get_answer(N, L_A)
        self.assertTrue(True)

    def test_get_answer_3(self):
        N = 3
        L_A = [1, 2, 3]
        self.assertEqual(11, c.get_answer(N, L_A))
