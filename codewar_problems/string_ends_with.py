def string_ends_with(text, ending):

    # get length of ending
    # take last letters of same length and compare to ending, return same 

    ending_length = len(ending)
    text_end = text[-ending_length:]
    return text_end == ending
    return True