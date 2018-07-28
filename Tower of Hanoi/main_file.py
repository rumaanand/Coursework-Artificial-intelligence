from TOH_DFS import start_dfs
from TOH_BFS import start_bfs
from TOH_BestFirstSearch import start_bestfirst

# This is the main file. Please provide a valid input and output state.
# A state is defined as a list(discs) of list(peg)
# where number represents the size of disc i.e where disc 3 > disc 2 > disc 1 is represented as 3>2>1.
# This will give he result for all three searches i.e Depth first, breadth first and best first search.

initial_state = [[1,2],[3,4],[]]
end_state = [[],[],[1,2,3,4]]

print '-----------------Start Best First Search----------------'
start_bestfirst(initial_state, end_state)
print '-----------------End Best First Search----------------'
print '***************************************************'
print '-----------------Start Depth First Search----------------'
start_dfs(initial_state, end_state)
print '-----------------End Depth First Search----------------'
print '***************************************************'
print '-----------------Start Breadth First Search----------------'
start_bfs(initial_state, end_state)
print '-----------------End Breadth First Search----------------'
