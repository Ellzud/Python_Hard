# Learn python the hard way
# exercise 5
# more variables and printing
# Rafael Serrano 4/23/2018

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "he's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, we will try to get it right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)