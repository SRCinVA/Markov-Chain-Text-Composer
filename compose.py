import string
import graph from Graph, Vertex

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

    g.generate_probability_mappings()

    return g


def main():
    # 1.) get words from the text
    words = get_words_from_text('text/hp_sorcerer_stone.txt')
# 2.) make a graph using those words
# 3.) get the next word for x number
# 4.) show these to the user
pass
