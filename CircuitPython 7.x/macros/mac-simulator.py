# MACROPAD Hotkeys: Tower application for Mac
# Contributed by Me

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from secrets import secrets

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Simulator', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Video', [Keycode.COMMAND, 'r']),
        (0x004000, 'Pic', [Keycode.COMMAND, 's']),
        (0x000000, '', []),
        # 2nd row ----------
        (0x0000ff, 'Keybrd', [Keycode.SHIFT, Keycode.COMMAND, 'k']),
        (0x0000ff, 'Shake', [Keycode.CONTROL, Keycode.COMMAND, 'z']),
        (0x0000ff, 'Dark', [Keycode.SHIFT, Keycode.COMMAND, 'a']),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0xff0000, 'Amy', ['amy@3md.com', Keycode.TAB, "%s\n" % secrets['amy@3md.com']]),
        # 4th row ----------
        (0xff0000, 'gambr', ['gambrozio@doximity.com', 0.1, Keycode.TAB, "%s" % secrets['gambrozio@doximity.com'], 0.1, "\n"]),
        (0xff0000, 'g.ambr', ['g.ambrozio@doximity.com', 0.1, Keycode.TAB, "%s" % secrets['g.ambrozio@doximity.com'], 0.1, "\n"]),
        (0xff0000, 'kwong', ['kwong+md@doximity.com', 0.1, Keycode.TAB, "%s" % secrets['kwong+md@doximity.com'], 0.1, "\n"]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
