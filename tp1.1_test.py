from TP import tp11

tree = {
		'A': ['C', 'B'],
		'B': ['F', 'D', 'C'],
		'C': ['E', 'B'],
		'D': [],
		'E': [],
		'F': []
		}

print(tp11.dfs(tree, 'A', 'E'))  # infinite loop
print(tp11.dfs_enh(tree, 'A', 'E'))  # perfect iterative
print(tp11.dfs_recursive(tree, 'A'))  # infinite recursion
print(tp11.dfs_recursive_enh(tree, 'A'))  # perfect recursion


