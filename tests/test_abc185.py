# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc185.a.main as a
import abc185.b.main as b
import abc185.c.main as c
import abc185.d.main as d
import abc185.e.main as e
import abc185.f.main as f


class Test_abc185_c(TestCase):

    def test_get_answer_200(self):
        L = 200
        self.assertEqual(366461620334848584, c.get_answer(L))

    def test_get_answer_12(self):
        L = 12
        self.assertEqual(1, c.get_answer(L))

    def test_get_answer_14(self):
        L = 14
        self.assertEqual(78, c.get_answer(L))

    def test_get_answer_20(self):
        L = 20
        self.assertEqual(75582, c.get_answer(L))
