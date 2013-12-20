# Python Template
# @author hl13g10
# @brief Main to run Assignment2 from

from resident import resident
from fitness import *
import math
#import matplotlib.pylab  # matplotlib
import time
import random
from datetime import datetime

#Some global values
POP_SIZE = 25
SAMPLE_SIZE = 15
GENERATIONS=600
fig = None
outfile = "data_%s.txt"

def MutateAll(population):
	'''mutates all the residents in the population'''
#	newpop
	for p in population:
		p = p.mutate()
	return population

## @brief writes the objective fitness to a csv file
def Write(pop1, pop2):
	fname1 = outfile % "pop1"
	fname2 = outfile % "pop2"
	f = open(fname1, "a")
	for p in pop1:
		f.write("%d," % p.value()[0])
	f.write("\n")
	f.close()
	
	f = open(fname2, "a")
	for p in pop2:
		f.write("%d," % p.value()[0])
	f.write("\n")
	f.close()

try:
	import pylab
	
	
	## @brief plots the data as it is generated
	#  @param - x - generation 
	#  @param - y - list of all residents at that generation
	def Plot(x, y1, y2=None):
		''' x should be a single number, y is list of values to residents that x value '''
		pylab.figure(Fig.number)
		pylab.xlabel("Generation")
		pylab.ylabel("Objective Fitness")
		pylab.ion()
		y_vals = list()
		x_vals = list()
		for _y in y1:
			y_vals.append(_y.value()[0])
			x_vals.append(x)
		pylab.plot(x_vals, y_vals, 'r.') # '.' is point, ',' is pixel
		
		if y2:#if two populations are given, colour the second one blue. 
			y_vals = list()
			x_vals = list()
			for _y in y1:
				y_vals.append(_y.value()[0])
				x_vals.append(x)
			pylab.plot(x_vals, y_vals, 'b.') # '.' is point, ',' is pixel
		pylab.draw()
		pass
except:
	def Plot(x, y1, y2=None):
		pass	
def FPS(pop):
	'''Fitness proportionate selection.
	Uses roulette wheel to select a parent from the population.
	Parent is mutated and the child is randomly replaced back into the population'''
	#make the wheel
	sum = 0
	wheel=list()
	for p in pop:
		sum = sum + p.fitness
		wheel.append(sum)
	
	#pick from the wheel
	pick = sum * random.random()
	for i in range(len(wheel)):
		if wheel[i] >= pick:
			break
	
	#got selected, now mutate and randomly replace
	child = pop[i].mutate()
	
	pick = int(math.floor(len(pop) * random.random()))
	pop[pick] = child

def Experiment1():
	#Experiment 1 - loss of gradient1
	pop1 = list()
	pop2 = list()

	for i in range(POP_SIZE):
		pop1.append(resident(dimensions=1))
		pop2.append(resident(dimensions=1))
	
	for i in range(GENERATIONS): # repeat
		if (i % 10) == 0:
			print '.',
		#plot data
		Plot(i, pop1, pop2) #i is generation, pop1+pop2 gives all the residents in one list
		#write data
		Write(pop1, pop2)
		#evaluate fitness of all individuals
		for a in pop1: #for each member in population 1
			#make a sample of SAMPLE_SIZE from pop2
			sample = list()
			for z in range(SAMPLE_SIZE):
				i = int(math.floor(random.random() * SAMPLE_SIZE))
				sample.append(pop2[i])
			a.fitness = fitness(a, sample)
		
		for a in pop2: #for each member in population 2
			#make a sample of SAMPLE_SIZE from pop1
			sample = list()
			for z in range(SAMPLE_SIZE):
				i = int(math.floor(random.random() * SAMPLE_SIZE))
				sample.append(pop1[i])
			a.fitness = fitness(a, sample)
		
		#select and replace
		FPS(pop1)
		FPS(pop2)
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
	for i in range(GENERATIONS): #itterate for n generations
		if (i % 10) == 0:
			print '.',
		Plot(i, pop1, pop2) #i is generation, pop1+pop2 gives all the residents in one list
		Write(pop1, pop2)
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
	#Fig = pylab.figure()
	pop1 = list()
	pop2 = list()
	print("Running Control...")
	print "Start at ", 
	print datetime.now().time()
	Control()
	print "Control Function Finished at ",
	print datetime.now().time()
	
	
	print("Running Experiment 1...")
	print "Start at ", 
	print datetime.now().time()
	Experiment1()
	print "Experiment1 Finished at ",
	print datetime.now().time()
	#pylab.figure(Fig.number)
	#pylab.show()
	#raw_input()

