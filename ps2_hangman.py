# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()



# your code begins here!



def get_guessed_word(secret_word, letters_guessed):
    word_to_print = ""
    for char in secret_word:
        if char in letters_guessed:
            word_to_print += char
        else:
            word_to_print += "_"
    return word_to_print



def hangman(secret_word):

    num_of_guesses = 2*len(secret_word)
    available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                         'w', 'x', 'y', 'z']
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    guess = False
    letters_guessed = []
    while num_of_guesses > 0 and not guess:
        print("--------------")
        print("You have " + str(num_of_guesses) + " left")
        print("".join(available_letters))
        letter = input("Please guess a letter: ")
        num_of_guesses -= 1
        if letter == secret_word:
            print("Congratulations you won!")
            guess = True
        elif letter not in available_letters:
            print("Oops you already guessed that letter!, guess again!")
            num_of_guesses += 1
        elif letter not in secret_word:
            print("Oops that letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            available_letters.remove(letter)
        else:
            letters_guessed.append(letter)
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            available_letters.remove(letter)
        if num_of_guesses == 0:
            print("Oops, you lost. Would you like to play again?")
            print("The word is " + secret_word)
            guess = True
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            guess = True
        

       
        
        

        # state the number of guesses - This is  done and easy.
        # state all the avaliable letters - Having difficulty with this.

        # Stating all available letters this means. I will print get_available letters. This should be a continuous appending list. Everytime
        # I guess a letter, it should append to a list letters_guessed. This list will then go into letters_guessed 
        # let someone guess if the letter is correct or not it should go into letters guessed
        # this should then PRINT the available letters
        # this will then print the guess
        # print the guess in terms of _

        


hangman(choose_word(wordlist))
