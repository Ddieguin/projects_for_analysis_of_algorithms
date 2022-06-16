class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, n):
        self.V = n
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            v = self.graph[i]
            while v:
                print(" -> {}".format(v.vertex), end="")
                v = v.next
            print(" \n")

    def has_edge(self, s, d): 
      v = self.graph[s]
      while v:
        if v.vertex == d: 
          return True
        else:
          v = v.next
      return False
      