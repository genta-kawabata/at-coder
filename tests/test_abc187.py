# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc187.a.main as a
import abc187.b.main as b
import abc187.c.main as c
import abc187.d.main as d
import abc187.e.main as e
import abc187.f.main as f


class Test_abc187_c(TestCase):

    def test_get_answer_1(self):
        N = 10
        L_S = [
            "red",
            "red",
            "red",
            "!orange",
            "yellow",
            "!blue",
            "cyan",
            "!green",
            "brown",
            "!gray"
        ]
        self.assertEqual("satisfiable", c.get_answer_list(N, L_S))

    def test_get_answer_2(self):
        N = 11
        L_S = [
            "red",
            "red",
            "red",
            "!orange",
            "yellow",
            "!blue",
            "cyan",
            "!green",
            "brown",
            "!gray",
            "!red"
        ]
        self.assertEqual("red", c.get_answer_list(N, L_S))

    def test_get_answer_term_list(self):

        N = 2 * pow(10, 5)
        S = []
        for _ in range(N):
            S.append("aaaaaaaaa")
        
        self.assertEqual("satisfiable", c.get_answer_list(N, S))

    def test_get_answer_term_set(self):

        N = 2 * pow(10, 5)
        S = []
        for _ in range(N):
            S.append("aaaaaaaaa")
        
        S = set(S)

        self.assertEqual("satisfiable", c.get_answer_set(N, S))
