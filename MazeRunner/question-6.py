from maze_generator import *
from maze_plot import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
from time import time

#Function to find the average no. of nodes expanded by A* using Manhattan and Euclid Heuristics

def question6() :
    maze_dimension = 200
    n = 50
    probability = [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4]
    manhattan_avg = []
    euclid_avg = []
    for p in probability:
    
        manhattan_nodes = 0
        euclid_nodes = 0

        for count in range(n):

            maze=maze_generator(maze_dimension,p)
            expanded_nodes3 = a_star(maze,"euclid",display=False)[1]
            expanded_nodes4 = a_star(maze,"manhattan",display=False)[1]
            manhattan_nodes = manhattan_nodes + len(expanded_nodes4)
            euclid_nodes = euclid_nodes + len(expanded_nodes3)
    
        manhattan_avg.append(manhattan_nodes/n)
        euclid_avg.append(euclid_nodes/n)


    plt.plot(probability , manhattan_avg , label = "MANHATTAN")
    plt.plot(probability , euclid_avg , label = "EUCLID")
    plt.ylabel('Nodes Expanded')
    plt.xlabel('Probability (p)')
    plt.legend()
    plt.show()

if __name__=="__main__":
    question6()

