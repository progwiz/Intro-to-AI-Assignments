from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time

#Function to find average number of nodes expanded for DFS and BFS for p < p0
def question7() :
    maze_dimension = 20
    n = 5
    probability = [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4]
    dfs_avg = []
    bfs_avg = []
    for p in probability:
    
        dfs_nodes = 0
        bfs_nodes = 0

        for count in range(n):

            maze=maze_generator(maze_dimension,p)


            expanded_nodes3 = depth_first_search(maze,display=False)[1]

            expanded_nodes4 = breadth_first_search(maze,display=False)[1]


            bfs_nodes = bfs_nodes + len(expanded_nodes4)
            dfs_nodes = dfs_nodes + len(expanded_nodes3)
    
        dfs_avg.append(dfs_nodes/n)
        bfs_avg.append(bfs_nodes/n)


    plt.plot(probability , dfs_avg , label = "DFS")
    plt.plot(probability , bfs_avg , label = "BFS")
    plt.ylabel('Nodes Expanded')
    plt.xlabel('Probability(p)')
    plt.legend()
    plt.show()

if __name__=="__main__":
    question7()


