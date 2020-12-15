import enum

COMMON_COLORS = (
    '--Select--',
    'Black',
    'Blue',
    'Brown',
    'Green',
    'Orange',
    'Peach',
    'Purple',
    'Red',
    'White',
    'Yellow',
)

COMMON_COLORS_HEX_CODES = {
    'Black': '#000000',
    'Blue': '#0000ff',
    'Brown': '#964b00',
    'Green': '#00ff00',
    'Orange': '#ffa500',
    'Peach': '#ffe5b4',
    'Purple': '#800080',
    'Red': '#ff0000',
    'White': '#ffffff',
    'Yellow': '#ffff00',
}

FILE_TYPES = [
    ('All files', '*'),
    ('BMP files', '*.bmp'),
    ('JPG files', '*.jpg'),
    ('JPEG files', '*.jpeg'),
    ('PNG files', '*.png'),
]

EVENT_FLAG_ALTKEY = 'Alt_L'
EVENT_FLAG_CTRLKEY = 'Control_L'
EVENT_FLAG_ENTERKEY = 'Return'
EVENT_FLAG_SHIFTKEY = 'Shift_L'

EVENT_LBUTTONDOWN = 'ButtonPress'
EVENT_LBUTTONUP = 'ButtonRelease'

EVENT_MOUSEMOVE = 'Motion'


class Region(enum.Enum):
    intensity = 1
    pattern = 2
