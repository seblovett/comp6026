# Python Template
# @author hl13g10
# @brief Main to run Assignment2 from

from resident import resident
from fitness import *
import math
import pylab  # matplotlib
import time

#Some global values
POP_SIZE = 25
SAMPLE_SIZE = 15
fig = None
outfile = "data.txt"

def MutateAll(population):
	'''mutates all the residents in the population'''
#	newpop
	for p in population:
		p.mutate()
	return population

## @brief writes the objective fitness to a csv file
def Write(populations):
	f = open(outfile, "a")
	for p in populations:
		f.write("%d," % p.value()[0])
	f.write("\n")
	f.close()

## @brief plots the data as it is generated
#  @param - x - generation 
#  @param - y - list of all residents at that generation
def Plot(x, y):
	''' x should be a single number, y is list of values to residents that x value '''
	pylab.figure(Fig.number)
	pylab.xlabel("Generation")
	pylab.ylabel("Objective Fitness")
	pylab.ion()
	y_vals = list()
	x_vals = list()
	for _y in y:
		y_vals.append(_y.value()[0])
		x_vals.append(x)
	pylab.plot(x_vals, y_vals, 'r.') # '.' is point, ',' is pixel
	pylab.draw()
	pass


def Control():
	#Control Experiment
	pop1 = list()
	pop2 = list()
	#initialise the populations
	for i in range(POP_SIZE):
		pop1.append(resident(dimensions=1))
		pop2.append(resident(dimensions=1))
	for i in range(POP_SIZE):
		pop1[i]._string=["0"*100]
		pop2[i]._string=["1"*100]
#	for i in range(5):
#		Plot(i, [i, i+1, i/2.0] )
#		print(i)
#		time.sleep(1)
	for i in range(600): #itterate for 600 generations
		Plot(i, pop1 + pop2) #i is generation, pop1+pop2 gives all the residents in one list
		Write(pop1+pop2)
		pop1 = MutateAll(pop1)
		pop2 = MutateAll(pop2)


def Test():
	a = resident(size = 10, dimensions = 1)
	print(a._string)
	print(a._value)	
	b = resident(size = 10, dimensions = 1)
	c = resident(size = 10, dimensions = 1)
	population = list()
	population.append(b)
	population.append(c)
	print("values:\n\ta=")
	print(a._value)
	print("\tb=")
	print(b._value)
	print("\tc=")
	print(c._value)
	a.fitness = fitness(a, population)
	print("fitness of a = %d" % a.fitness)
	#test 2D
	a = resident(size = 10)
	b = resident(size = 10)
	c = resident(size = 10)
	a._value = [1, 6]
	b._value = [4, 5]
	c._value = [2, 4]
	population = list()
	population.append(a)
	population.append(b)
	population.append(c)
	print("values:\n\ta=")
	print(a._value)
	print("\tb=")
	print(b._value)
	print("\tc=")
	print(c._value)
	a.fitness = fitness2(a, population)
	b.fitness = fitness2(b, population)
	c.fitness = fitness2(c, population)
	print("fitness2 of a = %d" % a.fitness)
	print("fitness2 of b = %d" % b.fitness)
	print("fitness2 of c = %d" % c.fitness)
	
	a.fitness = fitness3(a, population)
	b.fitness = fitness3(b, population)
	c.fitness = fitness3(c, population)
	print("fitness3 of a = %d" % a.fitness)
	print("fitness3 of b = %d" % b.fitness)
	print("fitness3 of c = %d" % c.fitness)
	
if "__main__" == __name__:
	''' Code to be run if this is main '''
	print("Assignment 2\nhl13g10")
	#clear the output data file
	f = open(outfile, "w")
	f.close()
	Fig = pylab.figure()
	pop1 = list()
	pop2 = list()
	Control()
	pylab.figure(Fig.number)
	pylab.show()
	raw_input()

