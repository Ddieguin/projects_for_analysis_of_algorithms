import graph
import copy

def heapPermutation(a, size, p):
  # if size becomes 1 then prints the obtained
  # permutation
  if size == 1:
      tmp = copy.copy(a)
      tmp.append(copy.copy(a[0]))
      p.append(tmp)
      return

  for i in range(size):
    heapPermutation(a, size-1, p)

    # if size is odd, swap 0th i.e (first)
    # and (size-1)th i.e (last) element
    # else If size is even, swap ith
    # and (size-1)th i.e (last) element
    if size & 1:
        a[0], a[size-1] = a[size-1], a[0]
    else:
        a[i], a[size-1] = a[size-1], a[i]

def validatePermutation(listPermutations, graph):
  resp = []
  for permutation in listPermutations:
    validPermutation = validatePermutationUtil(permutation, graph)
    resp.append(copy.copy(validPermutation))
  return resp
  
def validatePermutationUtil(permutation, graph):
  for i in range(len(permutation)-1):
    if not(graph.has_edge(permutation[i], permutation[i+1])):
      return None
  return permutation

def findCiclesByPermutation(graph, V):
  cicles = {}
  i = 3
  while(i <= V):
    p = []
    vertexes = list(range(0, i))
    heapPermutation(vertexes, len(vertexes), p)
    validPermutations = validatePermutation(p, graph)
    cicles[i] = copy.copy(validPermutations)
    i += 1
  return removeBadPermutations(cicles)

def removeBadPermutations(cicles):
  for k, permutations in cicles.items():
    filteredPermutations = list(filter(None, permutations))
    cicles[k] = filteredPermutations
  return cicles

if __name__ == "__main__":
  V = 5
  graph = graph.Graph(V)
  graph.add_edge(0, 1)
  graph.add_edge(1, 2)
  graph.add_edge(2, 0)
  graph.add_edge(2, 3)
  graph.add_edge(1, 3)
  graph.add_edge(4, 3)
  graph.add_edge(4, 2)

  cicles = findCiclesByPermutation(graph, graph.V)

  for k, cicle in cicles.items():
    print("k=" + str(k) + " -> " + str(cicle) +  "\n" );