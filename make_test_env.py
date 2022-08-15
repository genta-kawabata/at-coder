# -*- coding: utf-8 -*-

import os
import argparse

TESTS_DIR = "./tests"
TEMPLATE_FILE = "./test_template.txt"

if __name__ == "__main__":

    current_dir = os.path.abspath("./")

    # オプションからコンテストID を取得
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("-c", "--contest", help="Contest ID", required=True, type=str)
    args = parser.parse_args()
    contest_id = args.contest

    # コンテストIDディレクトリの中にある各問題の名前を取得
    contest_dir = os.path.join(current_dir, contest_id)
    if not os.path.exists(contest_dir):
        print(f"directory {contest_id} doesn't exist...")
        exit(1)

    paths_in_contest_dir = os.listdir(contest_dir)
    # list_question_dir = [dir for dir in paths_in_contest_dir if os.path.isdir(os.path.join(current_dir, contest_id, dir))]

    # tests ディレクトリの作成
    tests_dir_path: str = os.path.abspath(TESTS_DIR)
    if not os.path.exists(tests_dir_path):
        os.makedirs(tests_dir_path)

    # テストコードのテンプレートを取得
    with open(os.path.abspath(TEMPLATE_FILE), "r") as fr:
        test_code = fr.read()
        
        # コンテストIDと問題名を置換
        new_test_code = test_code.replace("{contest_id}", contest_id)
        # new_test_code = new_test_code.replace("{question}", question_name)

        # テストコードファイル作成
        # test_file_path = os.path.join(tests_dir_path, f"test_{contest_id}_{question_name}.py")
        test_file_path = os.path.join(tests_dir_path, f"test_{contest_id}.py")
        with open(test_file_path, "w") as fw:
            fw.write(new_test_code)
