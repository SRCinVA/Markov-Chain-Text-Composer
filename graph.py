# this is where the Markov Chain Distribution will live
import random

# Like in the explanation up front, this graph will be based on weighted vertices

class Vertex: 
    def __init__(self, value): # in this case, value will be the word
        self.value = value
        self.adjacent = {}  # this is a dictionary that will keep track of which vertices
                            # are connected to the vertex.