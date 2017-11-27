from collections import namedtuple, defaultdict
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Cell = namedtuple('Cell', ['x', 'y'])

#no boundary condition

#gets the neighbor cells via a tuple value for each cell coordinate given
def getNeighbours(m,cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                if x == -1:
                    if y == -1:
                        yield Cell(m-1,m-1)
                    elif y == m:
                        yield Cell(m-1,0)
                    else:
                        yield Cell(m-1,y)
                elif x == m:
                    if y == -1:
                        yield Cell(0,m-1)
                    elif y == m:
                        yield Cell(0,0)
                    else:
                        yield Cell(0,y)
                elif y == -1:
                    if x == -1:
                        yield Cell(m-1,m-1)
                    elif x == m:
                        yield Cell(m-1,0)
                    else:
                        yield Cell(x,m-1)
                elif y == m:
                    if x == -1:
                        yield Cell(0,m-1)
                    elif x == m:
                        yield Cell(0,0)
                    else:
                        yield Cell(x,0)
                else:
                    yield Cell(x, y)


#adds +=1 for each neighbour of a cell that is alive (so if the cell is alive, it exerts a +1 influence on all its neighbors)
def getNeighbourCount(m,board):
    neighbour_counts = defaultdict(int)
    for cell in board:
        for neighbour in getNeighbours(m,cell):
            neighbour_counts[neighbour] += 1
    return neighbour_counts


def advanceBoard(m,board):
    land=np.zeros(shape=(m,m)) 
    new_board = set()
    for cell, count in getNeighbourCount(m,board).items():
        #if the count ==3, it's going to be alive in the next generation whether or not it's dead or alive. 
        #If it's alive and count ==2, then it's alive again, hence cell in board and count ==2
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)   
    for i in enumerate(new_board):
        land[i[1][0]][i[1][1]] = 1
    fig=plt.figure()
    cmap=plt.cm.tab10  
    cmap.set_under(color='white')     
              
    return new_board, land

#only cells that are alive are added to the board
def generateBoard(desc):
    board = set()
    label='test'
    for row, line in enumerate(desc):
        for col, elem in enumerate(line):
            if elem ==  1:
                board.add(Cell(int(col), int(row)))
    return board, label

def animfunc(im):
    cmap=plt.cm.tab10  
    cmap.set_under(color='black') 
    return plt.imshow(im, cmap='gray', vmin=0.001 , interpolation='none')



def main():
    map=[]
    m=int(input("Number of cells:"))
    initboard=np.random.randint(0,2,size=(m,m))
    n=int(input("Number of generations: "))
    f = generateBoard(initboard)[0]
    for i in range(n):
        f = advanceBoard(m,f)[0]
        im = advanceBoard(m,f)[1]
        map.append(im)
    fig=plt.figure()
    anim = FuncAnimation(fig, animfunc, interval=n,frames=map)
    anim.save('game4.mp4')
    plt.show()


if __name__ == '__main__':
    main()



