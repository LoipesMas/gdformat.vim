let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import vim_gdformat
EOF

command! -nargs=0 GDFormat call GDFormat()

function! GDFormat()
    py3 vim_gdformat.gdformat()
endfunction

let g:gdformat_on_write = 0

function! GDFormatOnWrite()
    if g:gdformat_on_write == 1
        :GDFormat
    endif
endfunction
autocmd BufWritePre *.gd call GDFormatOnWrite()

