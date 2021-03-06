import string
import random
import re # to execute the improved-upon regex logic
import os  # so that Python can read multiple file names

import graph from Graph, Vertex

# Goals in this section:

def get_words_from_text(text_path):
    with open(text_path, 'r') as f: # why is Python mad at 'open'?
        text = f.read()    
        # next, "we want to split across the white space"
        # " ... and join it to other white spaces."
        # this means replacing all space "units" everywhere in the text with a single space (tough explanation on that ...)
        
        # to make it more logically like English:
        # remove certain sections of text using regex:
        
        text = re.sub(r'\[(.+)\]', ' ', text) 
        # she explained the reasoning behind the regex, but ... !!!
        # "if there are one or more characters inside the brackets, 
        # then repalce any version of that with a space in that text"




        
        text = ' '.join(text.split())
        text = text.lower()   # easier to compare everything when it's all lower
        # because of edge cases and over all complexity (this is for intermediate learners),
        # she is overlooking punctuation.
        # the line below turns punctuation in to empty strings (notice the importation above):
        text = text.translate(str.maketrans('','', string.punctuation))
    words = text.split() # 'words' are whatever falls out of the .split() operation.
    return words
# now we need to make a graph using those words

def make_graph(words):
    # we import the graph and the vertices from the graphpy file
    # (note the importation above)
    g = Graph

    previous_word = None # just to have this to fill in with each pass (?)
                        # ... because at the beginning, there is no previous word
    
    # for each word:
    for word in words:
    # then, for each word in Words, we're gong to check to see if it's in the graph
        word_vertex = g.get_vertex(word)
    # if it's not, we add it.
    # If there was a previous word (every one after the first, clearly),
    # then add an edge to the graph if the current word does not exist.
        if previous_word:
            previous_word.increment_edge(word_vertex)
    # if it *does* exist, then just increment the weight of the existing edge by 1.
    # set the word to the previous word (so you can access it and move to the next word) 
    # and continue the iteration.
        previous_word = word
    
    # having gone through all words
    # when finished, *then* you can generate the probability mappings:
    g.generate_probability_mappings()
    # last, return the graph
    return g

def compose(g, words, length=50): # note that length is defien by the user
    composition = []   # this is a list that you add to for every new word.
    word = g.get_vertex(random.choice(words)) # pick a random word from g. This starts the whole process.
    # for n iterations (defined by the user), we'll iterate to get the next word.
    for _ in range(length):
        composition.append(word.value)  # ... we'll append that next word to list 'composition'
                                        # ... and in doing so that word's value (unsure of this)
        # after doing that, now it's:
        word = g.get_next_word(word)                                
        # this replaces the current 'word' variable with the next one, time after time.
    return composition

def main(artist):
    # 1.) get words from the text, but for one song at a time:
    # words = get_words_from_text('text/hp_sorcerer_stone.txt')
    
    # to optimize main() for more than one song:
    words = [] # an empty list: we need a place to put things.
    for song_file in os.listdir(f'song/{artist}'):
    # the above will list every file in the folder with that artist name.
    # below, all we need to do is pass those parameters into the method, and we will get the words back:
        print(song_file) # this will help clue us in on where it might have failed.
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extends(song_words) # interesting note: x.extends iterates over all elements in the argument; it doesn't just lump everything as "one."


    # 2.) make a graph using those words from def get_words_from_text
    g = make_graph(words) 
    # 3.) get the next word for x number of words (as defined by the user); let's make def compose() for this:
    composition = compose(g, words, 100) # 100 overrides the original choice of 50.    
    return ' '.join(composition) # we want to return a string (does ' ' concatenate a space to every word? Yes.)
    # 4.) show these to the user

# to run the function:
if __name__ == '__main__':
    print(main(<artist>))
