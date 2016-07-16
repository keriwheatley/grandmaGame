# Keri Lau
# November 21, 2008
# Collaberation Statement: "I worked on this assignment alone using only course materials."

import time
import random
import string

# This program is a remake of a well-known pattern game.
# The object of the game is to get the player to find a pattern in a series of words.
# Words that have double back-to-back letters, such as LITTLE and BOOK are the answers.
# If the player's input is incorrect, the program chooses a set of examples at random, such as BOOKS versus MAGAZINES, to hint to the player.
# If the player inputs a correct word (for example BITTER) the computers says its correct and asks for another word.
# The game exits when the player types DONE.



def start_grandmaGame():
    print "This is a game."
    time.sleep(.5)
    print "Find the pattern and determine what Grandma likes."
    time.sleep(.5)
    print "To quit the game, just type DONE."
    time.sleep(.5)
    print ""
    print "Grandma likes PEPPER but not SALT."
    time.sleep(.5)
    word1=raw_input("What else does she like? ")
    time.sleep(.5)
    if word1=="DONE":
        print "Thanks for playing!"
    else:
        game(word1)

    
def game(word2):
    i=0
    while (i+1)<len(word2): # This loop finds the double letters (ie. 'll' or 'tt') in the inputed word.
        if word2[i]==word2[i+1]:
            print "Yes, Grandma does like %s." %(string.upper(word2))
            time.sleep(.5)
            word3=raw_input ('What else does she like? ')
            time.sleep(.5)
            i=len(word2)-2
            if word3!="DONE":
               game(word3)
            else:
                print "Thanks for playing!"
            return
        if word2[i]!=word2[i+1]:
            i=i+1
    b=random.randrange(0,16)
    likes=["sinners", "winners", "Mommy", "little", "tall", "Harry","kittens", "all", "books", "trees", "bees", "yellow", "jello", "good", "kisses", "wrapping paper", "the moon", "yellow"]
    dislikes=["saints", "losers", "Mother","big", "short", "Ron", "cats", "none", "magazines", "flowers", "ladybugs", "white", "fudge", "bad", "hugs","gift bags", "the sun", "white"]
    c=likes[b]
    d=dislikes[b]
    print "No, Grandma doesn't like %s." %(string.upper(word2)) # This prints a random set of examples.
    time.sleep(.5)
    print 'She likes %s but not %s.'  %(string.upper(c),string.upper(d))
    time.sleep(.5)
    word3=raw_input ("What else does she like? ")
    time.sleep(.5)
    if word3!="DONE":
        game(word3)
    else:
        print "Thanks for playing!"
