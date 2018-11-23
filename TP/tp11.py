def dfs(graph, start, goal):
	stack = [start]
	path = []
	sommet = None

	while len(stack) != 0:
		sommet = stack.pop()
		if sommet == goal:
			path.append(sommet)
			break
		path.append(sommet)
		[stack.append(i) for i in graph[sommet]]

	return path


def dfs_enh(graph, start, goal):
	stack = [start]
	path = []
	sommet = None

	while len(stack) != 0:
		sommet = stack.pop()
		if sommet == goal:
			path.append(sommet)
			break
		path.append(sommet)
		[stack.append(i) for i in graph[sommet] if i not in path]

	return path


# function without stack!!
def dfs_recursive(graph, start, path=[]):
	path += [start]

	for neighbor in reversed(graph[start]):
		path = dfs_recursive(graph, neighbor, path)

	return path


# function without stack
def dfs_recursive_enh(graph, start, path=[]):
	path += [start]

	for neighbor in reversed(graph[start]):
		if neighbor not in path:
			path = dfs_recursive_enh(graph, neighbor, path)

	return path
