# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

import main


class TestMain(TestCase):

    def test_get_n_q_from_stdin_IN_26_1000_OUT_26_1000(self):
        stdin = "26 1000"
        self.assertEqual(
            (26, 1000),
            main.get_n_q_from_stdin(stdin)
        )

    def test_get_n_q_from_stdin_IN_26_100_OUT_26_100(self):
        stdin = "26 100"
        self.assertEqual(
            (26, 100),
            main.get_n_q_from_stdin(stdin)
        )

    def test_get_n_q_from_stdin_IN_5_7_OUT_5_7(self):
        stdin = "5 7"
        self.assertEqual(
            (5, 7),
            main.get_n_q_from_stdin(stdin)
        )

    def test_get_char_list_IN_3_OUT_ABC(self):
        n = 3
        self.assertEqual(
            ['A', 'B', 'C'],
            main.get_char_list(n)
        )

    def test_get_char_list_IN_9_OUT_ABCDEFGHI(self):
        n = 9
        self.assertEqual(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            main.get_char_list(n)
        )

    def test_get_half_splitted_list_odd(self):
        in_list = ["A", "B", "C", "D", "E"]
        self.assertEqual(
            (["A", "B"], ["C", "D", "E"]),
            main.get_half_splitted_list(in_list)
        )

    def test_get_half_splitted_list_even(self):
        in_list = ["A", "B", "C", "D", "E", "F"]
        self.assertEqual(
            (["A", "B", "C"], ["D", "E", "F"]),
            main.get_half_splitted_list(in_list)
        )

    def test_get_half_splitted_list_empty(self):
        in_list = []
        self.assertEqual(
            ([], []),
            main.get_half_splitted_list(in_list)
        )

    def test_get_half_splitted_list_1(self):
        in_list = ["A"]
        self.assertEqual(
            (["A"], []),
            main.get_half_splitted_list(in_list)
        )

    @patch("builtins.input", lambda *args: "<")
    def test_input_patch_1value(self):
        self.assertEqual("<", main.ask(1, 2))

    @patch("builtins.input", side_effect=["<", ">"])
    def test_input_patch_2values(self, mock_input):
        self.assertEqual(
            ["<", ">"],
            [main.ask(1, 2), main.ask(1, 2)]
        )

    def test_insert_value_empty(self):
        v = "A"
        sorted_list = []
        self.assertEqual(
            ["A"],
            main.insert_value(v, sorted_list, main.ask)
        )

    @patch("builtins.input", side_effect=["<"])
    def test_insert_value_1value(self, mock_input):
        v = "A"
        sorted_list = ["B"]
        self.assertEqual(
            ["A", "B"],
            main.insert_value(v, sorted_list, main.ask)
        )

    @patch("builtins.input", side_effect=["<", ">"])
    def test_insert_value_2values(self, mock_input):
        v = "B"
        sorted_list = ["A", "C"]
        self.assertEqual(
            ["A", "B", "C"],
            main.insert_value(v, sorted_list, main.ask)
        )

    @patch("builtins.input", side_effect=["<", ">"])
    def test_get_answer_3_10(self, mock_input):
        stdin_n_q = "3 10"
        self.assertEqual(
            "! BAC",
            main.get_answer(stdin_n_q)
        )

    @patch("builtins.input", side_effect=["<", "<", ">", "<", ">", ">", ">"])
    def test_get_answer_5_7(self, mock_input):
        stdin_n_q = "5 7"
        self.assertEqual(
            "! BDCAE",
            main.get_answer(stdin_n_q)
        )

    def test_pop(self):
        in_list = ["A", "B", "C", "D"]
        self.assertEqual(
            ("B", ["A", "C", "D"]),
            (in_list.pop(1), in_list)
        )

    def test_get_split_top_left_right_0value(self):
        in_list = []
        self.assertEqual(
            ([], None, []),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_1value(self):
        in_list = ["A"]
        self.assertEqual(
            ([], "A", []),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_2values(self):
        in_list = ["A", "B"]
        self.assertEqual(
            (["A"], "B", []),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_3values(self):
        in_list = ["A", "B", "C"]
        self.assertEqual(
            (["A"], "B", ["C"]),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_4values(self):
        in_list = ["A", "B", "C", "D"]
        self.assertEqual(
            (["A", "B"], "C", ["D"]),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_5values(self):
        in_list = ["A", "B", "C", "D", "E"]
        self.assertEqual(
            (["A", "B"], "C", ["D", "E"]),
            main.get_split_top_left_right(in_list)
        )

    def test_get_split_top_left_right_6values(self):
        in_list = ["A", "B", "C", "D", "E", "F"]
        self.assertEqual(
            (["A", "B", "C"], "D", ["E", "F"]),
            main.get_split_top_left_right(in_list)
        )
