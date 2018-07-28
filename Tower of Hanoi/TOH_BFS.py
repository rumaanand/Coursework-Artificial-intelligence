# Breadth first method to search an end state from start state
initial_State = []
end_State = []
marked = []
queueBFS = []

def perform_bfs(queueBFS): # pops the top element from queue and pushes the child nodes in the queue.
    count=0    
    while queueBFS:
        count=count+1
        currentNode = queueBFS[-1]
        del queueBFS[-1]
        children = find_path(currentNode,count)
        queueBFS = children + queueBFS

def find_path(state,count): # find_path finds the next set of possible moves from the current state.
    children = []
    print state
    if state == end_State:
        print("End State reached")
        print 'Total number of moves using Breadth first search: ',
        print count
        exit()
    if state[0]: # if first peg is empty
        if not state[1]:
            child = [state[0][1:],[state[0][0]],state[2]]
            managetrace(child, children)
        else:
            
            if state[1][0] > state[0][0]:
                child = [state[0][1:],[state[0][0]] + state[1],state[2]]
                managetrace(child, children)
        
        if not state[2]:
            child = [state[0][1:],state[1],[state[0][0]]]
            managetrace(child, children)
        
        else:
            if state[2][0] > state[0][0]:
                child = [state[0][1:],state[1],[state[0][0]] + state[2]]
                managetrace(child, children)
        
    if state[1]: # if second peg is empty
        if not state[0]:
            child= [[state[1][0]],state[1][1:],state[2]]
            managetrace(child, children)
        
        else:
            if state[0][0] > state[1][0]:
                child = [[state[1][0]] + state[0],state[1][1:],state[2]]
                managetrace(child, children)
        
        if not state[2]: 
            child = [state[0],state[1][1:],[state[1][0]]]
            managetrace(child, children)
        
        else:
            if state[2][0] > state[1][0]:
                child = [state[0],state[1][1:],[state[1][0]] + state[2]]
                managetrace(child, children)
        
    if state[2]: # if third peg is empty
        if not state[0]:
            child= [[state[2][0]],state[1],state[2][1:]]
            managetrace(child, children)
        else:
            if state[0][0] > state[2][0]:
                child = [[state[2][0]] + state[0],state[1],state[2][1:]]
                managetrace(child, children)
        
        if not state[1]:
            child = [state[0],[state[2][0]],state[2][1:]]
            managetrace(child, children)
        
        else:
            if state[1][0] > state[2][0]:
                child = [state[0],[state[2][0]] + state[1],state[2][1:]]
                managetrace(child, children)
    return children
       
def managetrace(child, children): # managetrace appends the child node and checks if the end node has reached else find the next possible node.
    if child not in marked:
        marked.append(child)
        children.append(child)
        
def start_bfs(initial_state, end_state):
    global initial_State
    global end_State
    initial_State = initial_state
    end_State = end_state
    marked.append(initial_State)
    queueBFS.append(initial_State)
    perform_bfs(queueBFS)
