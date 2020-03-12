import matplotlib.pyplot as plt
import numpy as np
import os

def maze_plot(maze):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    ax.imshow(maze, cmap=cmap)
    #plt.show()
    plt.pause(0.1)

def maze_plot_final(maze):
    fig, ax = plt.subplots()
    ax.cla()
    cmap = plt.cm.get_cmap()
    cmap.set_bad("white")
    plt.xlim(-10,len(maze)+10)
    plt.ylim(len(maze)+10,-10)
    ax.imshow(maze, cmap=cmap)
    plt.draw()
    plt.savefig('figs/dfs-new.png', dpi=1000, bbox_inches='tight',)
    plt.show()


def plot_maze(maze,algo="BFS", path="figs/", figname="-recent"):
    
    os.makedirs(path, exist_ok=True)
    # create colored image from old image. 
    # 1. white color represents empty nodes.
    # 2. black color represents obstacles.
    # 3. red color represents explored nodes.
    # 4. green color represents final path.
    # 5. blue color represents start and goal.
    colors_dict={0: (255,255,255), 1: (0,0,0), -1: (255,0,0), -2: (0,255,0)}
    new_img=np.zeros((maze.shape[0],maze.shape[1],3), dtype=np.uint8)
    for x in range(maze.shape[0]):
        for y in range(maze.shape[1]):
            new_img[x,y]=colors_dict[int(maze[x,y])]
    new_img[0,0]= (0,0,255)
    new_img[-1,-1] = (0,0,255)
    
    
    plt.figure(0)
    plt.imshow(new_img)
    plt.savefig(path+algo+figname+".png", dpi=1000, bbox_inches="tight")
