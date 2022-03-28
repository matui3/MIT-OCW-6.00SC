from ps3a import *
import time
from perm import *

WORDLIST_FILENAME = "words.txt"

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    max = 0
    word = ""
    for num in range(1, HAND_SIZE):
        options = get_perms(hand, num)
        for perm in options:
            if perm in word_list:
                score = get_word_score(perm, HAND_SIZE)
                if score > max:
                    max = score
                    word = perm
    return word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    run = True
    while run:
        print("Current Hand: " + str(display_hand(hand)))
        word = comp_choose_word(hand, word_list)
        if is_valid_word(word, hand, word_list):
            update_hand(hand, word)
            points = get_word_score(word, HAND_SIZE)
            total_score += points
            print("\"" + word + "\"" + " earned " + str(points) +
              " points. Total: " + str(total_score) + " points")
        else:
            print("Total score: " + str(total_score) + " points.")
            run = False

    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    play = True
    while play:
        game = input(
            "Would you like to play hangman? Press u for a user and c for the computer. ")
        if game == 'u':
            choice = input("Press n for a new game. Press r to play the last hand. Press e to exit the game. ")
            if choice == 'n':
                hand = deal_hand(HAND_SIZE)
                play_hand(hand, word_list)
            elif choice == 'r':
                play_hand(hand, word_list)
            elif choice == 'e':
                play=False
            else:
                print(choice)
        elif game == 'c':
            hand = deal_hand(HAND_SIZE)
            comp_play_hand(hand, word_list)
        else:
            print(game)
        
          
          
          
                # ("Would you like to play hangman? Press n for a new game. Press r to play the last hand. Press e to exit the game. ")
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

#hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
#print(comp_play_hand(hand, word_list))