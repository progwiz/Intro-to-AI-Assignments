from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time

#Set -1 for traversed Elements

maze_probability = 0.2
maze_dimension = 100
#maze = maze_generator(maze_dimension, maze_probability)
maze=maze_generator(maze_dimension,0)
t=time()

#change diplay to True to see the image of the path.
#change second paramater of a_star to either "euclid" or "manhattan"

#### each of the search algorithm returns 
#### i) success_flag: 1 indicates goal was found, 0 indicates otherwise.
#### ii) expanded_nodes: numpy array which holds the list of nodes that were explore/expanded.
#### iii) final_path: numpy array which holds the list of nodes that belong to the path from start to goal.
#### iv) fringe: maximum size of the fringe at any point during the algorithm.  
####                  The array is empty if success_flag is 0.

#success_flag, expanded_nodes1, final_path1, fringe1 = depth_first_search(maze)
success_flag, expanded_nodes2, final_path, fringe2 = a_star(maze,"euclid")
success_flag, expanded_nodes3, final_path, fringe3 = a_star(maze,"manhattan")
success_flag, expanded_nodes4, final_path1, fringe4 = breadth_first_search(maze)

print(fringe2, fringe3, fringe4 )
print("running time: ", time()-t)