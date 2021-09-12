"""
    Functions for vim_gdformat.py
"""

import subprocess
import sys


def get_startupinfo():
    """
    Gets startup info for subprocess.
    (to avoid flashing an ugly, ugly cmd prompt on Windows when invoking gdformat)
    """
    startupinfo = None
    if sys.platform.startswith("win32"):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
    return startupinfo


# Call formatter.
def run_binary(binary, text, startupinfo):
    """
    Runs passed binary on passed text with passed startupinfo
    """
    command = [binary, "-"]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        startupinfo=startupinfo,
    )
    return (*proc.communicate(input=text), proc.returncode)


def parse_error_output(err) -> tuple[int, int]:
    """
    Parses gdformat's error and returns line and column
    """
    lines = err.split("\n")[:-1]
    for line in lines:
        if not line.startswith("lark.exceptions.UnexpectedToken"):
            continue
        split_line = line.split(" ")
        cursor_line = int(split_line[-3][:-1])
        cursor_column = int(split_line[-1][:-1])
        return cursor_line, cursor_column
    return -1, -1


if __name__ == "__main__":
    pass
