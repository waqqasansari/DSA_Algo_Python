def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    # Perform topological sort using Kahn's algorithm (BFS)
    queue = deque()
    # Start with nodes having no incoming edges
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If visited all nodes, then no cycle exists
    return visited_count == numCourses


print(canFinish(2, [[1,0]]))

print(canFinish(2, [[1,0],[0,1]]))