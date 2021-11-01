set number
set tabstop=4 softtabstop=4 shiftwidth=4
set nowrap
set bg=light
set hlsearch
set incsearch
set expandtab
set smartcase
set noswapfile
set autoindent
set fileformat=unix
set encoding=utf-8
set path+=**
set wildmenu
set termguicolors
set t_ut=
syntax on

autocmd BufWritePost *Xresources,*Xdefaults !xrdb %




"                   Start Plug-ins

call plug#begin('~/.vim/plugged')


"       Check and fix syntax with LSP support
Plug 'dense-analysis/ale'

"       Tab Completion
Plug 'ackyshake/VimCompletesMe'

"       Preview colours in source code
Plug 'ap/vim-css-color'

"       Syntax Highlighting for server configs
Plug 'chr4/nginx.vim'

"       Close pairs
Plug 'seroqn/tozzy.vim'


call plug#end()

"                   End Plug-ins

"                   Commands and keybindings


