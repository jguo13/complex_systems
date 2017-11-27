import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def initial(m,n):
    universe=np.zeros(shape=(m,n))
    #set the middle cell as alive
    mid=m//2-1
    universe[0][mid]=1
    return universe

def rule_parse(rulenumber):
    binary_rule=format(rulenumber, '08b') #convert decimal to binary and ensure 8 character width        
    #create a dictionary of the rule
    map= {
        (1, 1, 1): binary_rule[0],
        (1, 1, 0): binary_rule[1],
        (1, 0, 1): binary_rule[2],
        (1, 0, 0): binary_rule[3],
        (0, 1, 1): binary_rule[4],
        (0, 1, 0): binary_rule[5],
        (0, 0, 1): binary_rule[6],
        (0, 0, 0): binary_rule[7]
    }
    return map

def generate(n,universe,map):
    for i in range(0,n-1):
        for j in range(0,universe.shape[1]-1):
            if j == 0:
                gen=[universe[i][universe.shape[1]-1],universe[i][j], universe[i][j+1]]
            elif j == universe.shape[1]-1:
                gen=[universe[i][j-1],universe[i][j], universe[i][0]]
            else:
                gen=[universe[i][j-1],universe[i][j], universe[i][j+1]]
            universe[i+1][j]=map[tuple(gen)]  
    cmap=plt.cm.tab10  
    cmap.set_under(color='black')     
    return plt.imshow(universe, cmap='gray', vmin=0.001 , interpolation='none')          

def main():
	n=int(input("Number of generations: "))
	m=int(input("Number of cells: "))
	rule=int(input("Rule: "))
	universe = initial(m,n)
	map = rule_parse(rule)
	fig=plt.figure()
	anim = FuncAnimation(fig, generate, interval=100,frames=m, fargs=(universe,map))
	anim.save('complexsys.mp4')
	plt.show()


if __name__ == '__main__':
	main()






