import matplotlib.image as mpimg
import numpy as np
from draw_line import maze

img = mpimg.imread('C:/projects/39-Pathfinding/NewStructure/maze.png')

for y in range(len(maze)):
	for x in range(len(maze)):
		if(maze[y,x] == 5):
			img[y,x] = [1,0,0]


mpimg.imsave('C:/projects/39-Pathfinding/NewStructure/output.png', img)
print('Image saved!')