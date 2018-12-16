from Npuzzle.NPzl import *
import timeit


input = input('enter the puzzle to solve\n')
temp_list = input.split(",")

for element in temp_list:
    initial_state.append(int(element))

start = timeit.default_timer()

bfs(initial_state)

stop = timeit.default_timer()

print_res(stop-start)
