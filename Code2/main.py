#!/usr/bin/python
# COMP6026
# @author hl13g10
# @brief reimplementation of Powers (2007) work for COMP6026 coursework
import math
import random
import pylab
outfile = "pool.txt"
fig = pylab.figure()
## Globals
K = 0.1 ## Global Death rate
R_small = 4.0 ## Resources for a small group
R_large = 50.0 ## Resources for a large group
Gc = 0.018 ## Growth rate for a cooperator
Gs = 0.02 ## Growth rate for selfish
Cc = 0.1 ## Consumption rate for a cooperator
Cs = 0.2 ## Consumption rate for selfsih
N = 4000 ## Population size
N_large = 40 ## Number of individuals in a large group
N_small = 4 ## Number of individuals in a small group
T = 120 ## Number of generations
t = 4 ## Number of time steps in groups

#The numbers will be stored in a list, these are the Indexs for each genotype
NUM_GENO = 4
COOP_SM = 0
COOP_LG = 1
SELF_SM = 2
SELF_LG = 3

#Some global lists for storing some data in to plot later.
data_c_s = list()
data_c_l = list()
data_s_s = list()
data_s_l = list()
large = list()
selfish = list()

## @brief Calculated the resources allocated to each genotype.
#  @param - the group to use
#  @retval - The resources allocated
#  Resources are allocated using the following formula
#  \f[
# r_i = \frac{ n_i . G_i . C_i }{\sum\limits_j (n_j . G_j . C_j )} . R 
#  \f]
def Resource(group, R):

	#calculates the resource allocated to each genotype
	#calculate the sum part
	den = ( group[COOP_SM] * Gc * Cc ) + ( group[COOP_LG] * Gc * Cc ) + ( group[SELF_SM] * Gs * Cs ) + ( group[SELF_LG] * Gs * Cs )
	den = R / den  #and times it by the constant
	resources = [0] * NUM_GENO
	resources[COOP_SM] = den * group[COOP_SM] * Gc * Cc 
	resources[COOP_LG] = den * group[COOP_LG] * Gc * Cc 
	resources[SELF_SM] = den * group[SELF_SM] * Gs * Cs 
	resources[SELF_LG] = den * group[SELF_LG] * Gs * Cs 
	return resources


## @brief Calculate the growth of the population depending on the resource calculation
#  @param group - the group to use
#  @param resource - the resources consumed by the group
#  @retval - The resulting population
#  growth is calculated using the following formula
#  \f[
#	n_i (t + 1) = n_i (t) + \frac{r_i}{C_i} - K.n_i (t)
#  \f]
def GrowPopulation(group, resource):
	group[COOP_SM] = (group[COOP_SM] + ( resource[COOP_SM] / Cc ) - K * group[COOP_SM])
	group[COOP_LG] = (group[COOP_LG] + ( resource[COOP_LG] / Cc ) - K * group[COOP_LG])
	group[SELF_SM] = (group[SELF_SM] + ( resource[SELF_SM] / Cs ) - K * group[SELF_SM])
	group[SELF_LG] = (group[SELF_LG] + ( resource[SELF_LG] / Cs ) - K * group[SELF_LG])
	return group
## @brief Inialises the global lists and clears the output file
def InitWrite():
	f = open(outfile, 'w')
	f.write("COOP_SM,COOP_LG,SELF_SM,SELF_LG\n")
	f.close()
	data_c_s = list()
	data_c_l = list()
	data_s_s = list()
	data_s_l = list()

## @brief Writes the pool data to a text file and stores to list for plotting
#  @param pool - the pool to write
def WriteData(pool):
	f = open(outfile, 'a')
	f.write("%d,%d,%d,%d\n" % (pool[COOP_SM], pool[COOP_LG], pool[SELF_SM], pool[SELF_LG]))
	f.close()
	data_c_s.append(pool[COOP_SM] / float(N))
	data_c_l.append(pool[COOP_LG] / float(N))
	data_s_s.append(pool[SELF_SM] / float(N))
	data_s_l.append(pool[SELF_LG] / float(N))
	large.append((pool[SELF_LG] + pool[COOP_LG] )/ float(N))
	selfish.append((pool[SELF_LG] + pool[SELF_SM] )/ float(N))
	pass


