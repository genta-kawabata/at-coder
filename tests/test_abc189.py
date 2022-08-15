# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc189.a.main as a
import abc189.b.main as b
import abc189.c.main as c
import abc189.d.main as d
import abc189.e.main as e
import abc189.f.main as f


class Test_abc189_c(TestCase):

    def test_get_answer_1(self):
        list_A = [2, 4, 4, 9, 4, 9]

        self.assertEqual(20, c.get_answer(list_A))

    def test_get_answer_2(self):
        list_A = [1]
        self.assertEqual(1, c.get_answer(list_A))

    def test_get_answer_3(self):
        list_A = [100000]
        self.assertEqual(100000, c.get_answer(list_A))

    def test_get_answer_4(self):
        list_A = [a % 100000 for a in range(10000)]
        self.assertEqual(1, c.get_answer(list_A))

    def test_get_answer_5(self):
        list_A = [100000]
        self.assertEqual(100000, c.get_answer(list_A))


class Test_abc189_b(TestCase):

    def test_get_answer_1(self):
        list_v = [(i * 100) % 1000 for i in range(1000)]
        list_p = [1 for i in range(1000)]
        x = 1000000

        a = b.get_answer(
            list_v, list_p, x
        )

        self.assertTrue(True)
