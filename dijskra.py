from build_network import network, tracing
import math

for i in network:
	if(network[i][1] == 2):
		start_node = i
		break

# 		[[node, length, origin]]
queue = [[start_node, 0, None]]
dequeue = []

def generate_queue():
	for i in network:
		queue.append([i, math.inf, None])

def find_in_queue(query):
	i = 0
	for card in queue:
		if(card[0] == query):
			return i
		i += 1

def dijkstra():
	global queue
	queue.sort(key=lambda x: x[1])
	try:
		while not network[queue[0][0]][1] == 3:
			
			for i in network[queue[0][0]][2]:
				index = find_in_queue(i[0])
				if(index is not None):
					if(queue[0][1]+i[1] < queue[index][1]):
						queue[index][1] = queue[0][1]+i[1]
						queue[index][2] = queue[0][0]
			dequeue.append(queue[0])
			del queue[0]
			queue.sort(key=lambda x: x[1])
	except:
		raise Exception("Maze not possible")
	dequeue.append(queue[0])
	del queue[0]
generate_queue()
dijkstra()

print('Path Calculated!')
