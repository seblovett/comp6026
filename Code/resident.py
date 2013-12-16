# Python Template
# @author seblovett
# @brief A class to dictate the behaviour of an invidiual
import random

class resident:
	_size = 0
	_string = "";
	_value = 0;
	_mrate = 0;
	def __init__(self, size = 100, mutationrate = 0.005, dimensions=2):
		self._string = list()
		self._size = size
		self._mrate = mutationrate
		random.seed()
		for x in range(dimensions):
			_string = ""
			for i in range(self._size):
				r = random.random()
				if ( r < 0.5 ):
					_string = _string+"1"
				else:
					_string = _string+"0"
			self._string.append(_string)
		self.value() #get the value

	def value(self):
		self._value = list()
		for s in self._string:
			_value = 0
			for i in range(self._size):
				if "1" == s[i]:
					_value = _value + 1
			self._value.append(_value)
	def mutate(self):
		x = len(self._string)
		newstrs = list()
		for s in self._string:
			newstr = ""
			for i in range(self._size):#test each char
				r = random.random()
				if ( r < self._mrate): #test for mutation
					if ( "0" == self._string[i] ): #switch the bits if we mutate
						newstr = newstr + "1"
					else:
						newstr = newstr + "0"
				else:#else keep the same as before
					newstr = newstr + s[i]
			newstrs.append(newstr)
		self._string = newstrs #store the new string
		self.value() #recalculate the value
