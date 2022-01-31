# MACROPAD Hotkeys: Tower application for Mac
# Contributed by Me

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Xcode', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Run', [Keycode.COMMAND, 'r']),
        (0x004000, 'NB Run', [Keycode.SHIFT, Keycode.COMMAND, 'r']),
        (0x000000, '', []),
        # 2nd row ----------
        (0x004000, 'Test L', [Keycode.OPTION, Keycode.CONTROL, Keycode.COMMAND, 'u']),
        (0x004000, 'NB Test', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL, Keycode.COMMAND, 'u']),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0xFF0000, 'Dep Cl', [{'menu': 'File,Packages,Reset Package Caches'}]),
        (0xFF0000, 'Clean', [Keycode.SHIFT, Keycode.COMMAND, 'k']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
