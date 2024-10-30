#Quiz 3.
#This is quiz 3. This code was copy/pasted from the notes. The objects and capacity were changed.
def tabular_knapsack(objects, W):
    #Expects objects to be a list of pairs of the form (value,weight)
    n = len(objects)
    # we'll rely on indices to also represent weights, so we'll index from 0...W 
    # in the weight dimension of the table
    OPT = [[0]*(W+1)]#Temporarily fill in the row with 0's.
    
    # initialize the first row of the table
    for w in range(W+1):
        if objects[0][1] <= w:
            OPT[0][w] = objects[0][0]
        else:
            OPT[0][w] = 0
    # use the optimal substructure property to compute increasingly larger solutions
    for i in range(1,n):
        OPT.append([0]*(W+1)) #Temporarily fill in the row with 0's.
        v_i, w_i = objects[i]
        for w in range(W+1):
            if w_i <= w:
                OPT[i][w] = max(v_i + OPT[i-1][w-w_i], OPT[i-1][w])
            else:
                OPT[i][w] = OPT[i-1][w]
               
    [print(o) for o in OPT]
    return OPT[n-1][W]
W = 7
objects = ((10,5), (6,4), (1,1), (3,2), (7,2),) #objects are represented by tuples, (value, weight)
print(tabular_knapsack(objects, W))