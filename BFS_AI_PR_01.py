graph = {
  'A' : ['B','D','H'],
  'B' : ['C'],
  'D' : ['E','F'],
  'H' : ['I'],
  'C' : [],
  'E' : [],
  'F' : ['G'],
  'I' : [],
  'G' : []
}
visited = []		
stack = []     		
def breadth_first_search(visited,queue,starting_node):
    visited.append(starting_node)
    stack.append(starting_node)
    while stack:
        removed_ele = stack.pop(0)
        print(visited, "\n")
        for child in graph[removed_ele]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
breadth_first_search(visited,stack,'A')
for i in visited:
    print(i, end=" ")



