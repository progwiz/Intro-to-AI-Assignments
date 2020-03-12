# The main function of this file computes the mazes asked for in Q10. 
# The mazes generated are saved to figs/question2

import numpy as np
from maze_generator import *
from depth_first_search import *
from breadth_first_search import *
from a_star import *
import itertools
import  matplotlib.pyplot as plt
import sys 
import os
import pickle

# combine maze_count mazes to give total of maze_count + maze_countC4 * fact(4) new mazes
def crossover(mazes,dim, maze_count):
    sys.stdout.write("\r \n ------Performing Crossover operation")
    for i in range(maze_count-3):
        for j in range(i+1,maze_count-2):
            for k in range(j+1,maze_count-1):
                for l in range(k+1,maze_count):
                    crossover_mazes=[mazes[i],mazes[j],mazes[k],mazes[l]]
                    for permutation in list(itertools.permutations(list(np.arange(4)))):
                        new_maze=np.zeros((dim,dim), dtype=np.int8)
                        half_dim=int(dim/2)
                        new_maze[:half_dim,:half_dim]=crossover_mazes[permutation[0]][:half_dim,:half_dim]
                        new_maze[:half_dim,half_dim:]=crossover_mazes[permutation[1]][:half_dim,half_dim:]
                        new_maze[half_dim:,:half_dim]=crossover_mazes[permutation[2]][half_dim:,:half_dim]
                        new_maze[half_dim:,half_dim:]=crossover_mazes[permutation[3]][half_dim:,half_dim:]
                        mazes.append(new_maze)
    return mazes

# randomly add 1s and 0s to the maze_countC4 * fact(4) mazes
def mutations(mazes,maze_count,dim,mutation_count):
    sys.stdout.write("\r ------ Performing mutation operation            ")
    new_mazes=[]
    for maze_no,maze in enumerate(mazes[maze_count:]):
        new_maze=maze.copy()
        zero_count=int(np.random.random()*mutation_count)
        one_count=mutation_count-zero_count
        for _ in range(one_count):
            mutation_loc=np.random.choice(np.arange(1,dim),2)
            new_maze[tuple(mutation_loc)]=1
        for _ in range(zero_count):
            mutation_loc=np.random.choice(np.arange(1,dim),2)
            new_maze[tuple(mutation_loc)]=0
        flag=0
        for maze in mazes:
            if np.array_equal(maze, new_maze):
                flag=1
                break
        if not(flag):
            new_mazes.append(new_maze)
    return mazes[:maze_count]+new_mazes

# returns either the i) no of expanded nodes, or ii) length of the path, or iii) maximum size of the fringe
def fitness_function(maze,algo,fitness_func):
    if algo=="BFS":
        sf, expanded, path, fringe=breadth_first_search(maze, display=False)
    elif algo=="DFS":
        sf, expanded, path,fringe= depth_first_search(maze, display=False)
    elif algo=="Astar-euclidean":
        sf, expanded, path,fringe= a_star(maze, "euclid", display=False)
    else:
        sf, expanded, path, fringe=a_star(maze, "manhattan", display=False)
    if sf:
        if fitness_func=="expanded":
            return (expanded.shape)[0]
        elif fitness_func=="path":
            return (path.shape)[0]
        else:
            return fringe
    else: 
        return 0
    
# Genetic algorithm is the local search algorithm used.      
# parameters:
        # dim: size of the maze. Default: 200
        # algo: Algorithm to be used. one of "BFS", "DFS", "Astar-euclidean", "Astar-manhattan". Default: DFS
        # maze_count: No. of mazes to be retained at each iteration on which the crossover opertion is performed. Default: 5
        # mutation_count: no. of mutations (random 1s and 0s) to be added. Default: 10
        # iteration_count: no. of iterations before returning a solution. Default: 10
        # fitness_func: The property to be maximized. One of "expanded", "path", "fringe". Default: "expanded"
        # init_count: Initial number of mazes to be generated. Default: 100
        # display: Whether to display the final mazes that are generated.
def genetic_algo(dim, algo, maze_count, mutation_count, iteration_count, fitness_func, init_count, display=False):
    mazes=[]
    sys.stdout.write("\r\n ---  Generating inital mazes                       ")
    for i in range(init_count):
        if i<init_count/3:
            maze=maze_generator(dim,0.1)
        elif i<init_count*2/3:
            maze=maze_generator(dim,0.2)
        else:
            maze=maze_generator(dim,0.3)
        mazes.append(maze)
    mazes.append(maze_generator(dim,0))
    new_mazes=[]
    for mn,maze in enumerate(mazes):
        flag=0
        for mn2,maze2 in enumerate(mazes):
            if mn!=mn2:
                if np.array_equal(maze,maze2):
                    flag=1
                    break
        if not(flag):
            new_mazes.append(maze)
    mazes=new_mazes
    mazes=sorted(mazes, key=lambda x: fitness_function(x,algo, fitness_func), reverse=True)
    mazes=mazes[:maze_count]    

    sys.stdout.write("\r\n Initial Mazes generated")
    for i in range(iteration_count):
        sys.stdout.write("\r \n ---Performing iteration %d" %i)
        mazes=crossover(mazes, dim, maze_count)
        mazes=mutations(mazes, maze_count, dim, mutation_count)
        mazes=sorted(mazes, key=lambda x: fitness_function(x,algo,fitness_func), reverse=True)
        mazes=mazes[:maze_count]

    mazes=mazes[:3]
    if display:
        path="figs/question2/dim="+str(dim)+",maze_count="+str(maze_count)+",mut_count="+str(mutation_count)+",iter_count="+str(iteration_count)+",init_count="+str(init_count)+"/"+str(algo)+"/"+str(fitness_func)+"/"            
        os.makedirs(path, exist_ok=True)
        for maze_no, maze in enumerate(mazes):
            
            if algo=="BFS":
                sf, expanded, p, fringe=breadth_first_search(maze, display=True, sol_path=path, figname=str(maze_no))
            elif algo=="DFS":
                sf, expanded, p,fringe= depth_first_search(maze, display=True, sol_path=path,figname=str(maze_no))
            elif algo=="Astar-euclidean":
                sf, expanded, p,fringe= a_star(maze, "euclid", display=True,sol_path=path, figname=str(maze_no))
            else:
                sf, expanded, p, fringe=a_star(maze, "manhattan", display=True, sol_path=path, figname=str(maze_no))
            
            with open(path+str(maze_no)+".pickle","wb+") as f:
                pickle.dump(maze, f)
            with open(path+str(maze_no)+".txt", "w") as f:
                f.write(str(fitness_func)+": "+str(fitness_function(maze, algo, fitness_func)))
            
    return mazes

if __name__=="__main__":
    for maze_count in [5]:
        for algo in ["Astar-manhattan"]:
            sys.stdout.write("\r\n Performing for algo "+algo)
            for func in ["path","fringe"]:
                if func == "expanded" and algo in ["BFS", "Astar-euclidean", " Astar-manhattan"]:
                    continue
                sys.stdout.write("\r\n Performing for "+func)
                genetic_algo(200,algo,maze_count, 1000, 6, func,600,True)