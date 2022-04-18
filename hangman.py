# Hangman game
# assignment: programming assignment 1
# author: Arno Wu
# date: Apr 15
# file: hangman.py is a program that (put the description of the program)
# input: guess letter, continue the game or not 
# output: if the letter is in the word, right or wrongwin or lose

from random import choice

# make a dictionary.txt in the same folder where hangman.py is located
dictionary_file = "dictionary.txt"
dictionary_file_test = "dictionary-short.txt"
    
# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, ..., 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12
def import_dictionary (filename) :
    with open (filename, 'r') as f:
            words = [line.rstrip() for line in f.readlines()]
            lines = ([line.replace(' ', '') for line in words])
            lines.sort(key = len)
            dictionary = {3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
            # max_size = 12
    try:
        for key in dictionary:
            for word in lines:
                if key == len(word):
                    dictionary[key].append(word)
    except Exception:
        dictionary[12].append(word)
                    
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)
     
# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    # ask the player to set the options
    print("Welcome to the Hangman Game!")
    
    # size
    word_size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]:"))
    try:
        if word_size in range(3, 13):
            print(f'The word size is set to {word_size}.')     
        else:
            print("A dictionary word of any size will be chosen.")
        word_size = choice(range(1, 13))
                 
    except ValueError:
        print("worng input")
        
    # lives  
    lives = int(input("Please choose a number of lives [1 - 10, default 5]:"))
    try:
        if lives in range(1, 11):
            print(f'You have {lives} lives.')
        else:
            lives = 5
            print("You have 5 lives.") 
    except ValueError:
        print("wrong input")
    
    return (word_size, lives)

def hangman(word_size, lives):
    mylist = ['apple', 'banana', 'orange', 'strawberry']
    
    # use choice() function that selects an item from a list randomly, for example:
    list = dictionary[word_size]
    word = choice(list)
    
    # print(word)
    letter_guessed = ""
    
    # count the wrong letters
    wronglettercount = 0
    
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while lives > 0: 
        guess_letter = input("Letters chosen:")
        
        if guess_letter in letter_guessed:
            print("You have already chosen this letter.")
        elif guess_letter in word:
            print("You guessed right!")
        else:
            lives -= 1
            print("You guessed wrong, you lost one life.")
            wronglettercount += 1  
            
        # Guessed words
        letter_guessed = letter_guessed + guess_letter
        
        # format and print the game interface:
        for letter in word:
            if letter in letter_guessed:
                print(letter,end=" ")
                
            elif letter not in letter_guessed:
                print("_" * word_size,end=" ")
                
            elif "-" in word:
                print("-",end=" ")

        print(f" lives: {lives}",end=" ")
        print(str("X" * wronglettercount) + str("0" * lives))

    # check if the player won or lose 
    if wronglettercount == 0:
        print(f"Congratulations!!! You won! The word is {word}!")
            
        #Update the words the player has guessed
        mylist.append(letter_guessed)
            
        # Ask the player to continue th game or not  
        play_again = input("Would you like to play again [Y/N]?")
        if play_again == "Y":
           main()
                
        elif play_again == "N":
            print("Goodbye!")
            exit()
                      
    else:
        print(f"You lost! The word is {word}!") 
        play_again = input("Would you like to play again [Y/N]?")
                
        if play_again == "Y":
            main()       
        elif play_again == "N":
            print("Goodbye!")
            exit()
def main():
    word_size, lives = get_game_options ()
    hangman(word_size, lives)
    
# MAIN
if __name__ == '__main__' :
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    
    # print the dictionary (use only for debugging)
    print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary
    main()
