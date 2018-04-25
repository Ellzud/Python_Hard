# learn python the hard way
# exercise 23
# read code and try (play1)
# Rafael Serrano 4/25/2018

import random, string

def random_str(num, length = 7):
	with open("play1_result.txt", 'wb') as f:
		for i in range(num):
			chars = string.letters + string.digits
			s = [random.choice(chars) for i in range(length)]
			f.write(''.join(s) + '\n')
			
random_str(7)