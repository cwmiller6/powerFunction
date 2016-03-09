#Author: Cole Miller
#Date: 8 March 2016

def power(base, exponent):
	""" Takes two arguments, base and exponent, then calculates results """
	#Make and empty list for the number to be multiplied 
	bases = []
	#set var product to 1
	product = 1
	#add as many bases as the exponent inputted, so that it can be multiplied by itself that many times
	while len(bases) < exponent:
		bases.append(base)
	#Do the actual multiplying 
	for x in bases:
		product *= x
	#return the result 
	return product 


###### Main Program ######

#Ask for the users base and exponent as new raw_input variables (also set to ints)
inputBase = int(raw_input("Enter a base: "))
inputExponent = int(raw_input("Enter the power you would like to apply to the base: "))

#use the custom power fucntion for the inputted base and exponent 
result = power(inputBase, inputExponent)

#Print result in custom way 
print("{} to the {} power = {}".format(inputBase, inputExponent, result))

