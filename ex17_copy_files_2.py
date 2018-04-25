# learn python the hard way
#exercise 17
# copy files
# Rafael Serrano 4/24/2018

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


#in_file = open (from_file)
#indata = in_file.read()

#combine the last two in ine line
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input('>>')

out_file = open(to_file, 'w')
out_file.write(indata)

print "Yes, It's done"

out_file.close()
in_file.close()