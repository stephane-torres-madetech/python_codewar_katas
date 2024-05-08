""" Write a function that takes in a string of one or more words, and returns the same string, 
    but with all words that have five or more letters reversed (Just like the name of this Kata). 
    Strings passed in will consist of only letters and spaces. 
    Spaces will be included only when more than one word is present. """

def spin_words(sentence: str):

    spun_string = ''

    list_words = sentence.split()

    for word in list_words:
        if len(word) > 5:
            word = word[::-1]
        
        spun_string += word + ' '

    return spun_string.strip()