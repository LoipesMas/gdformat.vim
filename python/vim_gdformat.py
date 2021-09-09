"""
    Plugin for formating vim buffer using gdformat
"""
# Majority of following code is copied from clang-format.py
# I just made it work with gdformat


import difflib
import platform
import subprocess
import sys

# pylint: disable=import-error
import vim

# set g:gdformat_path to the path to gdformat if it is not on the path
# Change this to the full path if gdformat is not on the path.
BINARY = "gdformat"
if vim.eval('exists("g:gdformat_path")') == "1":
    BINARY = vim.eval("g:gdformat_path")


def get_buffer(encoding):
    """Return the current vim buffer
    enconding - encoding to use for decoding
    """
    if platform.python_version_tuple()[0] == "3":
        return vim.current.buffer
    return [line.decode(encoding) for line in vim.current.buffer]


def gdformat():
    """Formats current vim buffer using gdformat"""
    # Get the current text.
    encoding = vim.eval("&encoding")
    buf = get_buffer(encoding)
    # Join the buffer into a single string with a terminating newline
    text = ("\n".join(buf) + "\n").encode(encoding)

    # Avoid flashing an ugly, ugly cmd prompt on Windows when invoking gdformat.
    startupinfo = None
    if sys.platform.startswith("win32"):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

    # Call formatter.
    command = [BINARY, "-"]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        startupinfo=startupinfo,
    )
    stdout, stderr = proc.communicate(input=text)

    # If errors, print errors and return
    if stderr:
        if proc.returncode == 1:
            lines = stderr.decode(encoding).split("\n")[:-1]
            split_line = lines[5].split(" ")
            cursor_line = int(split_line[-3][:-1])
            cursor_column = int(split_line[-1][:-1])
            vim.command("call cursor(%d, %d)" % (cursor_line, cursor_column))
        print(stderr.decode(encoding))

    elif not stdout:
        print("No output from gdformat (crashed?).")
    else:
        lines = stdout.decode(encoding).split("\n")[:-1]
        sequence = difflib.SequenceMatcher(None, buf, lines)
        for opcode in reversed(sequence.get_opcodes()):
            if opcode[0] != "equal":
                vim.current.buffer[opcode[1] : opcode[2]] = lines[opcode[3] : opcode[4]]


if __name__ == "__main__":
    gdformat()
