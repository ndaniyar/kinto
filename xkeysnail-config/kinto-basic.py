# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = ["gnome-terminal","konsole","io.elementary.terminal","terminator","sakura","guake","tilda","xterm","eterm","kitty","alacritty","mate-terminal","tilix","xfce4-terminal"]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str(x) for x in terminals)

mscodes = ["code","vscodium"]
codeStr = "|".join(str(x) for x in mscodes)

define_modmap({
})

# [Global modemap] Change modifier keys as in xmodmap
# Non-terminal
define_conditional_modmap(lambda wm_class: wm_class.casefold() not in terminals,{
    # Mac Only
    Key.CAPSLOCK: Key.LEFT_CTRL,
    Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
})

# [Conditional modmap] Change modifier keys in certain applications
# Terminal
define_conditional_modmap(re.compile(termStr, re.IGNORECASE), {
    Key.CAPSLOCK: Key.LEFT_CTRL,
    Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
})

# Terminal Cmd-Tab sends Alt-Tab
define_keymap(re.compile(termStr, re.IGNORECASE),{
    # Only mapping C-S-key that are used in gnome-terminal
    # Copy/paste
    K("RC-C"): K("C-Shift-C"),
    K("RC-V"): K("C-Shift-V"),
    # New/Close Tab/Window, preferences
    K("RC-T"): K("C-Shift-T"),
    K("RC-N"): K("C-Shift-N"),
    K("RC-COMMA"): K("C-Shift-COMMA"),  # preferences
    K("RC-W"): K("C-Shift-W"),  # close tab
    K("RC-Q"): K("C-Shift-Q"),  # close window
    # Zoom
    K("RC-MINUS"): K("C-Shift-MINUS"),
    K("RC-EQUAL"): K("C-Shift-EQUAL"),
    K("RC-KEY_0"): K("C-Shift-KEY_0"),
    # Find
    K("RC-F"): K("C-Shift-F"),
    K("RC-G"): K("C-Shift-G"),
    K("RC-H"): K("C-Shift-H"),  # doesn't work
    K("RC-J"): K("C-Shift-J"),  # doesn't work
    # Tabs
    K("RC-KEY_1"): K("C-Shift-KEY_1"),
    K("RC-KEY_2"): K("C-Shift-KEY_2"),
    K("RC-KEY_3"): K("C-Shift-KEY_3"),
    K("RC-KEY_4"): K("C-Shift-KEY_4"),
    K("RC-KEY_5"): K("C-Shift-KEY_5"),
    K("RC-KEY_6"): K("C-Shift-KEY_6"),
    K("RC-KEY_7"): K("C-Shift-KEY_7"),
    K("RC-KEY_8"): K("C-Shift-KEY_8"),
    K("RC-KEY_9"): K("C-Shift-KEY_9"),
})
