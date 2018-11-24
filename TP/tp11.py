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


# function without stack!! + solution with cycles
def dfs_recursive_enh(graph, start, path=[]):
	path += [start]

	for neighbor in reversed(graph[start]):
		if neighbor not in path:
			path = dfs_recursive_enh(graph, neighbor, path)

	return path


# function without stack 1 solution
def dfs_recursive_enh_sol(graph, start, goal, path=[]):
	path += [start]

	for neighbor in reversed(graph[start]):
		if goal in path:
			break
		if neighbor not in path:
			if goal != neighbor:
				path = dfs_recursive_enh_sol(graph, neighbor, goal, path)
			else:
				path += neighbor
				break

	return path


# function without stack multiple solutions
def dfs_recursive_enh_multi_sol(graph, start, goal, path=[]):
	path += [start]

	for neighbor in reversed(graph[start]):
		if [i for i in goal if i in path] != []:
			break
		if neighbor not in path:
			if neighbor not in goal:
				path = dfs_recursive_enh_multi_sol(graph, neighbor, goal, path)
			else:
				path += neighbor
				break

	return path

