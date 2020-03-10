"""
Compilation of specific level configuration

For each level, there must be an element created in every list
"""

# W = wall
# {1...9} = user blocks
# E = exit
# Indications to load the map properly:
# -the map should be a rectangle with walls in its edges
# -there should be at least 1 piece and an exit
LEVELS = [
    [  # Level 1
        "WWWWWWWWWWWW",
        "W1W        W",
        "W W W  W   W",
        "W W W  W   W",
        "W W W      W",
        "W W W WWWWWW",
        "W   W     EW",
        "WWWWWWWWWWWW",
    ],
    [  # Level 2
        "WWWWWWWWWWWWWWW",
        "W1W       W   W",
        "W W WWWWW W W W",
        "W W     W W W W",
        "W WWWWW W W W W",
        "W W     W W W W",
        "W W WWWWW W W W",
        "W W W     W W W",
        "W W W WWWWW W W",
        "W   W       WEW",
        "WWWWWWWWWWWWWWW",
    ],
    [  # Level 3
        "WWWWWWWWWWWWW",
        "W    W W    W",
        "W    W W    W",
        "WWWWWW WWWWWW",
        "W1    2    EW",
        "WWWWWW WWWWWW",
        "W    W W    W",
        "W    W W    W",
        "WWWWWWWWWWWWW",
    ],
    [  # Level 4
        "WWWWWWWWWWWWW",
        "W1        WWW",
        "WWWWWWW   WWW",
        "W         WWW",
        "W           W",
        "W         W W",
        "W         W W",
        "W2        WEW",
        "WWWWWWWWWWWWW",
    ],
    [  # Level 5
        "WWWWWWWWWWWWWWWW",
        "W W1       W  3W",
        "W W            W",
        "W W       WWW  W",
        "W W      WWWW  W",
        "W W      WW WWWW",
        "W WWWWW WW     W",
        "W       W   W  W",
        "W2          W EW",
        "WWWWWWWWWWWWWWWW",
    ],
    [  # Level 6
        "WWWWWWWWWWWWWWW",
        "W1  W      W  W",
        "W   W      W  W",
        "W       W  W  W",
        "W       W     W",
        "WWWWW         W",
        "W2W     W     W",
        "W W     W  W  W",
        "W       W  W EW",
        "WWWWWWWWWWWWWWW",
    ],
    [  # Level 7
        "WWWWWWWWWWWWWWWWW",
        "W1              W",
        "W               W",
        "W           W WWW",
        "W2   W      W   W",
        "W    W      W   W",
        "WWWWWW      W   W",
        "W           W   W",
        "W3          W  EW",
        "WWWWWWWWWWWWWWWWW",
    ],
    [  # Level 8
        "WWWWWWWWWWWWW",
        "W    W2W    W",
        "WW         WW",
        "W1          W",
        "WW         WW",
        "W           W",
        "W    W W   EW",
        "WWWWWWWWWWWWW",
    ],
    [  # Level 9
        "WWWWWWWWWWWWW",
        "W   W     W W",
        "W W W  W    W",
        "W1W    W    W",
        "WWWWWWWW    W",
        "W2W    W    W",
        "W W W  W    W",
        "W   W     WEW",
        "WWWWWWWWWWWWW",
    ],
]

# Temporarily disabled
SONGS = [
    "resources/songs/bgm_action_1.mp3",  # Level 1
    "resources/songs/bgm_action_2.mp3",  # Level 2
    "resources/songs/bgm_action_3.mp3",  # Level 3
    "resources/songs/bgm_action_4.mp3",  # Level 4
    "resources/songs/bgm_action_5.mp3",  # Level 5
]

# In seconds
LEVEL_TIMER = [
    25,  # Level 1
    25,  # Level 2
    25,  # Level 3
    25,  # Level 4
    25,  # Level 5
    25,  # Level 6
    15,  # Level 7
    30,  # Level 8
    10,  # Level 9
]
