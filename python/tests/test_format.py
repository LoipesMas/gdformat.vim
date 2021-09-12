"""
Tests
"""
from format_functions import run_binary, parse_error_output


def read_from_file(file_path):
    """
    Reads file contents
    """
    with open(file_path, "r") as file:
        return file.read()


def test_run_binary():
    """
    Tests running binary and getting no errors
    """
    text = read_from_file("tests/texts/valid.gd").encode("utf-8")
    stdout, stderr, returncode = run_binary("gdformat", text, None)
    assert returncode == 0
    assert len(stdout) > 0
    assert len(stderr) == 0


def test_invalid():
    """
    Tests running binary and getting errors
    """
    text = read_from_file("tests/texts/invalid.gd").encode("utf-8")
    stdout, stderr, returncode = run_binary("gdformat", text, None)
    assert returncode != 0
    assert len(stdout) == 0
    assert len(stderr) > 0


def test_invalid_parse():
    """
    Tests running binary and getting errors and parsing them correctly
    """
    text = read_from_file("tests/texts/invalid.gd").encode("utf-8")
    _, stderr, _ = run_binary("gdformat", text, None)
    err = stderr.decode("utf-8")
    cursor_line, cursor_column = parse_error_output(err)
    assert cursor_line == 6 and cursor_column == 5


def test_parse_error_from_file():
    """
    Tests parsing errors from file (that worked last time)
    """
    err = read_from_file("tests/texts/error_out.txt")
    cursor_line, cursor_column = parse_error_output(err)
    assert cursor_line == 6 and cursor_column == 5
