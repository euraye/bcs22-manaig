# CLASSES ------------------------------------------------------------------------------------------

class PathNode:
    name = None
    next_node = None
    def __init__(self, location_name):
        pass
    
    def nextNode(self):
        return self.next_node
    
class PathList:

    starting_node = None
    last_node = None
    size = 0



    def __init__(self):
        pass
    


    def get(self, name):
        """
        Returns the node that matches the given name.
        Returns None if no match is found.
        """
        current_node = self.starting_node
        while current_node != None:
            if current_node.name == name: return current_node
            else: current_node = current_node.nextNode()
        else: return None



    def getByIndex(self, index):
        """
        Returns the node at the nth position in the link.
        Returns None if index exceeds the link size.
        """
        counter = 0
        current_node = self.starting_node
        while current_node is not None:
            if counter == index: return current_node
            else:
                current_node = current_node.nextNode
                counter += 1
        else: return None



    def add(self, name):
        """ Adds a node to this PathList link by creating a new PathNode instance with the provided name. """
        self.addByNode(PathNode(name))
        return self



    def addByNode(self, node):
        """ Adds a PathNode to this PathList link by adding an existing PathNode instance. """

        #If this PathList's last_node is a Nonetype...
        if self.last_node is None:
            current_node = self.starting_node if self.starting_node is not None else node
            next_node = current_node.nextNode()
            #Keep going through the link until it reaches a Nonetype. (End of link) (Uses linear search)
            while True:
                #If the end of the link is reached...
                if next_node == None:
                    #Assign a new PathNode to the current_node's next_node.
                    current_node.next_node = node

                    #Assign the newly created PathNode to this PathList's last_node.
                    self.last_node = current_node.next_node
                    break
                
                #Updates the current_node to become its next_node for the next iteration.
                else: current_node = current_node.nextNode()
            
            self.size += 1

            #Returns this PathList instance once the loop ends; for method chaining.
            return self
        
        #If this PathList's last_node is a PathNode instance...
        else:
            #Assigns the last_node's next_node (a Nonetype) a new PathNode instance.
            self.last_node.next_node = node

            #Assigns the newly created PathNode instance as the new last_node.
            self.last_node = self.last_node.next_node



    def addList(self, list):
        """ Appends this list of PathNode instances to the end of the link. """
        for item in list:
            if isinstance(item, str): self.add(PathNode(item))
            elif isinstance(item, PathNode): self.add(item)
            else: print(f"Item {item} is neither a String or PathNode instance; cannot be added.")
            
            self.add(item)
            print(f"Added path: {item}")
    


    def merge(self, path_list_instance):
        """ Merges this PathList instance with this one. """
        first_node = path_list_instance.starting_node
        self.addByNode(first_node)
        current_node = first_node.nextNode

        while current_node is not None:
            self.addByNode(current_node)
            current_node = current_node.nextNode
        else: self.addByNode(None)



    def pop(self, name):
        """ Removes one PathNode with a matching name and returns the removed PathNode. """
        current_node = self.starting_node
        new_list = PathList()
        match = None
        hasFoundMatch = False

        while current_node is not None:
            if current_node.name != name or hasFoundMatch: new_list.add(current_node)
            else:
                match = current_node
                hasFoundMatch = True

            current_node = current_node.nextNode()
        
        self = new_list
        return match



    def popAll(self, name):
        """ Removes all PathNodes with matching names and returns all removed PathNodes. """
        current_node = self.starting_node
        new_list = PathList()
        matches = None

        while current_node is not None:
            if current_node.name != name: new_list.add(current_node)
            else: matches.append(current_node)

            current_node = current_node.nextNode()
        
        self = new_list
        return matches



    def remove(self, name):
        """ Removes one PathNode with a matching name, but returns this PathList instance instead. """
        self.pop(name)
        return self



    def removeAll(self, name):
        """ Removes all PathNodes with matching names, but returns this PathList instance instead. """
        self.popAll(name)
        return self



    def search(self, name):
        """ Returns the first PathNode with a matching name. """
        current_node = self.starting_node

        while current_node is not None:
            if current_node.name == name: return current_node

        return current_node



    def searchAll(self, name):
        """ Returns all PathNodes with a matching name. """
        current_node = self.starting_node
        match_list = []

        while current_node is not None:
            if current_node.name == name: match_list.append(current_node)

        return match_list
    

# SHORT PATH ALGO ----------------------------------------------------------------------------------
import heapq

#Implements Dijkkstra's algorithm
def shortPath(graph, start, end):
    #A list of the shortest distances from the start vertex (0).
    distanceList = {vertex: float("inf") for vertex in graph}
    distanceList[start] = 0

    #Minimum heap used to select the vertex with the shortest distance.
    #Q: What's a heap?
    priority_queue = [(0, start)]

    #List of vertices that lead to the current vertex.
    previous_vertices = {vertex: None for vertex in graph}

    #Iterates through the list of vertices
    while priority_queue: #While priority_queue is is not empty.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        #If the current distance is greater than the current vertex's distance.
        if current_distance > distanceList[current_vertex]:
            continue

        for neighbor_vertex, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distanceList[neighbor_vertex]:
                distanceList[neighbor_vertex] = distance
                heapq.heappush(priority_queue, (distance, neighbor_vertex))
                previous_vertices[neighbor_vertex] = current_vertex

    short_path = []

    while end:
        short_path.insert(0, end)
        end = previous_vertices[end]
    return distanceList, previous_vertices



