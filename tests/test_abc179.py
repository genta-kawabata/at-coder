# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc179.a.main as a
import abc179.b.main as b
import abc179.c.main as c
import abc179.d.main as d
import abc179.e.main as e
import abc179.f.main as f


class TestAbc179C_Kawa(TestCase):


    def test_get_answer_kawa_2(self):
        N = 2
        self.assertEqual(1, c.get_answer_kawa(N))

    def test_get_answer_kawa_3(self):
        N = 3
        self.assertEqual(3, c.get_answer_kawa(N))

    def test_get_answer_kawa_100(self):
        N = 100
        self.assertEqual(473, c.get_answer_kawa(N))

    def test_get_answer_kawa_1000000(self):
        N = 1000000
        self.assertEqual(13969985, c.get_answer_kawa(N))


class TestAbc179C_Example(TestCase):

    def test_get_answer_example_2(self):
        N = 2
        self.assertEqual(1, c.get_answer_example(N))

    def test_get_answer_example_3(self):
        N = 3
        self.assertEqual(3, c.get_answer_example(N))

    def test_get_answer_example_100(self):
        N = 100
        self.assertEqual(473, c.get_answer_example(N))

    def test_get_answer_example_1000000(self):
        N = 1000000
        self.assertEqual(13969985, c.get_answer_example(N))
