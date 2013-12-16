# Python Template
# @author hl13g10
# @brief collection of the fitness functions

from resident import resident

## @brief Score function.
#  @param - a - value to be scored. Should be a resident
#  @param - b - value to score a against. Should be a resident
#  @retval - Score of a when compared to b
#  A basic score function. Returns 1 if a &gt; b, else 0
def score(a, b):
	if ( a > b):
		return 1
	else:
		return 0

## @brief Two Dimensional Score function.
#  @param - a - value to be scored. 
#  @param - b - value to score a against.
#  @retval - Score of a when compared to b
def score2(a, b):
	if ( abs( a[0] - b[0] ) > abs( a[1] - b[1] ) ):
		return score( a[0], b[0] )
	else:
		return score( a[1], b[1] )


## @brief Two Dimensional Score function, to add intransitive superiority
#  @param - a - value to be scored. 
#  @param - b - value to score a against.
#  @retval - Score of a when compared to b
def score3(a, b):
	if ( ( abs(a[0] - b[0]) ) < ( abs(a[1] - b[1]) ) ):
		return score( a[0], b[0] )
	else:
		return score( a[1], b[1] )
## @brief first fitness function
#  @param - a - resident to score
#  @param - S - list of residents to score against
#  @retval - fitness of a
#  calculates the fitness of a against population S. 
def fitness(a, S):
	fit = 0
	for b in S:
		fit = fit + score(a._value,b._value)
	return fit

## @brief second fitness function
#  @param - a - 2D values to score
#  @param - S - list of residents to score against
#  @retval - fitness of a
#  calculates the fitness of a against population S. 
#  stores the fitness in a.fitness and also returns it
def fitness2(a, S):
	fit = 0
	for b in S:
		fit = fit + score2(a._value,b._value)
	return fit

## @brief third fitness function
#  @param - a - 2D values to score
#  @param - S - list of residents to score against
#  @retval - fitness of a
#  calculates the fitness of a against population S. 
#  stores the fitness in a.fitness and also returns it
def fitness3(a, S):
	fit = 0
	for b in S:
		fit = fit + score3(a._value,b._value)
	return fit

if "__main__" == __name__:
	''' Code to be run if this is main '''
	pass
