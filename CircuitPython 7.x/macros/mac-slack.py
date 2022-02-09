# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Slack', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00ff00, 'Check', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':white_check_mark:', 0.2, '\n']),
        (0x00ff00, 'ThbUp', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':thumbsup:', 0.2, '\n']),
        (0xff0000, 'ThbDn', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':thumbsdown:', 0.2, '\n']),
        # 2nd row ----------
        (0x00ff00, '+1', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':plus1:', 0.2, '\n']),
        (0x0000ff, 'Tada', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':tada:', 0.2, '\n']),
        (0x0000ff, 'Shrg', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':shrug:', 0.2, '\n']),
        # 3rd row ----------
        (0x0000ff, 'Giggle', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':giggle:', 0.2, '\n']),
        (0x0000ff, 'lol', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':joy:', 0.2, '\n']),
        (0x0000ff, 'Party', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':party:', 0.2, '\n']),
        # 4th row ----------
        (0x880000, 'Nope', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':shake:', 0.2, '\n']),
        (0x880000, 'Tks', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':thanks:', 0.2, '\n']),
        (0x880000, 'Yes', [Keycode.COMMAND, Keycode.SHIFT, '\\', -Keycode.COMMAND, -Keycode.SHIFT,
                           ':yes-party:', 0.2, '\n']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
