# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

random_word = random.choice(FIVE_LETTER_WORDS)
random_word = "yucky"

letter_count = {}
guesses = {}
for letter in random_word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)

def wordle():
    row = 0
    col = 0

    def enter_action(s):  
        row = gw.get_current_row()
        col = 0        
        word = ""    
        for x in range(N_COLS):
            word += gw.get_square_letter(row,col) 
            col = col + 1
        
        #gw.show_message(word)

        if word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("That's a good word")
            square = 0
            count = 0
            color_count = {}

            for x in range(N_COLS):
                letter = gw.get_square_letter(row,square)
                if letter.lower() == random_word[square]:
                    gw.set_square_color(row,square,"#66BB66")
                    color = "green"
                    count = count + 1
                elif letter.lower() in random_word:
                    gw.set_square_color(row,square, "#CCBB66")
                    color = "yellow"
                else:
                    gw.set_square_color(row,square, "#999999")
                    color = "gray"
                
                color_count[square] = color

                square = square+1      
            
            print(color_count)
            square = 0
            for x in range(N_COLS):
                letter = gw.get_square_letter(row,square).lower()
                if letter in letter_count and color_count[square] == "green":
                    col = 0
                    for t in range(N_COLS):
                        if gw.get_square_letter(row,col).lower() == letter and color_count[col] != "green":
                            gw.set_square_color(row,col, "#999999")
                            color_count[col] = "gray"
                            print("test1")
                        col = col+1
            
            for x in range(N_COLS):
                if letter in letter_count and color_count[square] == "yellow":
                    col = 0
                    color_instance = 0
                    for t in range(N_COLS):
                        if gw.get_square_letter(row,col).lower() == letter and color_count[col] != "gray":
                            color_instance = color_instance + 1
                            print("test2")
                        col = col + 1
                    print(color_instance)

                    col = 0
                    while letter_count[letter] < color_instance:
                        if gw.get_square_letter(row,col).lower() == letter and color_count[col] == "yellow":  
                            gw.set_square_color(row,col, "#999999")
                            color_instance = color_instance - 1
                            print("test3")        
                        col = col + 1                         
                square = square+1 
            
            guesses[row] = color_count
            print(guesses)

            if count == 5:
                gw.show_message("You Won!")
                gw.share(guesses)
                gw.set_current_row(7)
            elif row + 1 == N_ROWS:
                gw.show_message("You Lost") 
                gw.set_current_row(row+1)
            else:
                print(row)
                gw.set_current_row(row+1)

        elif (word[-1]) == " ":
            gw.show_message("Not enough letters")
        else:
            gw.show_message("Not in word list")
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    gw.set_current_row(0)

    # for x in random_word:
    #     gw.set_square_letter(row,col,x)
    #     col = col + 1

    
print(random_word)
# Startup code

if __name__ == "__main__":
    wordle()