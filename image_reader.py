import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('C:/projects/39-Pathfinding/NewStructure/maze.png')
image = []

start = False
end = False

for row in img:
	image_row = []
	for px in row:
		if(list(px) == [0, 0, 0]):
			image_row.append(1)
		elif(list(px) == [1, 1, 1]):
			image_row.append(0)
		elif(round(list(px)[0]) == 0 and round(list(px)[1]) == 0 and round(list(px)[2]) == 1):
			image_row.append(2)
			start = True
		elif(round(list(px)[0]) == 0 and round(list(px)[1]) == 1 and round(list(px)[2]) == 0):
			image_row.append(3)
			end = True
	image.append(image_row)

if(not start):
	raise Exception('Blue not found')
if(not end):
	raise Exception('Green not found')

print('Image Loaded!')
