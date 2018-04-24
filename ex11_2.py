# Learn python the hard way
# excersice 11
# inputs
# Rafael Serrano 4/23/2018

# I wanted to change the initial script to use raw_input as a function
# I'm passing the question as a parameter

age = raw_input("How old are you? ")

height = raw_input("How tall are you? ")

weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." %(
	age, height, weight)