from maze_generator import * 
from breadth_first_search import *
from a_star import *
import numpy as np

if __name__ == "__main__":
    maze=maze_generator(200, 0)
    for i in range(0):
    
        loc =np.random.choice(200,2)
        maze[tuple(loc)]=1
    sf, e, p, f = a_star(maze, "euclid", display=True)