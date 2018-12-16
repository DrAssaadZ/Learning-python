from TP import tp11

# turn the file content into a dict
with open('queens.txt', 'r') as File:  # use 'rU' instead of 'r' if there is a problem
    tree = {}
    for line in File:
        line = line.split()
        if not line:  # case of empty line
            continue
        tree[line[0]] = line[1:]

# print the resulted dict
for i in tree:
    print("'" + i + "':", tree[i], ",")

# find the solution
# solutions: '0100000110000010' && '0010100000010100'
tp11.dfs_goal_w_path(tree, 'S', '0100000110000010')
