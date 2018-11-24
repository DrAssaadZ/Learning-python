from TP import tp11

tree = {
		'A': ['C', 'B'],
		'B': ['C', 'F', 'D'],
		'C': ['E', 'B'],
		'D': [],
		'E': [],
		'F': []
		}

# print(tp11.dfs(tree, 'A', 'E'))  # infinite loop
print(tp11.dfs_enh(tree, 'A', 'E'))  # perfect iterative
# print(tp11.dfs_recursive(tree, 'A'))  # infinite recursion
print(tp11.dfs_recursive_enh(tree, 'A'))  # perfect recursion
print(tp11.dfs_recursive_enh_sol(tree, 'A', 'C'))  # perfect recursion with 1 sol
print(tp11.dfs_recursive_enh_multi_sol(tree, 'A', ['B', 'E']))  # perfect recursion, first solution


