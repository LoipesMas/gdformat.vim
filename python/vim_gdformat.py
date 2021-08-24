# Majority of following code is copied from clang-format.py
# I just made it work with gdformat


import difflib
import json
import platform
import subprocess
import sys
import vim

# set g:gdformat_path to the path to gdformat if it is not on the path
# Change this to the full path if gdformat is not on the path.
binary = 'gdformat'
if vim.eval('exists("g:gdformat_path")') == "1":
    binary = vim.eval('g:gdformat_path')


def get_buffer(encoding):
    if platform.python_version_tuple()[0] == '3':
        return vim.current.buffer
    return [line.decode(encoding) for line in vim.current.buffer]


def gdformat():
    # Get the current text.
    encoding = vim.eval("&encoding")
    buf = get_buffer(encoding)
    # Join the buffer into a single string with a terminating newline
    text = ('\n'.join(buf) + '\n').encode(encoding)

    # Avoid flashing an ugly, ugly cmd prompt on Windows when invoking gdformat.
    startupinfo = None
    if sys.platform.startswith('win32'):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

    # Call formatter.
    command = [binary, '-']
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, startupinfo=startupinfo)
    stdout, stderr = p.communicate(input=text)

    # If errors, print errors and return
    if stderr:
        print(stderr.decode(encoding))
        return

    if not stdout:
        print('No output from gdformat (crashed?).')
    else:
        lines = stdout.decode(encoding).split('\n')[:-1]
        sequence = difflib.SequenceMatcher(None, buf, lines)
        for op in reversed(sequence.get_opcodes()):
            if op[0] != 'equal':
                vim.current.buffer[op[1]:op[2]] = lines[op[3]:op[4]]
    return


if __name__ == "__main__":
    gdformat()
