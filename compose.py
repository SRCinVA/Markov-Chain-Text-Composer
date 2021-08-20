import string

# Goals in this section:

get_words_from_text(text_path):
    with open(text_path, 'r') as f: # why is Python mad at 'open'?
        text = f.read()    
        # next, "we want to split across the white space"
        # " ... and join it to other white spaces."
        # this means replacing all space "units" everywhere in the text with a single space (tough explanation on that ...)
        text = ' '.join(text.split())
        text = text.lower()   # easier to compare everything when it's all lower
        # because of edge cases and over all complexity (this is for intermediate learners),
        # she is overlooking punctuation.
        # the line below turns punctuation in to empty strings (notice the importation above):
        text = text.translate(str.maketrans('','', string.punctuation))
    words = text.split() # 'words' are whatever falls out of the .split() operation.
    return words

def main():
    # 1.) get words from the text
    words = get_words_from_text('text/hp_sorcerer_stone.txt')
# 2.) make a graph using those words
# 3.) get the next word for x number
# 4.) show these to the user
pass
