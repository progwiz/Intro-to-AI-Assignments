import matplotlib.pyplot as plt
from maze_plot import *
from get_neighbors import *
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def breadth_first_search(bfs_maze,display=False, sol_path="figs/", figname="-recent"):
    bfs_maze=bfs_maze.copy()
    source = (0,0)
    goal = (len(bfs_maze)-1, len(bfs_maze)-1)
    bfs_queue=np.array([source], dtype=np.int16)
    bfs_expanded=np.empty((0,2), dtype=np.int16)
    bfs_parent= np.full((bfs_maze.shape[0], bfs_maze.shape[0],2), -1, dtype=np.int16)
    max_fringe=1
    while len(bfs_queue):
        
        cur_node, bfs_queue = bfs_queue[0], bfs_queue[1:]
        if bfs_maze[tuple(cur_node)]==-1: continue
        bfs_expanded=np.append(bfs_expanded, np.array([cur_node],dtype=np.int16), axis=0)
        bfs_maze[tuple(cur_node)] = -1
        
        # if current node is goal, return success.
        if np.array_equal(cur_node, goal):
            # if goal is reached, deduce the path using the parent array
            current=goal   
            bfs_path=np.array([goal], dtype=np.int16)
            while not(np.array_equal(bfs_parent[current],[-1,-1])):
                bfs_path=np.append(bfs_path,np.array([bfs_parent[current]], dtype=np.int16), axis=0)
                current=tuple(bfs_parent[current])
             
            # if display is true, plot the path onto image and display it.
            if display:
                print("Path found!")
                for node in bfs_path:
                    bfs_maze[tuple(node)]=-2
                    #bfs_path(bfs_maze, cur_node, bfs_parent)
                plot_maze(bfs_maze,"BFS", sol_path, figname)
                
            return 1, bfs_expanded, bfs_path, max_fringe
            
        neighbors = traversable_neighbors(bfs_maze, cur_node)
        for neighbor in neighbors:
            # if no parent is assigned to child node, it is neither explore nor in queue.
            i,j = neighbor
            if np.array_equal(bfs_parent[i][j], (-1,-1)):
                bfs_parent[i][j] = cur_node
                bfs_queue= np.append(bfs_queue, np.array([neighbor], dtype=np.int16), axis=0)
        if max_fringe<len(bfs_queue):
            max_fringe=len(bfs_queue)
    # queue is exmpty and no path was found, return failure.
    if display:
        print("No Path Found :(")
        plot_maze(bfs_maze,"BFS", sol_path,figname)
    return 0,bfs_expanded, [], max_fringe
