# MACROPAD Hotkeys: Tower application for Mac
# Contributed by Me

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'zoom.us', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Audio', [Keycode.SHIFT, Keycode.COMMAND, 'a']),
        (0x004000, 'Video', [Keycode.SHIFT, Keycode.COMMAND, 'v']),
        (0x000000, '', []),
        # 2nd row ----------
        (0x000020, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x000000, '', []),
        (0x000020, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0xff0000, 'Leave', [Keycode.COMMAND, 'w', -Keycode.COMMAND, '\n']),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
