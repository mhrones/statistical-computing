#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author:
"""

import random
import ps2
import ps3a


word_list = ps2.load_words()

def test_mc_player(hand, N=100, seed=1):
    """
    play a hand 3 times, make sure produced same scores.

    """

    hand_score = ps3a.play_mc_hand(hand)

    if hand_score != ps3a.play_mc_hand(hand):
        return False
    return True

if __name__ == "__main__":

    # Set the MC seed
    seed = 100

    test_hands = ['helloworld', 'UMasswins', 'statisticscomputing']
    for handword in test_hands:
        hand = ps2.get_frequency_dict(handword)
        if not test_mc_player(hand, seed=seed):
            print('Reproducibility problem for %s' % handword)
        else:
            print("No Issues for ", handword)
