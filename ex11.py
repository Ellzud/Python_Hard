# Learn python the hard way
# excersice 11
# inputs
# Rafael Serrano 4/23/2018

# We put commas at the end of the lines to prevent that a new line is created where we don't want it
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(
	age, height, weight)