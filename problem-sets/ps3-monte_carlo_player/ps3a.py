#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
"""

import random
import ps2


random.seed("I love Statistics!")
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
word_list = ps2.load_words()



def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    handlen = 0
    for v in hand.values():
        handlen += v

    return handlen


def hand_to_list(hand):
    """
    Helper Function
    transfer current hand to a list, so we can use random.sample()
    """
    ls=[]
    for letter in hand.keys():
        #iterate letter key value times
        for j in range(hand[letter]):
             ls=ls+[letter]
    #create a list of letters
    return ls

# PROBLEM 1a
def choose_word(hand, N=100):
    """
    choose best word for current hand by N simulations,
    then calculate its score
    if can't find a word return none and score=0
    """

    bestscore = 0
    bestword = None


    # IMPLEMENT ME

    hand_len = calculate_handlen(hand)
    rand_length = 3#random.randint(0,hand_len)
    hand_list = hand_to_list(hand)

    words_generated = []

    for word_attempt in range(0,N):
        temp_list = hand_to_list(hand)
        word_created = ""

        for i in range(0, rand_length):
            if(len(temp_list) > rand_length):
                char = random.choices(temp_list)[0]
                temp_list.remove(char)
                word_created = word_created + char
        if(len(word_created) == rand_length):
            words_generated.append(word_created)

    valid_word_scores = {}
    for word in words_generated:
        if ps2.is_valid_word(word, hand, word_list):
            valid_word_scores[word] = ps2.get_word_score(word, hand_len)

    if(len(valid_word_scores.keys()) == 0):
        return None, 0
    bestword = ""
    bestscore = 0
    for word in valid_word_scores.keys():
        if valid_word_scores[word] > bestscore:
            bestword = word
            bestscore = valid_word_scores[word]

    return bestword, bestscore




# PROBLEM 1b
def play_mc_hand(hand, N=100):
    """
    repeat choose best word process,
    find best word and score for currrent hand
    until game ends
    return total score and words found in a list
    """
    random.seed("I love Statistics!")

    handscore=0  # Score for the hand
    wordls=[]  # List of words in order played

    # IMPLEMENT ME
    hand_copy = hand.copy()

    # As long as there are still letters left in the hand:
    while calculate_handlen(hand_copy) > 0:

        # Display the hand

        # ps2.display_hand(hand)

        # Finds the word based on the Monte Carlo Simulation

        chosen_word, chosen_score = choose_word(hand_copy, N)

        if chosen_word == None:
            break
        else:
            hand_copy =  ps2.update_hand(hand_copy, chosen_word)
            #print("HAND UPDATED: ",hand_copy)
            wordls.append(chosen_word)
            handscore += chosen_score






    return wordls, handscore

# PROBLEM 1d
def play_n_mc_hand(hand, N, n):

    """
    Simulated n hands generating N candidate words for each round.
    Return two lists: a nested list of hands(each itself is a list) played and a list of scores.

    """
    #create two empty lists

    mc_hands = []
    mc_scores = []

    # IMPLEMENT ME


    for sample in range(0, n):
        hand_copy = hand.copy()
        word_list, hand_score = play_mc_hand(hand_copy, N)
        mc_hands.append(word_list)
        mc_scores.append(hand_score)

    return (mc_hands, mc_scores)


# PROBLEM 1c
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:
    * The hand is displayed.

    * The user may input a word.
    * When any word is entered (valid or invalid), it uses up letters
      from the hand.
    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # Keep track of the total score
    totalscore = 0

    # As long as there are still letters left in the hand:
    handlen = calculate_handlen(hand)
    while handlen > 0:

        # Display the hand
        ps2.display_hand(hand)

        # Ask user for input
        word = input('Enter a word: ')
        """
        add choose_word() option when input is "?"
        """
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break

        elif word == '?':
            # IMPLEMENT ME
            word, b_score = choose_word(hand, N=100)
            pass

        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if ps2.is_valid_word(word, hand, word_list):

                # Tell the user how many points the word earned,
                # and the updated total score
                handscore = ps2.get_word_score(word, handlen)
                print('You earned {} points.'.format(handscore))
                totalscore += handscore

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('Invalid word')

            # update the user's hand by removing the letters of their inputted word
            hand = ps2.update_hand(hand, word)
            handlen = calculate_handlen(hand)


    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print('Total score is {}.'.format(totalscore))

    # Return the total score as result of function
    return totalscore

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    # Generate a (reproducible) hand
    word_list = ps2.load_words()
    random.seed(1)
    hand = ps2.deal_hand(15)

    # Set the number of MC samples
    N=100

    # Choose a word from the hand
    print(choose_word(hand, N))

    # Play the hand using MC
    c=play_mc_hand(hand, N)
    print(c)

    # Play n MC hands
    n=5
    (mc_hands, mc_scores) = play_n_mc_hand(hand, N, n)
    print(mc_hands)
    print(mc_scores)

    # Play the hand manually with help
    play_hand(hand, word_list)
