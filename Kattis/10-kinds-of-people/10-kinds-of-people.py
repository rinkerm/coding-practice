import sys
'''
This is my 3rd attempt at a solution for 10 kinds of people on kattis
This solution also fails due to time limit exceeded at test 23/25
'''
def colorFillHelper(groups,bin_map,uncatagorized,x,y,g,val):
	'''
	Recursive helper function to actually do the 'coloring'
	'''
	if(x<0 or x>= len(bin_map[0]) or y<0 or y>= len(bin_map) or bin_map[y][x] != val or "{},{}".format(x,y) not in uncatagorized):
		return
	key = "{},{}".format(x,y)
	groups[key] = g
	uncatagorized.remove(key)
	colorFillHelper(groups,bin_map,uncatagorized,x+1,y,g,val)
	colorFillHelper(groups,bin_map,uncatagorized,x-1,y,g,val)
	colorFillHelper(groups,bin_map,uncatagorized,x,y+1,g,val)
	colorFillHelper(groups,bin_map,uncatagorized,x,y-1,g,val)

	
def colorFill(groups,bin_map,uncatagorized,x,y,g):
	'''
	modified version of a color fill algorithm to split the map into contiguous regions
	'''
	val = bin_map[y][x]
	colorFillHelper(groups,bin_map,uncatagorized,x,y,g,val)


def main():
	line1 = sys.stdin.readline().strip().split(" ")
	r = int(line1[0])
	c = int(line1[1])
	groups = {}
	uncatagorized = set()
	bin_map  = []
	for i in range(0,r):
		map_line = sys.stdin.readline().strip()
		map_row = []
		for j in range(0,c):
			map_row.append(int(map_line[j]))
			uncatagorized.add("{},{}".format(j,i))
			groups["{},{}".format(j,i)] = 0
		bin_map.append(map_row)
	g = 0
	while(len(uncatagorized)>0):
		elem = uncatagorized.pop()
		splitted = elem.split(",")
		x = int(splitted[0])
		y = int(splitted[1])
		uncatagorized.add(elem)
		colorFill(groups,bin_map,uncatagorized,x,y,g)
		g+=1
	n = int(sys.stdin.readline())	
	for k in range(0,n):
		in_line = sys.stdin.readline().strip().split(" ")
		start = [int(in_line[1])-1,int(in_line[0])-1]
		end = [int(in_line[3])-1,int(in_line[2])-1]
		if(groups["{},{}".format(start[0],start[1])]==groups["{},{}".format(end[0],end[1])]):
			if(bin_map[start[1]][start[0]]==0):
				print("binary")
			else:
				print("decimal")
		else:
			print("neither")
		#print(bestfirst(start,end,bin_map))
	
	
main()
	
