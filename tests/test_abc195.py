# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc195.a.main as a
import abc195.b.main as b
import abc195.c.main as c
import abc195.d.main as d
import abc195.e.main as e
import abc195.f.main as f


class Test_abc195_b(TestCase):

    def test_get_answer_1(self):
        pass


class Test_abc195_c(TestCase):

    def test_get_answer_1010(self):
        N = 1010

        self.assertEqual(11, c.get_answer(N))

    def test_get_answer_27182818284590(self):
        N = 27182818284590

        self.assertEqual(107730272137364, c.get_answer(N))

    def test_get_answer_123456(self):
        N = 123456
        c.get_answer(N)
        self.assertTrue(True)

    def test_get_total_num_comma_4(self):
        keta = 4
        self.assertEqual(9000, c.get_total_num_comma(keta))

    def test_get_total_num_comma_5(self):
        keta = 5
        self.assertEqual(99000, c.get_total_num_comma(keta))

    def test_get_total_num_comma_13(self):
        keta = 13
        self.assertEqual(99000, c.get_total_num_comma(keta))



class Test_abc195_d(TestCase):

    def test_get_answer_1(self):
        pass
