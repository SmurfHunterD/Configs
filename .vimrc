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
set encoding=utf-8
syntax on
colorscheme sorbet 
let python_highlight_all = 1
:hi Directory guifg=#c291cf ctermfg=blue
let g:minimap_auto_start = 1
let g:minimap_width = 20
let g:lightline = {
      \ 'colorscheme': 'sorbet',
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'readonly', 'filename', 'modified', 'title' ] ]
      \ },
      \ 'component': {
      \   'title': '1v9ish'
      \ },
      \ }

"                   Start Plug-ins

call plug#begin('~/.vim/plugged')
"       Check and fix syntax with LSP support
Plug 'dense-analysis/ale'
"       Server address highlighting 
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
"       Vim Statusline/Tabline Highliting
Plug 'itchyny/lightline.vim'
"       Autocomplete
Plug 'ycm-core/youcompleteme'
"       Nerdtree Icons
Plug 'ryanoasis/vim-devicons'
"       Nerdtree Icon Colors
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
"       Vim Minimap
Plug 'wfxr/minimap.vim'

call plug#end()

"                   End Plug-ins

"                   Commands and keybindings
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
autocmd VimEnter * NERDTree | wincmd p

