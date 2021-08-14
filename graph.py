# this is where the Markov Chain Distribution will live
import random

# Like in the explanation up front, this graph will be based on weighted vertices

class Vertex: 
    def __init__(self, value): # in this case, value will be the word
        self.value = value
        self.adjacent = {}  # this dictionary will keep track of which vertices
                            # are connected to the vertex. Basically, a word:weight pair.

    def add_edge_to(self, vertex, weight=0) # we need to know which vertex we're drawing the edge toward.
                                            # initialize weight to 0
        self.adjacent[vertex] = weight # this pairs the verex with the weights in the dictionary 
    
    def add_edge(self, vertex):  # for words that are already present in the dictionary
        self-adjacent[vertex] =self.adjacent.get(vertex,0) + 1 # plus 1 to account for the new occurence.
        # if the key exists, we'll pull up the value of that pre-existing vertex.
        # if it doesn't, then it's just 0
