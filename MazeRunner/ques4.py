from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
import numpy as np
import matplotlib.pyplot as plt

def ques4(n):
# This function calculates the average length of the path for a certain dimension for all p
# For each value of p, the function takes an average of n mazes
# The output is a graph which contains the average length as the value for a key 'p'
    print("Question 4 has started.....")
    dfs_avg = {}
    bfs_avg = {}
    a_euclid_avg = {}
    a_manhattan_avg = {}

    p_values = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    for p in p_values:
        dim = 200

        dfs_lengths=[]
        bfs_lengths=[]
        a_euclid_lengths=[]
        a_manhattan_lengths=[]
        dfs_count=0
        bfs_count=0
        a_euclid_count=0
        a_manhattan_count=0
        for rep in range(n):
            maze = maze_generator(dim, p)
            dfs_count = len(depth_first_search(maze, display = False)[2])
            dfs_lengths.append(dfs_count)

            bfs_count = len(breadth_first_search(maze, display = False)[2])
            bfs_lengths.append(bfs_count)

            a_euclid_count = len(a_star(maze, "euclid", display = False)[2])
            a_euclid_lengths.append(a_euclid_count)

            a_manhattan_count = len(a_star(maze,"manhattan", display = False)[2])
            a_manhattan_lengths.append(a_manhattan_count)


        if dfs_lengths:
            dfs_avg[p] = np.mean(dfs_lengths)
#        print("DFS AVERAGE LENGTHS for p = {}".format(p))
#        if p in dfs_avg.keys():
#            print(dfs_avg[p])



        if bfs_lengths:
            bfs_avg[p] = np.mean(bfs_lengths)
#        print("BFS AVERAGE LENGTHS for p = {}".format(p))
#        if p in bfs_avg.keys():
#            print(bfs_avg[p])


        if a_euclid_lengths:
            a_euclid_avg[p] = np.mean(a_euclid_lengths)
#        print("A* Euclidean distance AVERAGE LENGTHS for p = {}".format(p))
#        if p in a_euclid_avg.keys():
#            print(a_euclid_avg[p])



        if a_manhattan_lengths:
            a_manhattan_avg[p] = np.mean(a_manhattan_lengths)
#        print("A* Manhattan distance AVERAGE LENGTHS for p = {}".format(p))
#        if p in a_manhattan_avg.keys():
#            print(a_manhattan_avg[p])

    fig = plt.figure()
    axes = fig.add_axes([0,0,1,1])
    axes.plot(dfs_avg.keys(),list(dfs_avg.values()),label = 'dfs')
    axes.plot(bfs_avg.keys(),list(bfs_avg.values()),'r',label = 'bfs')
    axes.plot(a_euclid_avg.keys(),list(a_euclid_avg.values()),'b', label = 'a_euclid')
    axes.plot(a_manhattan_avg.keys(),list(a_manhattan_avg.values()),color = 'orange',label = 'a_manhattan')
    axes.set_xlim([0,1])
    axes.legend()
    plt.show()



if __name__=="__main__":
    ques4(2)
