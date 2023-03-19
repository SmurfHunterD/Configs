#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

neofetch

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias update='sudo pacman -Syy'

alias upgrade='sudo pacman -Syyuu'

alias df="df -h -x squashfs -x tmpfs -x devtmpfs"

alias paur="paru"

alias extip="curl icanhazip.com"

alias st="curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3"

alias run="./a.out"

alias clean="sudo pacman -Scc"

alias config.py="vim ~/.config/qtile/config.py"

alias miniterm.conf="vim ~/.config/miniterm/miniterm.conf"

alias firewall="sudo firewall-config"

alias .vimrc="vim .vimrc"

alias .bashrc="vim .bashrc"

alias getiso="wget -P /home/lo/ISOs -i iso-list.txt"

alias nm="nm-connection-editor"

alias anime="ani-cli"

alias starship.toml="vim .config/starship.toml"

alias pacman.conf="sudo vim /etc/pacman.conf"

#set history format with timestamps
HISTTIMEFORMAT="%Y-%m-%d %T "

eval "$(starship init bash)"