# MASTER -------------------------------------------------------------------------------------------

"""
Home : Store A, Store B, Intersection
Store A : Home, Store B
Store B: School
Intersection : School
School : Intersection
"""
path_graph = {
    "Home" : [ ("Store A", 7), ("Store B", 12), ("Intersection", 25)],
    "Store A" : [("Home", 7), ("Store B", 5)],
    "Store B" : [("School", 7)],
    "Intersection" : [("School", 7)],
    "School" : [("Store B", 7), ("Intersection", 7)]
}

"""
Home -> Store A
Home -> Store B
Home -> Intersection
Store A -> Home
Store A -> Store B
Store B -> School
Intersection -> School
School -> Intersection
"""

pathTuple = (
    ("Home", "Store A"),
    ("Home", "Store B"),
    ("Home", "Intersection"),
    ("Store A", "Home"),
    ("Store A", "Store B"),
    ("Store B", "School"),
    ("Intersection", "School"),
    ("School", "Intersection")
)
pathListFinal = PathList()

for path in pathTuple:
    start = path[0]
    end = path[1]

    #The PathList inside parent PathList, pathListFinal, forming a 2D PathList.
    second_layer = PathList()

    #Obtains the values returned by shortPath().
    shortest_distance, shortest_path = shortPath(path_graph, start, end)

    #Gets the distance between the start and end points and assigns it to "distance".
    distance = shortest_distance.get(end)

    second_layer.add(start)
    second_layer.add(end)
    second_layer.add(distance)

    pathListFinal.add(second_layer)

    print(f"Path from {path[0]} to {path[1]} took {distance} steps. Added to PathList.")

    """
    Notes:
    What do I add to the list?
    The path from point A to Z? If so, why are all of them only 2 nodes long?
    They never go from point A to B to ... to Z.
    Is it supposed to store them as a list or a tuple?
    If so, it seems redundant to use the existing list or tuple types when I already have my own.
    If I have to use my own implementation (thus creating a 2D structure),
    then storing only 2 items per 2nd layer seems too much,
    especially that a type of list was not specified;
    a linked list would not be the best structure for this purpose.

    Apologies if I got something horribly wrong while doing this,
    I'm just working with what little information I have, plenty of which is guesswork.

    Edit:
    I have decided I will do the latter--use my own structure to form a 2D linked list.
    Given that we are just starting out in DSA, I doubt this is the way I'm supposed to do this,
    but I am out of ideas at this point and I really need to go to bed.
    What I made may be wrong, but it wasn't for a lack of trying.

    Ps. I am aware that the parameter for PathList.add() is called "name",
        but was used to store non-name data regardless. This was because I
        intended it to be used as a chain that points from Point A to Z.
        However, I had to abandon that idea last minute due to the aforementioned problems.
        Normally, I would change the names if this was an ongoing project.
        Though I kept them as is to show my prior intent with this.
    """

#--------------- IGNORE ---------------
#Printed data from shortest_path and shortest_distance respectively.
"""
Path from Home to Store A:
{'Home': None, 'Store A': 'Home', 'Store B': 'Store A', 'Intersection': 'Home', 'School': 'Store B'}
{'Home': 0, 'Store A': 7, 'Store B': 12, 'Intersection': 25, 'School': 19}

Path from Home to Store B:
{'Home': None, 'Store A': 'Home', 'Store B': 'Store A', 'Intersection': 'Home', 'School': 'Store B'}
{'Home': 0, 'Store A': 7, 'Store B': 12, 'Intersection': 25, 'School': 19}

Path from Home to Intersection:
{'Home': None, 'Store A': 'Home', 'Store B': 'Store A', 'Intersection': 'Home', 'School': 'Store B'}
{'Home': 0, 'Store A': 7, 'Store B': 12, 'Intersection': 25, 'School': 19}

Path from Store A to Home:
{'Home': 'Store A', 'Store A': None, 'Store B': 'Store A', 'Intersection': 'School', 'School': 'Store B'}
{'Home': 7, 'Store A': 0, 'Store B': 5, 'Intersection': 19, 'School': 12}

Path from Store A to Store B:
{'Home': 'Store A', 'Store A': None, 'Store B': 'Store A', 'Intersection': 'School', 'School': 'Store B'}
{'Home': 7, 'Store A': 0, 'Store B': 5, 'Intersection': 19, 'School': 12}

Path from Store B to School:
{'Home': None, 'Store A': None, 'Store B': None, 'Intersection': 'School', 'School': 'Store B'}
{'Home': inf, 'Store A': inf, 'Store B': 0, 'Intersection': 14, 'School': 7}

Path from Intersection to School:
{'Home': None, 'Store A': None, 'Store B': 'School', 'Intersection': None, 'School': 'Intersection'}
{'Home': inf, 'Store A': inf, 'Store B': 14, 'Intersection': 0, 'School': 7}

Path from School to Intersection:
{'Home': None, 'Store A': None, 'Store B': 'School', 'Intersection': 'School', 'School': None}
{'Home': inf, 'Store A': inf, 'Store B': 7, 'Intersection': 7, 'School': 0}
"""


