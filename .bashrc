#
# ~/.bashrc
#

neofetch

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#######  aliases  #######
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias edit='sudo vim'

alias gedit='sudo geany'

alias btp='btop'

alias update='sudo pacman -Syy'

alias upgrade='sudo pacman -Syyuu'

alias df="df -h -x squashfs -x tmpfs -x devtmpfs"

alias extip="curl icanhazip.com"

alias st="curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3"

alias run="./a.out"

alias clean="sudo pacman -Scc"

alias anime="ani-cli"