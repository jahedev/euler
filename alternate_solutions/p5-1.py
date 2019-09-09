factors = list(range(1,21))
multiple = 1

def verify_multiple(factors, multiple):
	for factor in reversed(factors): 
		if (multiple % factor == 0):
			print ("{} is a factor of {}".format(factor,multiple))
		else:
			return False
		if (factor == factors[0]):
			return True

while (True):
	if verify_multiple(factors, multiple) == False:
		multiple = multiple + 1
	else:
		print ("{} is the smallest multiple of the range of factors".format(multiple))
		break;