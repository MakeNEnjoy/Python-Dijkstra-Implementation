import numpy as np
from operator import add
from collections import Counter
from VARS import maze, template_maze

# 0 = Can walk, 1 = Wall, 2 = Start, 3 = End, 4 = Checked, 5 = Checked and End

# Constants
MOVE_UP = [-1, 0]
MOVE_DOWN = [1, 0]
MOVE_LEFT = [0, -1]
MOVE_RIGHT = [0, 1]

def move(pos, direction):
	return tuple(list(map(add, pos, direction)))


def get_directions(pos):
	return [move(pos, MOVE_UP), move(pos, MOVE_RIGHT), move(pos, MOVE_DOWN), move(pos, MOVE_LEFT)]

nodes = []

def find_nodes(pos):

	options = []

	for direction in get_directions(pos):

		options.append(maze[direction])

		if(maze[direction] == 0 or maze[direction] == 3):
			maze[direction] = 4
			find_nodes(direction)
			
	
	options = Counter(options)
	
	if(4 - options[1] != 2 or template_maze[tuple(pos)] == 3 or maze[tuple(pos)] == 2):
		nodes.append(tuple(pos))

def build_nodes():
	network = {}
	uuid = 0
	for pos in nodes:
		#				[position, type, connections]
		network[uuid] = [pos, template_maze[pos], []]

		uuid += 1
	return network

def find_pos_in_net(network, query):
	for i in network:
		if(network[i][0] == query):
			return i


tracing = []
def connect_network(network):
	global tracing
	for node in network:
		temp_maze = template_maze.copy()
		temp_maze[network[node][0]] = 4
		for direction in get_directions(network[node][0]):
			if(temp_maze[direction] == 0 or temp_maze[direction] == 2 or temp_maze[direction] == 3):
				found = None
				path = direction
				distance = 0
				tracer = []
				tracer.append(network[node][0])
				while found is None:
					tracer.append(path)
					distance += 1
					temp_maze[path] = 4
					found = find_pos_in_net(network, path)
					paths = get_directions(path)
					for i in range(len(paths)):
						if(temp_maze[paths[i]] == 0 or temp_maze[paths[i]] == 2 or temp_maze[paths[i]] == 3):
							if(i == 0):
								path = move(path, MOVE_UP)
							elif(i == 1):
								path = move(path, MOVE_RIGHT)
							elif(i == 2):
								path = move(path, MOVE_DOWN)
							else:
								path = move(path, MOVE_LEFT)
				tracing.append(tracer)
				if((node, distance) not in network[found][2]):

					network[found][2].append((node, distance))
					network[node][2].append((found, distance))
	return network



start_point = tuple([element for tupl in np.where(maze == 2) for element in tupl])
find_nodes(start_point)
network = build_nodes()
network = connect_network(network)

print('Network Built!')