## @brief plots the data in the global lists.
def PlotAll():
        pylab.figure(fig.number)
        pylab.xlabel("Generation")
        pylab.ylabel("Number of genotype")

	x = range(T)
        pylab.plot(x, data_c_s, 'b-', label="Co-op Small") # '.' is point, ',' is pixel
        pylab.plot(x, data_c_l, 'b:', label="Co-op Large") # '.' is point, ',' is pixel
        pylab.plot(x, data_s_s, 'r-', label="Selfish Small") # '.' is point, ',' is pixel
        pylab.plot(x, data_s_l, 'r:', label="Selfish Large") # '.' is point, ',' is pixel
	pylab.legend(loc='lower right')
	pylab.show()
        pylab.draw()

	#pylab.figure()
	pylab.xlabel("Generation")
	pylab.ylabel("Global frequency")
	pylab.plot(x, large, 'k:', label="Large Group Size")
	pylab.plot(x, selfish, 'k-', label="Selfish resource usage")
	pylab.legend(loc='upper right')
	pylab.show()
	pylab.draw()
	pass

## @brief some testing to check things work
def Test():
	test = [6.0,8.0,12.0,14.0]
	r = Resource(test, R_large)
	print ("Group :")
	print test
	print("Resources: ")
	print r
	GrowPopulation(test, r)
	print ("Group :")
	print test
	raw_input()
	pass
## @brief main function.
#  Executes the stages of the GA. 
if "__main__" == __name__:
	#initialise an equally distributed population
	InitWrite()
	pool = list()
	for i in range(NUM_GENO):
		pool.append( float(N / NUM_GENO ) )
	print pool
	#WriteData(pool)
	#r = Resource(pool)
	#print r
	#pool = GrowPopulation(pool, r)
	#print pool
	for g in range(T):
		print("GENERATION %d" % g)
		WriteData(pool)
		#Group formation
		smallgroups = list()
		largegroups = list()
		#number of groups
		sm = int((pool[COOP_SM] + pool[SELF_SM]) / N_small)
		lg = int((pool[COOP_LG] + pool[SELF_LG]) / N_large)
		#calculate proportions
		if sm:#if we have any small groups to make
			p_sm_coop = pool[COOP_SM] / ( pool[COOP_SM] + pool[SELF_SM])
			for i in range(sm):
				group = [0.0] * NUM_GENO
				for i in range(N_small): #group size of n small
					if (random.random() < p_sm_coop):#choose a coop
						group[COOP_SM] += 1
					else:
						group[SELF_SM] += 1
				smallgroups.append(group)
		if lg:#if we have any large groups to make
			p_lg_coop = pool[COOP_LG] / ( pool[COOP_LG] + pool[SELF_LG])
			for i in range(lg):
				group = [0.0] * NUM_GENO
				for i in range(N_large): #group size of n small
					if (random.random() < p_lg_coop):#choose a coop
						group[COOP_LG] += 1
					else:
						group[SELF_LG] += 1
				largegroups.append(group)
		
		#Reproduction and resource allocation for allowed timesteps
		for group in largegroups:
			for _t in range(t):
				rl = Resource(group, R_large)
				GrowPopulation(group, rl)
		for group in smallgroups:
			for _t in range(t):
				rs = Resource(group, R_small)
				GrowPopulation(group, rs)
		#Migrant pool formation
		pool = [0.0]*NUM_GENO#reset pool - will remove any that didn't make it to groups
		for group in (largegroups + smallgroups):
			for i in range(NUM_GENO):
				pool[i] += group[i]
		print("Pool Size = %d" % sum(pool))
		#reduce pool
		scale = float(N) / float(sum(pool)) #scale so that have a population size of N
		print("Scale = %f" % scale)
		for i in range(NUM_GENO):
			pool[i] = ((pool[i] * scale))
		print("Pool Size after scale = %d" % sum(pool))
		
	#end for T
	PlotAll()
	print("DONE!")
	raw_input()
	pass
