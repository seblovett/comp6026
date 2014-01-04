#!/usr/bin/python
# COMP6026
# @author seblovett
# @brief 
import math
import random
import pylab
outfile = "pool.txt"
fig = pylab.figure()
## Globals
K = 0.1
R_small = 4.0
R_large = 50.0
Gc = 0.018
Gs = 0.02
Cc = 0.1
Cs = 0.2
N = 4000
N_large = 40
N_small = 4
T = 120#00
t = 4

#The numbers will be stored in a list, these are the Indexs for each genotype
NUM_GENO = 4
COOP_SM = 0
COOP_LG = 1
SELF_SM = 2
SELF_LG = 3

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
#	r_i = \frac{ n_i . G_i . C_i }{\Sigma (n_j . G_j . C_j )} . R 
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

def InitWrite():
	f = open(outfile, 'w')
	f.write("COOP_SM,COOP_LG,SELF_SM,SELF_LG\n")
	f.close()
	data_c_s = list()
	data_c_l = list()
	data_s_s = list()
	data_s_l = list()
## @brief Writes the pool data to a text file
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


## @brief plots the data as it is generated
#  @param - x - generation
#  @param - y - list of all residents at that generation
def InitPlot():
        pylab.figure(fig.number)
        pylab.xlabel("Generation")
        pylab.ylabel("Number of genotype")
	pylab.legend(loc='lower right')
#def Plot(x, y):
#        ''' x should be a single number, y is list of values to residents that x value '''
#        pylab.figure(fig.number)
#        pylab.ion()
#        y_vals = list()
#        x_vals = list()
#        print data_c_s
#        pylab.xlabel("Generation")
#        pylab.ylabel("Number of genotype")
#        pylab.plot(x, data_c_s, 'b.', label="Co-op Small") # '.' is point, ',' is pixel
#        pylab.plot(x, data_c_l, 'k.', label="Co-op Large") # '.' is point, ',' is pixel
#        pylab.plot(x, data_s_s, 'g.', label="Selfish Small") # '.' is point, ',' is pixel
#        pylab.plot(x, data_s_l, 'r.', label="Selfish Large") # '.' is point, ',' is pixel
#	pylab.legend(loc='upper left')
#        pylab.draw()
#        pass
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
if "__main__" == __name__:
	#initialise an equally distributed population
	InitWrite()
	#InitPlot()
	pool = list()
	for i in range(NUM_GENO):
		pool.append( float(N / NUM_GENO ) )
	print pool
	#WriteData(pool)
	#r = Resource(pool)
	#print r
	#pool = GrowPopulation(pool, r)
	#print pool
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
	for g in range(T):
		print("GENERATION %d" % g)
		WriteData(pool)
		#Group formation
#		largegroups = list()
#		#make large groups
#		lg = pool[COOP_LG] + pool[SELF_LG]
#		p_coop = pool[COOP_LG] / lg
#		print("lg = %d" % lg)
##		while lg >= N_large:#while there are enough large left
#		for i in range(int(lg / N_large)):
#			group = list()
#			group = [0.0]*NUM_GENO
#			for i in range(N_large):
#				if (random.random() < p_coop):#choose a coop
#					if 0 < pool[COOP_LG]:
#						group[COOP_LG] += 1
#						pool[COOP_LG]  -= 1
#					else:#no coops left in pool
#						group[SELF_LG] += 1
#						pool[SELF_LG]  -= 1
#				else: #choose a selfish
#					if 0 < pool[SELF_LG]:
#						group[SELF_LG] += 1
#						pool[SELF_LG]  -= 1
#					else:#no selfish left in pool
#						group[COOP_LG] += 1
#						pool[COOP_LG]  -= 1
#			largegroups.append(group)
##			lg = pool[COOP_LG] + pool[SELF_LG]
#		#make small groups
#		smallgroups = list()
#		sm = pool[COOP_SM] + pool[SELF_SM]
#		p_coop = pool[COOP_SM] / sm
##		while sm >= N_small:#while there are enough large left
#		for i in range(int(sm / N_small)):
#			group = list()
#			group = [0.0]*NUM_GENO
#			for i in range(N_small):
#				if (random.random() < p_coop):#choose a coop
#					if 0 != pool[COOP_SM]:
#						group[COOP_SM] += 1
#						pool[COOP_SM]  -= 1
#					else:#no coops left in pool
#						group[SELF_SM] += 1
#						pool[SELF_SM]  -= 1
#				else: #choose a selfish
#					if 0 < pool[SELF_SM]:
#						group[SELF_SM] += 1
#						pool[SELF_SM]  -= 1
#					else:#no selfish left in pool
#						group[COOP_SM] += 1
#						pool[COOP_SM]  -= 1
#			smallgroups.append(group)
#			sm = pool[COOP_SM] + pool[SELF_SM]

		#make groups
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
		if 0 == g:		
			print("Large Groups")
			print largegroups
			total = [0,0,0,0]
			for group in largegroups:
				for i in range(len(group)):
					total[i] += group[i]
			print total
			print("NumLG = %d" % len(largegroups))
			print("Small Groups")
			print smallgroups
			total = [0]*4
			for group in smallgroups:
				for i in range(len(group)):
					total[i] += group[i]
			print total
			print("NumSM = %d" % len(smallgroups))
			raw_input()
		#Reproduction
#		for _t in range(t): #for number of pool steps
#			for group in largegroups:
#				rl = Resource(group, R_large)
#				GrowPopulation(group, rl)
#			for group in smallgroups:
#				rs = Resource(group, R_small)
#				GrowPopulation(group, rs)


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
		
		#raw_input()
		#store the data
		#Plot(g, pool)
		#WriteData(pool)
	#end for T
	PlotAll()
	print("DONE!")
	raw_input()
	pass
