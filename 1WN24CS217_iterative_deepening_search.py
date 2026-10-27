
def dls(graph, node, goal, limit, path):
    if node == goal:
        return path + [node]

    if limit == 0:
        return None

    for child in graph.get(node, []):
        if child not in path:
            result = dls(graph, child, goal, limit - 1, path + [node])
            if result is not None:
                return result

    return None


def ids(graph, initial, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls(graph, initial, goal, depth, [])

        if result is not None:
            print("Solution Path:", " -> ".join(result))
            print("Depth:", len(result) - 1)
            return

    print("Goal not found within the specified maximum depth.")


initial = input("Initial State: ")
goal = input("Goal State: ")
max_depth = int(input("Maximum Depth: "))

n = int(input("Number of nodes: "))
graph = {}

for _ in range(n):
    line = input().replace(":", " ").replace(",", " ").split()
    node = line[0]
    children = line[1:]
    graph[node] = [] if children == ["-"] else children

ids(graph, initial, goal, max_depth)
