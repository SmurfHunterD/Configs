set number
set relativenumber
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
colorscheme sorbet 
let python_highlight_all = 1

"                   Start Plug-ins

call plug#begin('~/.vim/plugged')
"       Check and fix syntax with LSP support
Plug 'dense-analysis/ale'
"       Tab Completion
Plug 'chr4/nginx.vim'
"       Close pairs
Plug 'seroqn/tozzy.vim'
"       Nerdtree
Plug 'preservim/nerdtree'
"       NerdTree highlighting buffers
Plug 'PhilRunninger/nerdtree-buffer-ops'
"       Debugging
Plug 'puremourning/vimspector'
"       Python Syntax Highliting
Plug 'vitiral/vim-python'

call plug#end()

"                   End Plug-ins

"                   Commands and keybindings
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
autocmd BufWritePost *Xresources,Xdefaults !xrdb %
autocmd VimEnter * NERDTree | wincmd p

