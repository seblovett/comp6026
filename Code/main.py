# Python Template
# @author hl13g10
# @brief Main to run Assignment2 from

from resident import resident
from fitness import *
if "__main__" == __name__:
	''' Code to be run if this is main '''
	print("Assignment 2\nhl13g10")
	
	#Globals
	POP_SIZE = 25
	SAMPLE_SIZE = 15
	#to check class works
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
	
