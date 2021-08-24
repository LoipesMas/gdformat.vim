# Disclaimer
This is an early version, barely working.

# About
A simple wrapper for [gdformat](https://github.com/Scony/godot-gdscript-toolkit).

It's based on [clang-format.py](https://github.com/llvm/llvm-project/blob/main/clang/tools/clang-format/clang-format.py).


# Usage
Example (put this in your vim config):
```
function! FormatGDScript()
  py3f <path-to-file>/vim-gdformat.py
endfunction
autocmd BufWritePre *.gd call FormatGDScript()
```
(This will automagically format the file when you save it)
