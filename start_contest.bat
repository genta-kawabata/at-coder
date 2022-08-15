@echo off

set contest_id=abc195

rem call を使うと、処理が終わってから次の処理にいく
call acc new %contest_id%
call py make_test_env.py -c %contest_id%
