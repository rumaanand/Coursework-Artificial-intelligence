# Best first method to search an end state from start state
initial_State = []
end_State = []
marked = []
count = 0
found = False
def perform_bestfirst(currentState): # main method to print trace after finding the best option at every level 
    global count
    global found
    if found:
        return found
    print currentState
    count = count+1
    bestOption = currentState
    if bestOption == end_State:
        found = True
        print("End State reached")
        print 'Total number of moves using best first search: ',
        print count
        return found
    else:
         children = find_path(bestOption)
         bestOption=find_bestOption(children)
         marked.append(bestOption)
         perform_bestfirst(bestOption)
    return found

#this method is used to find the value that is closest to the solution by calculating the heuristic value of all the possible options and choosing the option with minimum heuristic value.
def find_bestOption(children): 
    minVal = 999999
    bestChild= None
    for child in children:
        if child not in marked:
            # Heuristic approach - computes the sum of the difference between number of discs and also value of disc in the current state and end state for each peg.
            optionValue = abs(sum(child[0]) - sum(end_State[0])) + abs(sum(child[1]) - sum(end_State[1])) + abs(sum(child[2]) - sum(end_State[2])) + abs(len(child[0]) - len(end_State[0]))
            + abs(len(child[1]) - len(end_State[1])) + abs(len(child[2]) - len(end_State[2]))
            if(optionValue < minVal):
                bestChild = child
    return bestChild

def find_path(state): # find_path finds the next set of possible moves from the current state.
    children = []
    if state[0]: # if first peg is empty
        if not state[1]:
            child = [state[0][1:],[state[0][0]],state[2]]
            managechildren(child, children)
        else:
            
            if state[1][0] > state[0][0]:
                child = [state[0][1:],[state[0][0]] + state[1],state[2]]
                managechildren(child, children)
        
        if not state[2]:
            child = [state[0][1:],state[1],[state[0][0]]]
            managechildren(child, children)
        
        else:
            if state[2][0] > state[0][0]:
                child = [state[0][1:],state[1],[state[0][0]] + state[2]]
                managechildren(child, children)
        
    if state[1]: # if second peg is empty
        if not state[0]:
            child= [[state[1][0]],state[1][1:],state[2]]
            managechildren(child, children)
        
        else:
            if state[0][0] > state[1][0]:
                child = [[state[1][0]] + state[0],state[1][1:],state[2]]
                managechildren(child, children)
        
        if not state[2]: 
            child = [state[0],state[1][1:],[state[1][0]]]
            managechildren(child, children)
        
        else:
            if state[2][0] > state[1][0]:
                child = [state[0],state[1][1:],[state[1][0]] + state[2]]
                managechildren(child, children)
        
    if state[2]: # if third peg is empty
        if not state[0]:
            child= [[state[2][0]],state[1],state[2][1:]]
            managechildren(child, children)
        else:
            if state[0][0] > state[2][0]:
                child = [[state[2][0]] + state[0],state[1],state[2][1:]]
                managechildren(child, children)
        
        if not state[1]:
            child = [state[0],[state[2][0]],state[2][1:]]
            managechildren(child, children)
        
        else:
            if state[1][0] > state[2][0]:
                child = [state[0],[state[2][0]] + state[1],state[2][1:]]
                managechildren(child, children)
    return children
       
def managechildren(child, children): # managechildren appends the child node.
    if child not in marked:
        children.append(child)
        
def start_bestfirst(initial_state, end_state):
    global initial_State
    global end_State
    global count
    global found
    initial_State = initial_state
    end_State = end_state
    marked.append(initial_State)
    count = 0
    found = False
    perform_bestfirst(initial_State)
    
