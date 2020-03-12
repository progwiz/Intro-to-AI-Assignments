import matplotlib.pyplot as plt
from maze_plot import *
from get_neighbors import *
from breadth_first_search import *
import math
import numpy as np
import heapq
import matplotlib.pyplot as plt

def euclidean_distance(a_star_maze):
    euclid_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = np.int16)
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)    
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            euclid_heuristic[i,j] = math.sqrt(math.pow((x - i), 2)+ math.pow((y-j),2))
    return euclid_heuristic

def manhattan_distance(a_star_maze):

    manhattan_heuristic = np.zeros((len(a_star_maze), len(a_star_maze)), dtype = np.int16)
    (x, y) = (len(a_star_maze)-1, len(a_star_maze)-1)
    for i in range(len(a_star_maze)):
        for j in range(len(a_star_maze)):
            manhattan_heuristic[i,j] = abs(x-i)+abs(y-j)
    return manhattan_heuristic

def a_star(a_star_maze,h, display=False, sol_path="figs/", figname="-recent"):
    a_star_maze=a_star_maze.copy()
    source = (0,0)
    goal = (len(a_star_maze)-1, len(a_star_maze)-1)
    if h=="euclid":
        heuristic = euclidean_distance(a_star_maze)
    else:
        heuristic = manhattan_distance(a_star_maze)
    
    # the parent array holds the parent of each child node. 
    a_star_parent=np.full((len(a_star_maze),len(a_star_maze),2),-1,dtype=np.int16)
    
    a_star_p_queue = []
    heapq.heappush(a_star_p_queue, (np.int16(heuristic[source]),np.int16(0),(np.int16(source[0]),np.int16(source[1]))))
    a_star_expanded=np.empty((0,2), dtype=np.int16)
    max_fringe=1
    while len(a_star_p_queue):

        cur_heuristic, cur_cost, cur_node = heapq.heappop(a_star_p_queue)
        cur_node=tuple(cur_node)
        if a_star_maze[cur_node]==-1: continue
        a_star_expanded=np.append(a_star_expanded, np.array([cur_node], dtype=np.int16), axis=0)
        
        # if current node is goal, return success.
        if np.array_equal(cur_node, goal):
            # if goal is reached, deduce the path using the parent array.
            current=goal   
            a_star_path=np.array([goal], dtype=np.int16)
            while not(np.array_equal(a_star_parent[current],[-1,-1])):
                a_star_path=np.append(a_star_path,np.array([a_star_parent[current]], dtype=np.int16), axis=0)
                current=tuple(a_star_parent[current])
             
            # if display is true, plot the path onto image and display it.
            if display:
                print("Path found!")
                for node in a_star_path:
                    a_star_maze[tuple(node)]=-2
                    #bfs_path(bfs_maze, cur_node, bfs_parent)
                plot_maze(a_star_maze,"Astar-"+h, sol_path, figname)
                
            return 1, a_star_expanded, a_star_path, max_fringe
        
        # add neighbors to priortiy queue.
        neighbors = traversable_neighbors(a_star_maze, cur_node)
        for node in neighbors:
            (i,j) = node
            if np.array_equal(a_star_parent[i][j], (-1,-1)):
                a_star_parent[i][j] = np.array(cur_node, dtype=np.int16)
                heapq.heappush(a_star_p_queue, (np.int16(heuristic[i,j]+cur_cost),np.int16(cur_cost+1),(np.int16(node[0]),np.int16(node[1]))))
        
        a_star_maze[cur_node] = -1
        if max_fringe<len(a_star_p_queue):
            max_fringe=len(a_star_p_queue)
    # if priority queue is empty and goal wasn't reached, return failure.
    if display:
        print("No Path found :(")
        plot_maze(a_star_maze,"Astar-"+h, sol_path, figname)
    return 0, a_star_expanded, [], max_fringe
