import graph

cycles = [None] * 4

IN_STACK = 1
NOT_VISITED = 2
DONE = 3

def printCycle(stack, v):
  stack2 = []
  stack2.append(stack.pop())
  while stack2[len(stack2)-1] != v:
    stack2.append(stack.pop())
  while stack2:
    print(stack2[len(stack2)-1])
    stack.append(stack2.pop())
    
def DFSTree(g, stack, visited):
  top = stack[len(stack)-1]
  v = g.graph[top]
  while v:
    vertex = v.vertex
    if visited[vertex] == IN_STACK:
      printCycle(stack, vertex)
    elif visited[vertex] == NOT_VISITED:
      stack.append(vertex)
      visited[vertex] = IN_STACK
      DFSTree(g, stack, visited)
    v = v.next
  visited[top] = DONE

def findCycles(g):
  visited = [NOT_VISITED] * (g.V)
  for vertex in range(g.V):
    if visited[vertex] == NOT_VISITED:
      stack = []
      stack.append(vertex)
      visited[vertex] = IN_STACK
      DFSTree(g, stack, visited)
      
if __name__ == "__main__":
    V = 3
    graph = graph.Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.print_graph()

    findCycles(graph)
