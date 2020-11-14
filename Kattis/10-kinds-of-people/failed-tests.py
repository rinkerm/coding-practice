import sys
from queue import PriorityQueue

def euclideanDist(p,q):
	xdist = (q[0]-p[0])**2
	ydist = (q[1]-p[1])**2
	return(xdist+ydist)
def bestfirst(start,end,bin_map):
	'''
	Implementation of a bestfirst approach
	'''
	visited = {}
	stack = PriorityQueue()
	stack.put((0,start))
	if(not(bin_map[start[1]][start[0]]==bin_map[end[1]][end[0]])):
		return "neither"
	elif(start == end):
		if(bin_map[start[1]][start[0]] == 0):
			return "binary"
		else:
			return "decimal"
	else:
		val = bin_map[start[1]][start[0]]
		if(val==0):
			return_val = "binary"
		else:
			return_val = "decimal"
			
		while(not stack.empty()):
			item = stack.get()[1]
			if("{},{}".format(item[0],item[1]) in visited):
				"Do nothing"
			else:
				visited["{},{}".format(item[0],item[1])] = True
				x = item[0]
				y = item[1]

				if(bin_map[y][x]==val):
					if([x,y] == end):
						return return_val
					for i in [[-1,0],[0,1],[1,0],[0,-1]]:
						x1 = x+i[0]
						y1 = y+i[1]
						
						if((x1>=0 and x1<len(bin_map[0])) and (y1>=0 and y1<len(bin_map))):
							stack.put((euclideanDist([x1,y1],end),[x1,y1]))
		return "neither"

def dfs(start,end,bin_map):
	'''
	Implementation of a depth first search to find if there is a path
	Outcome 23/25 -> Time Limit Exceeded
	'''
	visited = {}
	stack = [start]
	if(not(bin_map[start[1]][start[0]]==bin_map[end[1]][end[0]])):
		return "neither"
	elif(start == end):
		if(bin_map[start[1]][start[0]] == 0):
			return "binary"
		else:
			return "decimal"
	else:
		val = bin_map[start[1]][start[0]]
		if(val==0):
			return_val = "binary"
		else:
			return_val = "decimal"
			
		while(len(stack)>0):
			if("{},{}".format(stack[0][0],stack[0][1]) in visited):
				stack.pop(0)
			else:
				visited["{},{}".format(stack[0][0],stack[0][1])] = True
				x = stack[0][0]
				y = stack[0][1]
				stack.pop(0)
				

				if(bin_map[y][x]==val):
					if([x,y] == end):
						return return_val
					for i in [[-1,0],[0,1],[1,0],[0,-1]]:
						x1 = x+i[0]
						y1 = y+i[1]
						
						if((x1>=0 and x1<len(bin_map[0])) and (y1>=0 and y1<len(bin_map))):
							stack.insert(0,[x1,y1])
		return "neither"




def main():
	line1 = sys.stdin.readline().strip().split(" ")
	r = int(line1[0])
	c = int(line1[1])

	bin_map  = []
	for i in range(0,r):
		map_line = sys.stdin.readline().strip()
		map_row = []
		for j in range(0,c):
			map_row.append(int(map_line[j]))
		bin_map.append(map_row)

	n = int(sys.stdin.readline())

	for k in range(0,n):
		in_line = sys.stdin.readline().strip().split(" ")
		start = [int(in_line[1])-1,int(in_line[0])-1]
		end = [int(in_line[3])-1,int(in_line[2])-1]
		#print(bestfirst(start,end,bin_map))
main()
	
