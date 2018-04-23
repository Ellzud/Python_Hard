#Learn python the hard way
# exercise 6
#strings
#Rafael serrano 4/23/2018


# the variable x contains a string with a formatter inside and also contains the value at the end 
#(the value is not part of the string but is part of the variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# when we use the %r, we are telling python that the variable is raw data
print "I said: %r." % x
print "I also said: '%s'." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#here the value "False" that is inside the variable hilarious is converted to a string
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
