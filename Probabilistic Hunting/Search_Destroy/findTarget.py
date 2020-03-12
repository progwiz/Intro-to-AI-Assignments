import random
import numpy as np
import sys

global curr_path

global total_cost

# the main search function
def findTarget(landscape, target, rule, typ="stationary"):
    global total_cost
    total_cost=1
    global curr_path
    curr_path=[]
    searches = 0
    probability = [0.1,0.3,0.7,0.9]
    belief = np.full((landscape.shape[0], landscape.shape[1]),1/(landscape.shape[0]*landscape.shape[1]), dtype = np.float64)
    i,j= 0,0
    while True:
        searches += 1
        i,j = maxBelief(landscape, belief, rule, (i,j), typ)
        #sys.stdout.write("\r searches: "+str(searches)+" max: "+str(i)+","+str(j)+" target: "+ str(target) +" belief: "+str(belief[(i,j)]))
        if((i,j) == target):
            if(random.uniform(0,1) < (1-probability[landscape[i][j]])):
                return searches
        belief[i][j] = belief[i][j] * probability[landscape[i][j]]
        beta = 1 / np.sum(belief)
        belief = belief * beta
        if typ!="stationary":
            #move target
            move_type=[]
            move_type.append(landscape[target])
            nbrs=get_nbrs(target, landscape)
            ind=random.randint(0,len(nbrs)-1)
            target=nbrs[ind]
            move_type.append(landscape[target])
            
            # update beliefs using moving target information
            new_belief=np.zeros(belief.shape,dtype=np.float64)
            non_zeros=np.transpose(np.nonzero(belief))
            non_zeros=[tuple(non_zero) for non_zero in non_zeros]
            for non_zero_index in non_zeros:
                if landscape[non_zero_index] in move_type:
                    nbrs=get_nbrs(non_zero_index,landscape)
                    valid_nbrs=[nbr for nbr in nbrs if landscape[nbr] in move_type]
                    for valid_nbr in valid_nbrs:
                        new_belief[valid_nbr]+=(belief[non_zero_index]/len(valid_nbrs))
            belief=new_belief
            beta=1/np.sum(belief)
            belief=belief*10
            belief = belief * beta
        

#returns left, right, top, bottom neighbor
def get_nbrs(loc, landscape):
    x,y=loc
    nbrs=[]
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        nbr_x,nbr_y=x+dx, y+dy
        if 0<=nbr_x<landscape.shape[0] and 0<=nbr_y<landscape.shape[1]:
            nbrs.append((nbr_x,nbr_y))
    return nbrs

# returns manhattan distance
def manhattan(loc1,loc2):
    return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1])

# gets the path from p1 to p2 with maximum belief 
def get_best_path(p1,p2, belief):
    
    m1=p2[0]-p1[0]
    if m1:
        m1=int(m1/abs(m1))
    m2=p2[1]-p1[1]
    if m2:
        m2=int(m2/abs(m2))
        
    paths=[[(p1[0]+m1*1,p1[1])],[(p1[0],p1[1]+m2*1)]]
    
    for i in range(abs(p1[0]-p2[0])+abs(p1[1]-p2[1])-1):
        new_paths=[]
        for path in paths:
            x,y=path[-1]
            d=[]
            if x!=p2[0]:
                d.append((m1*1,0))
            if y!=p2[1]:
                d.append((0,m2*1))
            for dx,dy in d:
                next_point = [(x+dx,y+dy)]
                new_path = path+next_point
                new_paths.append(new_path)
        paths=new_paths
    costs=[np.sum([belief[loc] for loc in path]) for path in paths]
    return paths[np.argmax(costs)]


def rule3_2(current, belief, landscape):
    nbrs=get_nbrs(current, landscape)
    costs=[]
    for nbr in nbrs:
        s1=0
        s2=0
        for x in range(landscape.shape[0]):
            for y in range(landscape.shape[1]):
                if nbr!=(x,y):
                    s1+=(belief[x,y]*manhattan(nbr,(x,y)))
                    s2+=belief[x,y]
        costs.append(s1/s2)
    print(min(costs), nbrs[np.argmin(costs)], belief[x,y])
    return (nbrs[np.argmin(costs)])

def maxBelief(landscape, belief, rule, current, typ="stationary"):
    """
    The function accepts the landscape and belief matrix and returns the index
    of the cell with the maximum belief to be considered for exploration
    in the next iteration
    Rule 1 : The terrain type won't matter --> P(cell containing a target)
    Rule 2 : The terrain type will matter --> P(finding a target in a cell)
    Rule 3 : Search by moving only one step at a time.
    """
    max = -1
    x,y = 0,0
    terrain = [0.1,0.3,0.7,0.9]
    if rule == 1:
        for i in range(0, len(landscape)):
            for j in range(0, len(landscape)):
                if belief[i][j] > max:
                    max = belief[i][j]
                    x = i
                    y = j
    elif rule==2:
        for i in range(0, len(landscape)):
            for j in range(0, len(landscape)):
                if((belief[i][j] * (1 - terrain[landscape[i][j]])) > max):
                    max = (belief[i][j] * (1 - terrain[landscape[i][j]]))
                    x = i
                    y = j
    
    elif rule==3:
        #x,y = rule3_2(current, belief, landscape)
        
        global curr_path
        if not(len(curr_path)):
            for i in range(0, len(landscape)):
                for j in range(0, len(landscape)):
                    if (i,j)!=current:
                        val=(belief[i][j]* terrain[landscape[i,j]])/manhattan(current,(i,j))
                        if(val > max):
                            max = val
                            x = i
                            y = j
        
        #nbrs=get_nbrs(current, landscape)
        #x,y = min(nbrs, key = lambda l: manhattan(l,(x,y)))
        global total_cost
        total_cost+=(manhattan((x,y),current)+1)
        
    return x,y
