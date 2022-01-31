# MACROPAD Hotkeys: Tower application for Mac
# Contributed by Me

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Tower', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Fetch', [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, 'f']),
        (0x004000, 'Pull', [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, 'p']),
        (0x004000, 'Push', [Keycode.OPTION, Keycode.SHIFT, Keycode.COMMAND, 'u']),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
