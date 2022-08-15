# -*- coding: utf-8 -*-

from unittest import TestCase
import random as rd

# import tests.utils as utils
# import utils

import abc191.a.main as a
import abc191.b.main as b
import abc191.c.main as c
import abc191.d.main as d
import abc191.e.main as e
import abc191.f.main as f


class Test_abc191_c(TestCase):

    # def test_count_balack_1(self):
    #     l_s = ".###."
    #     self.assertEqual(3, count_black(l_s))

    def test_get_answer_1(self):
        H = 5
        W = 5
        S = [
            ".....",
            ".###.",
            ".###.",
            ".###.",
            "....."
        ]

        self.assertEqual(4, c.get_answer(H, W, S))

    def test_get_answer_2(self):
        H = 5
        W = 5
        S = [
            ".....",
            ".#...",
            ".##..",
            ".###.",
            "....."
        ]

        self.assertEqual(8, c.get_answer(H, W, S))

    def test_get_answer_3(self):
        H = 5
        W = 7
        S = [
            ".......",
            "..##...",
            ".####..",
            ".####..",
            "......."
        ]

        self.assertEqual(8, c.get_answer(H, W, S))

    def test_get_answer_4(self):
        H = 9
        W = 13
        S = [
            ".............",
            "...######....",
            "..########...",
            ".##########..",
            ".#########...",
            "..#######....",
            "...#####.....",
            "....###......",
            "............."
        ]

        self.assertEqual(26, c.get_answer(H, W, S))

    def test_get_answer_5(self):
        H = 3
        W = 3
        S = [
            "...",
            ".#.",
            "..."
        ]

        self.assertEqual(4, c.get_answer(H, W, S))


    def test_get_answer_6(self):
        H = 10
        W = 10
        S = [
            "..........",
            ".#####....",
            ".####.....",
            ".###......",
            ".####.....",
            ".#####....",
            ".######...",
            ".#######..",
            ".########.",
            ".........."
        ]

        self.assertEqual(18, c.get_answer(H, W, S))


class Test_abc191_b(TestCase):

    def test_get_answer_1(self):
        N = 5
        X = 5
        A = [3, 5, 6, 5, 4]

        self.assertEqual("3 6 4", b.get_answer(N, X, A))
