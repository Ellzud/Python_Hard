# learn python the hard way
# exercise 15
# reading files
# Rafael Serrano 4/23/2018

from sys import argv

script, filename = argv # unpacks the arguments to variables

txt = open(filename)  #returns a file object

print "here's your file %r:" % filename  #shows you the name of your txt file
print txt.read()  # we use a function of the file object to read it

print "\n Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print "\n", txt_again.read()