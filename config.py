from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Return", lazy.spawn("lxterminal"), desc="Terminal Emualtor"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    ######   Personal keybindings   #######
    Key([mod], "p", lazy.spawn("xfce4-screenshooter"), desc="screenshot"),
    Key([mod], "a", lazy.spawn("xfce4-appfinder"), desc="appfinder"),
    Key([mod], "g", lazy.spawn("gimp"), desc="gimp"),
    Key([mod], "d", lazy.spawn("darktable"), desc="darktable"),
    Key([mod], "w", lazy.spawn("brave"), desc="web browser"),
    Key([mod, "shift"], "s", lazy.spawn("steam"), desc="steam"),
    Key([mod, "shift"], "d", lazy.spawn("/opt/resolve/bin/resolve"), desc="DaVinci Resolve"),
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm"), desc="File Manager"),

   ]

groups = [Group(i) for i in "123"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
     #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
     #layout.Max(),
     #Try more layouts by unleashing below layouts.
     #layout.Stack(num_stacks=2),
     #layout.Bsp(),
     #layout.Matrix(),
     #layout.MonadTall(),
     #layout.MonadWide(),
     #layout.RatioTile(),
     layout.Tile(),
     #layout.TreeTab(),
     #layout.VerticalTile(),
     #layout.Zoomy(),
]

###########Define Colors############

##### #700B97 ######
##### #4E9F3D ######
##### #1597E5 ######
##### #F78812 ######
##### #911F27 ######
##### #F037A5 ######
##### #865439 ######
##### #64C9CF ######
##### #FAFF00 ######
##### #C68B59 ######


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),

                widget.GroupBox(),
                
                widget.Prompt(),
                
                widget.WindowName(),
                
                widget.TextBox(foreground="700B97",text='NET'),
                widget.Wlan(foreground="700B97"),
                widget.Net(foreground="700B97"),
                widget.NetGraph(fill_color="1597E5",border_color="700B97",graph_color="700B97"),

                widget.Spacer(length=10),
                
                widget.CPU(foreground="1597E5"),
                widget.CPUGraph(fill_color="700B97",border_color="1597E5",graph_color="1597E5"),

                widget.Spacer(length=10),
                
                widget.TextBox(foreground="64C9Cf",text='RAM'),
                widget.Memory(foreground="64C9CF"),
                widget.MemoryGraph(fill_color="700B97",border_color="64C9CF",graph_color="64C9CF"),

                widget.Spacer(length=10),
                
                widget.TextBox(foreground="C68B59",text='DISK'),
                widget.DF(foreground="C68B59",visible_on_warn=False),

                widget.Spacer(length=10),

                widget.TextBox(foreground="4E9F3d",text='TEMP'),
                widget.ThermalSensor(foreground="4E9F3d"),
                
                widget.Spacer(length=10),
                
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                
                widget.Systray(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "Qtile"
