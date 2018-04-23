# learn python the hard way
# exercise 8
#even more printing and variables
# Rafael Serrano 4/23/2018

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
#prediction for next line is just the variable printed 4 times without any substitution
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)