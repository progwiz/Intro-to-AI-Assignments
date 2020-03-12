from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time
import numpy as np
import matplotlib.pyplot as plt

def ques5(n):
    print("Question 5 has started.....")
    dfs_avg = {}
    a_euclid_avg = {}
    a_manhattan_avg = {}

    p_values = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    for p in p_values:
        dim = 200

        dfs_lengths=[]
        a_euclid_lengths=[]
        a_manhattan_lengths=[]
        dfs_count=0
        a_euclid_count=0
        a_manhattan_count=0
        for rep in range(n):
            maze = maze_generator(dim, p)
            dfs_count = len(depth_first_search(maze, display = False)[2])
            dfs_lengths.append(dfs_count)

            a_euclid_count = len(a_star(maze, "euclid", display = False)[2])
            a_euclid_lengths.append(a_euclid_count)

            a_manhattan_count = len(a_star(maze,"manhattan", display = False)[2])
            a_manhattan_lengths.append(a_manhattan_count)


        if dfs_lengths:
            dfs_avg[p] = np.mean(dfs_lengths)
#        print("DFS AVERAGE LENGTHS for p = {}".format(p))
#        if p in dfs_avg.keys():
#            print(dfs_avg[p])

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

    fig1 = plt.figure()
    axes1 = fig1.add_axes([0,0,1,1])
    axes1.plot(dfs_avg.keys(),list(dfs_avg.values()),label = 'dfs')
    axes1.plot(a_euclid_avg.keys(),list(a_euclid_avg.values()),'b', label = 'a_euclid')
    axes1.plot(a_manhattan_avg.keys(),list(a_manhattan_avg.values()),color = 'orange',label = 'a_manhattan')
    axes1.legend()
    plt.show()

if __name__=="__main__":
    ques5(2)
