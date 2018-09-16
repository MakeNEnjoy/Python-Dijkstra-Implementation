from dijskra import tracing, network, dequeue as queue
from VARS import maze

def find_in_queue(query):
	i = 0
	for card in queue:
		if(card[0] == query):
			return i
		i += 1

#maze[network[queue[-1][0]][0]] = 5
#previous_path = -1
next_path = find_in_queue(queue[-1][0])
while next_path != 0:
	#maze[network[queue[next_path][2]][0]] = 5
	previous_path = next_path
	next_path = find_in_queue(queue[previous_path][2])
	1 == 1
	for pxs in tracing:
		if(network[queue[previous_path][0]][0] == pxs[0] and network[queue[next_path][0]][0] == pxs[-1]):
			for px in pxs:
				maze[px] = 5


print('Line Draw!')