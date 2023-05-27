#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

neofetch

PS1="[\u@\h \W]\$ "

alias grep="grep --color=auto"

alias ls="ls --color=auto"

alias update="sudo pacman -Syy"

alias upgrade="sudo pacman -Syyuu"

alias df="df -h -x squashfs -x tmpfs -x devtmpfs"

alias paur="paru"

alias st="curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3"

alias run="./a.out"

alias clean="sudo pacman -Scc"

alias config.py="vim ~/.config/qtile/config.py"

alias .bashrc="vim .bashrc"

alias nm="nm-connection-editor"

alias anime="ani-cli"

alias pacman.conf="sudo vim /etc/pacman.conf"

alias .vimrc="vim .vimrc"

alias xinitrc="sudo vim /etc/X11/xinit/xinitrc"

alias .Xresources="vim .Xresources"

alias init.lua="vim ~/.config/nvim/init.lua"

#set history format with timestamps
HISTTIMEFORMAT="%Y-%m-%d %T "

. "$HOME/.cargo/env"

export PATH=$PATH:/usr/bin/pip
export PATH=$PATH:/home/lo/.local/bin
function _update_ps1() {
    PS1=$(powerline-shell $?)
}
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi
