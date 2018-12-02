import sys

sys.setrecursionlimit(5000)
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
def dfs_recursive_enh_sol(graph, start, goal, path=[], vis=[]):
	path += [start]
	vis.append(start)

	# TO DO: add a visited function to add a path from parent to node

	for neighbor in reversed(graph[start]):
		if goal in path:
			break
		if neighbor not in path:
			if goal == neighbor:
				path += neighbor
				vis.append(neighbor)
				print("jjknkdfnv", vis)
				break
			else:
				path = dfs_recursive_enh_sol(graph, neighbor, goal, path, vis)

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


# dfs algo returns path from root to targeted vertex
found = 0


def dfs_goal_w_path(graph, node, goal, path=[], visited=[]):
	global found
	if found > 0:
		return
	visited.append(node)
	path = path + [node]
	for neighbor in graph[node]:
		if neighbor == goal:
			found = found + 1
			path.append(neighbor)
			visited.append(node)
			print('visited: ', visited)
			print('path: ', path)
			return
		if neighbor not in path:
			dfs_goal_w_path(graph, neighbor, goal, path, visited)

