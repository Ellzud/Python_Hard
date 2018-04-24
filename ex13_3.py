# learn python the hard way
# exercise 13
# parameters, unpacking, variables
# Rafael Serrano 4/23/2018

from sys import argv

script, first, second, third, fourth = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is called: ", third
print "Your fourth argument is: ", fourth
print "\n\n"
# Let's play matlibs
adj1 = raw_input("Please give me an Adjective to use: ")
adj2 = raw_input("Please give me a second Adjective to use: ")
print '\n\n'
print "The %s %s is a %s %s" %(adj1, first, adj2, second)