from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
import numpy as np
import pickle
import math
import sys
import os
import matplotlib.pyplot as plt


#round no. to 3 decimal places.
def round_no(x):
    return math.ceil(x * 1000.0) / 1000.0

# This function computes the graphs for question 1.
# The graphs are saved in figs/graphs/q1
def question1():
    algos=["DFS","BFS","Astar-Euclidean","Astar-Manhattan"]
    P=list(np.arange(0,1.1,0.1))
    final_stats={}
    for algo in algos:
        stats={}
        for p in P:
            dim=100
            vals={}
            while dim<2500:
                flag=0
                success_count=0
                times=[]
                for i in range(30):
                    sys.stdout.write("\r algo: %s p: %f dim %i rep: %i" %(algo, p, dim, i))
                    maze=maze_generator(dim, p)
                    t=time()
                    if algo=="BFS":
                        sf,en,path=breadth_first_search(maze, display=False)
                    if algo=="DFS":
                        sf,en,path=depth_first_search(maze, display=False)
                    if algo=="Astar-Euclidean":
                        sf,en,path=a_star(maze,"euclid", display=False)
                    if algo=="Astar-Manhattan":
                        sf,en,path=a_star(maze,"manhattan",display=False)
                    exec_time=time()-t
                    success_count+=sf
                    if exec_time>60:
                        flag=1
                        break
                    else:
                        times.append(exec_time)
                if flag:
                    break
                else: 
                    vals[dim]=[np.max(times),success_count]
                dim+=100
            stats[p]=vals
        final_stats[algo]=stats
      
    #plot max-dimension vs P graph for all algorithms. 
    
    path="figs/graphs/q1/"
    os.makedirs(path,exist_ok=True)
    
    figno+=1
    plt.figure(figno)
    colors=["red","green","blue","black"]
    plt.xlabel("P")
    plt.ylabel("Max Dimension")
    
    STATS={}
    file_string=""
    for algo_no,algo in enumerate(algos):
        file_string+=(algo+":\n")
        PSTATS={}
        MAXDIMS=[]
        for p, p_stats in final_stats[algo].items():
            DIMS=[]
            TIMES=[]
            for dim, dim_stats in p_stats.items():
                DIMS.append(dim)
                TIMES.append(dim_stats[0])
            PSTATS[p]=[DIMS,TIMES]
            max_dim=np.max(list(p_stats.keys()))
            MAXDIMS.append(max_dim)
            t, count=p_stats[max_dim]
            file_string+=("\n---P:"+str(p)+"Max dimension:"+str(max_dim))
        file_string+="\n\n"
        STATS[algo]=PSTATS
        plt.plot(P,MAXDIMS,color=colors[algo_no])
    with open("data/q1.txt","w") as f:
        f.write(file_string)
    plt.legend(tuple(algos),loc="upper right")
    plt.title("Max Dimensions for time<60s")
    plt.savefig(path+"All - P vs max-dim.jpg")
    
    #write individual running time graphs

    colors=["blue","red","green","maroon","brown","olive","teal","purple","magenta","cyan","orange"]
    legend=tuple(["p="+str(p) for p in P])
    for algo in algos:
        figno+=1
        plt.figure(figno)
        for p,p_stats in STATS[algo].items():
            plt.plot(p_stats[0],p_stats[1],color=colors[int(p*10)])
        plt.axhline(y=60, color="black")
        plt.xlabel("Dimension")
        plt.ylabel("Time")
        plt.legend(legend,loc="lower right")
        plt.title(algo)
        plt.savefig(path+algo+"-dim vs t.jpg")

# This function creates the images for question 2
# The images are saved as figs/"BFS/DFS/Astar"-recent.jpg
def question2(dim=100, p=0.2):
    sf=0
    while not(sf):
        maze=maze_generator(dim,p)
        sf, expanded_nodes1, final_path1, fringe1 = a_star(maze, "manhattan")

    sf, expanded_nodes1, final_path1, fringe1 = depth_first_search(maze,True)
    sf, expanded_nodes2, final_path, fringe2 = a_star(maze,"euclid",True)
    sf, expanded_nodes3, final_path, fringe3 = a_star(maze,"manhattan",True)
    sf, expanded_nodes4, final_path1, fringe4 = breadth_first_search(maze,True)

    
# this function computes the graph for q3
# the graph is saved to figs/graphs/q3
def question3(dim=200):
    P=list(np.arange(0,1.01,0.05))
    trials=1000
    success_avg=[]
    for p in P:
        count=0
        for i in range(trials):
            sys.stdout.write("\r p: %f rep: %f" %(p,i))
            maze=maze_generator(dim,p)
            if p<0.1:
                sf,en,path=depth_first_search(maze,display=False)
            elif p>=0.5:
                sf,en,path=breadth_first_search(maze,display=False)
            else:
                sf,en,path=a_star(maze,"euclid",display=False)
            count+=sf
        success_avg.append(count/trials)
          
    
    path="figs/graphs/q3/"
    os.makedirs(path,exist_ok=True)
    figno=0
    plt.figure(figno)
    plt.plot(P,success_avg)
    plt.xlabel("P")
    plt.ylabel("Probability of there existing a path to the goal")
    plt.title("Question 3")
    plt.savefig(path+"p vs success_prob.jpg")
    
        
if __name__=="__main__":
    #question1()
    question2()
    #question3()