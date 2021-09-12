from format_functions import get_startupinfo, run_binary, parse_error_output



def read_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def test_run_binary():
    text = read_from_file("tests/texts/valid.gd").encode('utf-8')
    stdout, stderr, returncode = run_binary("gdformat", text, None)
    assert returncode == 0
    assert len(stderr) == 0

def test_invalid():
    text = read_from_file("tests/texts/invalid.gd").encode('utf-8')
    stdout, stderr, returncode = run_binary("gdformat", text, None)
    assert returncode != 0
    assert len(stderr) > 0

def test_invalid_parse():
    text = read_from_file("tests/texts/invalid.gd").encode('utf-8')
    stdout, stderr, returncode = run_binary("gdformat", text, None)
    err = stderr.decode('utf-8')
    cursor_line, cursor_column = parse_error_output(err)
    assert cursor_line == 6 and cursor_column == 5




def test_parse_error_from_file():
    err = read_from_file("tests/texts/error_out.txt")
    cursor_line, cursor_column = parse_error_output(err)
    assert cursor_line == 6 and cursor_column == 5
