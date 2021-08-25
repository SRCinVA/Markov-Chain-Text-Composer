import string
import graph from Graph, Vertex

# Goals in this section:

def get_words_from_text(text_path):
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

def main():
    # 1.) get words from the text
    words = get_words_from_text('text/hp_sorcerer_stone.txt')
    # 2.) make a graph using those words from def get_words_from_text
    g = make_graph(words) 
    # 3.) get the next word for x number of words (as defined by the user); let's make def compose()
    
    # 4.) show these to the user
    pass
