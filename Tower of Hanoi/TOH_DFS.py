# Depth first search method to search end state from start state
initial_State = []
end_State = []
marked = [] # keeps tracks of the nodes that have been visited.
children = []
found = False

#find_path finds the next set of possible moves from the current state.
def find_path(state):
    if found:
        return children
    if state[0]: # if first peg is empty
        if found:
            return children
        if not state[1]:
            child = [state[0][1:],[state[0][0]],state[2]]
            managetrace(child)
        else:
            
            if state[1][0] > state[0][0]:
                child = [state[0][1:],[state[0][0]] + state[1],state[2]]
                managetrace(child)
        
        if not state[2]:
            child = [state[0][1:],state[1],[state[0][0]]]
            managetrace(child)
        
        else:
            if state[2][0] > state[0][0]:
                child = [state[0][1:],state[1],[state[0][0]] + state[2]]
                managetrace(child)
        
    if state[1]: # if second peg is empty
        if found:
            return children
        if not state[0]:
            child= [[state[1][0]],state[1][1:],state[2]]
            managetrace(child)
        
        else:
            if state[0][0] > state[1][0]:
                child = [[state[1][0]] + state[0],state[1][1:],state[2]]
                managetrace(child)
        
        if not state[2]:
            child = [state[0],state[1][1:],[state[1][0]]]
            managetrace(child)
        
        else:
            if state[2][0] > state[1][0]:
                child = [state[0],state[1][1:],[state[1][0]] + state[2]]
                managetrace(child)
        
    if state[2]: # if third peg is empty
        if found:
            return children
        if not state[0]:
            child= [[state[2][0]],state[1],state[2][1:]]
            managetrace(child)
        else:
            if state[0][0] > state[2][0]:
                child = [[state[2][0]] + state[0],state[1],state[2][1:]]
                managetrace(child)
        
        if not state[1]:
            child = [state[0],[state[2][0]],state[2][1:]]
            managetrace(child)
        
        else:
            if state[1][0] > state[2][0]:
                child = [state[0],[state[2][0]] + state[1],state[2][1:]]
                managetrace(child)
    return children

       
def managetrace(child): # managetrace appends the child node and checks if the end node has reached else find the next possible node.
    children.append(child)
    if child not in marked:
        marked.append(child)
        if child == end_State:
            found = True
            print_path(children)
            print("End State reached")
        find_path(child)

def print_path(children): # prints the output/trace after each move.
    total_child = 0
    for child in children:
        print child
        total_child = total_child + 1
    print "Total number of moves using Depth first search : ",
    print total_child
        
def start_dfs(initial_state, end_state):
    global initial_State
    global end_State
    global found
    initial_State = initial_state
    end_State = end_state
    marked.append(initial_State)
    children.append(initial_State)
    found = False
    find_path(initial_State)
