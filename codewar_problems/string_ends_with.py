def string_ends_with(text, ending):

    # get length of ending
    # take last letters of same length and compare to ending, return same 

    text_end = text[-len(ending):]
    return text_end == ending

    # could be written return text[-len(ending):] == ending gets rid on another variable declaration.
  


    # python has an endswith method!!!