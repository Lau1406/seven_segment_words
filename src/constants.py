"""
File that store constants to be used in other places
"""

# A tuple list with all letters and whether or not they can be displayed on a 7-segment display. All lower case
seven_segment_symbols = [
    ('a', True),
    ('b', True),
    ('c', True),
    ('d', True),
    ('e', True),
    ('f', True),
    ('g', False),
    ('h', True),
    ('i', True),
    ('j', True),
    ('k', False),
    ('l', True),
    ('m', False),
    ('n', True),
    ('o', True),
    ('p', True),
    ('q', False),
    ('r', True),
    ('s', True),
    ('t', True),
    ('u', True),
    ('v', False),
    ('w', False),
    ('x', False),
    ('y', True),
    ('z', True),
    ('0', True),
    ('1', True),
    ('2', True),
    ('3', True),
    ('4', True),
    ('5', True),
    ('6', True),
    ('7', True),
    ('8', True),
    ('9', True),
    ('0', True),
    ('-', True),
    ('.', True),
    (',', True),
    ('|', True),
]

banned_letters = 'gkmqvwxz'
regex_banned_letters = '[gkmqvwxz]'

filename = '../data/words.txt'
