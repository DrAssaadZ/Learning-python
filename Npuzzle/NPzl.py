from collections import deque


class State:

    def __init__(self, state, parent, move):

        self.state = state

        self.parent = parent

        self.move = move

        if self.state:
            self.map = ''.join(str(e) for e in self.state)


goal_state = [0, 1, 2, 3]
goal_node = State
initial_state = list()
board_len = 4
board_side = 2

nodes_visited = 0

moves = list()


def bfs(start_state):

    global goal_node

    explored, queue = set(), deque([State(start_state, None, None)])

    while queue:

        node = queue.popleft()

        explored.add(node.map)

        if node.state == goal_state:
            goal_node = node
            return queue

        neighbors = expand(node)

        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor)
                explored.add(neighbor.map)


def expand(node):

    global nodes_visited
    nodes_visited += 1

    neighbors = list()

    neighbors.append(State(move(node.state, 1), node, 1))
    neighbors.append(State(move(node.state, 2), node, 2))
    neighbors.append(State(move(node.state, 3), node, 3))
    neighbors.append(State(move(node.state, 4), node, 4))

    nodes = [neighbor for neighbor in neighbors if neighbor.state]

    return nodes


def move(state, position):

    new_state = state[:]

    index = new_state.index(0)

    if position == 1:  # Up

        if index not in range(0, board_side):

            temp = new_state[index - board_side]
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down

        if index not in range(board_len - board_side, board_len):

            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left

        if index not in range(0, board_len, board_side):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right

        if index not in range(board_side - 1, board_len, board_side):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None


def find_path():

    current_node = goal_node

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves


def print_res(time):

    global moves

    moves = find_path()

    print("\nSteps to solve: " + str(moves))
    print("Space complexity(Visited Nodes): " + str(nodes_visited))
    print("Time complexity(Running Time): " + format(time, '.8f'))
