# -*- coding: utf-8 -*-
"""
@author: moloch
Copyright 2017
"""

import os

from random import SystemRandom

RAND = SystemRandom()
CODENAME_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CODENAME_PATH, "adjectives.txt"), 'r') as words:
    ADJECTIVES = [word.strip() for word in words.readlines() if len(word) > 2]

with open(os.path.join(CODENAME_PATH, "nouns.txt"), 'r') as words:
    NOUNS = [word.strip() for word in words.readlines() if len(word) > 2]


def get_codename():
    """ Get a random CIA/NSA-like codename """
    return u"{adjective} {noun}".format(
        adjective=RAND.choice(ADJECTIVES),
        noun=RAND.choice(NOUNS)
    ).upper()
