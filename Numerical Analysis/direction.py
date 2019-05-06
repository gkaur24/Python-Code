import random
import numpy as np



def dirx (data):
    if data == "north" or "south":
        return 0
    if data == "east":
        return 1
    if data == "west":
        return -1
def diry (data):
    if data == "east" or "west":
        return 0
    if data == "north":
        return -1
    if data == "south":
        return 1
def oppo(data):
    if data == "west":
        return "east"
    if data == "east":
        return "west"
    if data == "north":
        return "south"
    if data == "south":
        return "north"

north=1
south=2
east=3
grid1=np.zeros(101,101)
def make_passages(x,y,grid):
    directions=["north","south","east","west"]
    random.shuffle(directions)
    for number in directions:
        newx= x+dirx(number)
        newy=y+diry(number)
        
        if newx > 0 and newx < 101 and newy > 0 and newy < 101 and grid[newy][newx]==0:
            grid[y][x]|=number
            grid[newy][newx]|=oppo(number)
            make_passages(newx, newy,grid)
make_passages(0,0,grid)



#directions=[north,south,east,west]
#random.shuffle(directions)
#print directions
