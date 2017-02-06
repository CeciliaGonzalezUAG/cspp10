#identify whether or not its a word or phrase
# from there seperate whether or not the word has more than 3 letters.
#from there makde it turn the word into a list of letters
#or the phrase into a list of words. scramble the letters nd everything that 
#has more than  letters. from there make sure to be able to turn
#it into the order of the sentence, undo the lists and return the scrambled
#version into the phrase.
import random
phrase= input("Input word or phrase: ")


def scramble_word(phrase):
    if len(phrase)> 2:
        first_letter= phrase[0]
        last_letter= phrase[-1]
        new_phrase=phrase[1:-1]
        phrase_list= list(new_phrase)
        random.shuffle(phrase_list)
        new_phrase= "".join(phrase_list)
        new_phrase= first_letter+new_phrase+last_letter
        print(new_phrase)
    
scramble_word(phrase)


    
    