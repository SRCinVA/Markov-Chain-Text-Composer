# this is where the Markov Chain Distribution will live
import random

# Like in the explanation up front, this graph will be based on weighted vertices

class Vertex: 
    def __init__(self, value): # in this case, value will be the word
        self.value = value
        self.adjacent = {}  # this dictionary will keep track of which vertices
                            # are connected to the vertex. Basically, a word:weight pair.
        self.neighbors = [] # to keep track of the neighbors ...
        self.neighbors_weights = [] # ... and the neighbor weights

    def add_edge_to(self, vertex, weight=0) # we need to know which vertex we're drawing the edge toward.
                                            # initialize weight to 0
        self.adjacent[vertex] = weight # this pairs the verex with the weights in the dictionary 
    
    def add_edge(self, vertex):  # for words that are already present in the dictionary
        self-adjacent[vertex] =self.adjacent.get(vertex,0) + 1 # plus 1 to account for the new occurence.
        # if the key exists, we'll pull up the value of that pre-existing vertex.
        # if it doesn't, then it's just 0.

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)   # we append the vertex to self.neighbors (unclear why)
            self.neighbors_weights.append(weight)  # same (??) reasoning here.
        # this has *nothing* to do with probabilities.

    def next_word(self): # this finds a random word based on weights
        return random.choices(self.neighbors, weights = self.neighbors_weights)[0] # this gives us the first item in the list

    # Now assemble these vertices into a graph

class Graph:
    def __init__(self):
        self.vertices = {}    # this will be an empty dicitonary of vertices
                                # this way, when we encounter a new word,
                                # we can look it up and get the vertex from thsi dictionary

    def get_vertex_values(self): # this returns all the possible words in the graph (so far).
        return set(self.vertices.keys*())

    def add_vertex(self, value): # for whenever we encounter a new word.
        self.vertices[value] = Vertex(value) 
        # Above, we create a new Vertex object and "put it in this string-to-vertex mapping"
        # (not really sure what that means ...)

    def get_vertex(self, value): # for when you have a word and need to find the vertex object it represents
        # if the value isn't in the graph already, then you need to add it in, shown below:
        if value not in self.vertices:
            self.add_vertex(value)
        #otherwise, you just return what's already there:
        return self.vertices[value]

    def get_next_word(self, current_vertex): # "get the next word based on these weight mappings."
        self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self): # this is to ge the probability mappings of every vertex
        for vertex in self.vertices.values():
            vertex.get_probability_map()  # 2:44:38 cannot understand the reasoning behind this ...