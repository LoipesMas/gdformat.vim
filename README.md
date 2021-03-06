# About
A simple wrapper for [gdformat](https://github.com/Scony/godot-gdscript-toolkit).

It's based on [clang-format.py](https://github.com/llvm/llvm-project/blob/main/clang/tools/clang-format/clang-format.py).

# Requirements
Obviously requires `gdformat` from [godot-gdscript-toolkit](https://github.com/Scony/godot-gdscript-toolkit).

If it's not in your PATH, you need to set `g:gdformat_path` to it's path.

# Installation
Install using your favourite plugin manager.

For example `Plug 'loipesmas/gdformat.vim'` for vim-plug.

You also need to install `gdformat`, for example with `pip install gdtoolkit`.

# Usage
Use command `:GDFormat` to format current buffer.

You can also do `let g:gdformat_on_write = 1` in your vim config to automatically format on write.

# Contributing
Contributions are very welcome! Just open an issue or a PR.
