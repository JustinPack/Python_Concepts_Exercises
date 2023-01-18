# Demonstrate topological sort on a directed acyclic graph
# a directed acyclic graph (DAG) is a directed graph with no cycles
# cycles are sequences of vertices v1, v2, ..., vk such that v1 = vk and v1, v2, ..., vk-1 are distinct
# a topological ordering of a DAG is a linear ordering of its vertices such that if (u, v) is an edge in the DAG,
# then u comes before v in the ordering

# import the defaultdict class from the collections module
from collections import defaultdict

# define the vertices of the graph
vertices = ['A', 'B', 'C', 'D', 'E']

# define the edges of the graph
edges = [('A', 'C'), ('A', 'B'), ('B', 'D'), ('C', 'D'), ('D', 'E')]


# print the topological ordering of the vertices
def topological_sort(vertices, edges):
    # Create a dictionary to store the indegree of each vertex
    indegree = defaultdict(int)

    # Initialize the indegree of each vertex to 0
    for v in vertices:
        indegree[v] = 0

    # Create a dictionary to store the adjacency list for each vertex
    adjacency_list = defaultdict(list)

    # Initialize the adjacency list for each vertex to an empty list
    for v in vertices:
        adjacency_list[v] = []

    # Iterate through the edges and update the indegree and adjacency list for each vertex
    for u, v in edges:
        indegree[v] += 1
        adjacency_list[u].append(v)

    # Create a queue to store the vertices with indegree 0
    queue = []

    # Add all vertices with indegree 0 to the queue
    for v in vertices:
        if indegree[v] == 0:
            queue.append(v)

    # Initialize a list to store the topological ordering of the vertices
    topological_ordering = []

    # Perform the topological sort
    while queue:
        # Remove a vertex from the queue
        u = queue.pop(0)

        # Add the vertex to the topological ordering
        topological_ordering.append(u)

        # Decrement the indegree of each of u's neighbors
        for v in adjacency_list[u]:
            indegree[v] -= 1

            # If a neighbor's indegree becomes 0, add it to the queue
            if indegree[v] == 0:
                queue.append(v)

    # Return the topological ordering of the vertices
    return topological_ordering


topological_ordering = topological_sort(vertices, edges)
print(topological_ordering)  # ['A', 'C', 'B', 'D', 'E']
