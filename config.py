from typing import List 
from libqtile import bar, layout, widget, hook
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
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Terminal Emulator"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    ######   Personal keybindings   #######
    Key([mod], "p", lazy.spawn("xfce4-screenshooter"), desc="screenshot"),
    Key([mod], "g", lazy.spawn("gimp"), desc="raster image editor"),
    Key([mod], "d", lazy.spawn("darktable"), desc="photo editor"),
    Key([mod], "w", lazy.spawn("brave"), desc="web browser"),

    Key([mod], "i", lazy.spawn("inkscape"), desc="vector image editor"),
    Key([mod], "o", lazy.spawn("obs"), desc="streaming"),
    Key([mod], "v", lazy.spawn("kdenlive"), desc="video editor"),
    Key([mod], "e", lazy.spawn("codium"), desc="IDE"),
    Key([mod], "a", lazy.spawn("ardour7"), desc="audio editor"),
    Key([mod], "l", lazy.spawn("lutris"), desc="game center"),
    Key([mod], "space", lazy.spawn("pavucontrol"), desc="volume control"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="chat server"),
    Key([mod, "shift"], "s", lazy.spawn("steam"), desc="game center"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show drun combi -show-icons"), desc="run menu"),
    Key([mod, "shift"], "q", lazy.spawn("qbittorrent"), desc="bittorrent client"),
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm"), desc="file manager"),
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

    ######   Colors   ######

#c1 = "#95E2FF"
#c2 = "#49A4D4"
#c3 = "#1597E5"
#c4 = "#700B97"
#c5 = "#64C9Cf"
#c6 = "#B7E4D6"

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
     layout.Tile(
         border_width = 5,
         border_focus = "#700b97",
         add_after_last = False,
         master_length = 1
         ),
     layout.TreeTab(),
     #layout.VerticalTile(),
     #layout.Zoomy(),
]

widget_defaults = dict(
    font='Source Code Pro',
    fontsize=11,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
     Screen(
        top = bar.Bar(
			[
                widget.Sep(linewidth = 2,foreground = "#95e2ff"),
                
                widget.CurrentLayout(foreground = "#95e2ff"),

                widget.GroupBox(active = "#95e2ff"),
                
                widget.Sep(linewidth = 2,foreground = "#95e2ff"),
                
                widget.Prompt(foreground = "#49a4d4"),

                widget.Sep(linewidth = 2,foreground = "#49a4d4"),
                
                widget.WindowName(foreground = "#1597e5"),

                widget.Sep(linewidth = 2,foreground = "#1597e5"),
                widget.Sep(linewidth = 2,foreground = "#700b97"),

                widget.TextBox(text = ''),
                widget.TextBox(foreground = "#700b97",text = 'NET'),
                #widget.Wlan(foreground = "#700b97"),
                widget.Net(foreground = "#700b97"),
                widget.NetGraph(fill_color = "#1597e5",border_color = "#700b97",graph_color = "#700b97"),

                widget.Sep(linewidth = 2,foreground = "#700b97"),
                widget.Sep(linewidth = 2,foreground = "#1597e5"),

                widget.TextBox(text = ''),
                widget.CPU(foreground = "#1597e5"),
                widget.CPUGraph(fill_color = "#700b97",border_color = "#1597e5",graph_color = "#1597e5"),
                widget.ThermalZone(fgcolor_normal = "1597e5"),

                widget.Sep(linewidth=2,foreground = "1597e5"),
                widget.Sep(linewidth=2,foreground = "49a4d4"),

                widget.TextBox(text = ''),
                widget.TextBox(foreground = "#49a4d4",text = 'DISK'),
                #widget.DF(foreground = "#49a4d4",visible_on_warn = False),
                widget.HDDBusyGraph(fill_color = "#700b97",border_color = "#49a4d4",graph_color = "#49a4d4"),

                widget.Sep(linewidth = 2,foreground="#49a4d4"),
                widget.Sep(linewidth = 2,foreground="#87e4d6"),
                widget.TextBox(text = ''),
                widget.TextBox(foreground = "#87e4d6",text = 'RAM'),
                widget.Memory(foreground = "#87e4d6",measure_mem = 'M'),
                widget.MemoryGraph(fill_color = "#700b97",border_color = "#87e4d6",graph_color = "#87e4d6"),
                widget.Sep(linewidth = 2,foreground="#49a4d4"),

                widget.Sep(linewidth = 2,foreground="#ffffff"),
                widget.Clock(format="%y/%m/%d %H:%M"),
                widget.Sep(linewidth = 2,foreground="#ffffff"),
			],
			24,
        ),
     ),
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
