if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listed3d = [[[[i,j,k] for k in range(0,z+1)] for j in range(0,y+1) ]for i in range(0,x+1)]
    listed2d = [v for sublist in listed3d for v in sublist]
    listed = [v for sublist in listed2d for v in sublist if v[0] + v[1] + v[2] != n]
    listed.sort
    print(listed)
