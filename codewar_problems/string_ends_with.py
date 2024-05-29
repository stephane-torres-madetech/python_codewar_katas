def string_ends_with(text, ending):

    # get length of ending
    # take last letters of same length and compare to ending, return same 

    text_end = text[-len(ending):]
    return text_end == ending
    return True


    # python has an endswith method!!!