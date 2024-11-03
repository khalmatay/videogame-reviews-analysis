from functions import algo_question


def test_algo_question():
    input_file = "tests/test_input.txt"

    expected_output = "YES\n6 2 2\nYES\n97 1 1 1\nNO\nNO\nYES\n1 1 1 1 1 1 1 1\nNO\nYES\n3 1 1"

    assert algo_question(input_file) == expected_output
