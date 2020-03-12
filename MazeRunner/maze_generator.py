"""
This program generates a maze of the given dimensions based on the
entered dimension for the maze and the probability value.
"""

import random
import numpy as np
from maze_plot import *
from depth_first_search import *

def maze_generator(maze_dimension, maze_probability):
    data = np.zeros((maze_dimension, maze_dimension), dtype = np.int8)

    for i in range(maze_dimension):
        for j in range(maze_dimension):
            if random.random() <= maze_probability:
                data[i][j] = 1
    data[0][0] = 0
    data[maze_dimension-1][maze_dimension-1] = 0
    return data


def max_dfs_path(maze_dimension):
    data= np.zeros((maze_dimension, maze_dimension), dtype= np.int8)
    for i in range(0,maze_dimension-1):
        data[i,:]=0
    for i in range(1,maze_dimension-1):
        data[i,1]=1
    for j in range(1,maze_dimension):
        data[-2,j]=1
    data[:,0]= 0
    data[-1,:]= 0
    data[1,1]=0
    data[0,0]=data[-1,-1]=0
    return data

def max_dfs_expanded(maze_dimension):
    data= np.zeros((maze_dimension, maze_dimension), dtype= np.int8)
    for i in range(0,maze_dimension-1):
        data[i,:]=-1
    for i in range(1,maze_dimension-1):
        data[i,1]=1
    for j in range(1,maze_dimension):
        data[-2,j]=1
    data[:,0]= -2
    data[-1,:]= -2
    return data

if __name__=="__main__":
    dfs_path = max_dfs_path(200)
    sf, expanded, path, fringe = depth_first_search(dfs_path, display=True, sol_path="figs/worst-case/dfs", figname="path" )
    print(len(path), fringe)
    max_dfs = max_dfs_expanded(200)
    plot_maze(max_dfs, path="figs/worst-cases/", figname="dfs-worst-expanded")