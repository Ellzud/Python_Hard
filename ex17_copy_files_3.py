# learn python the hard way
#exercise 17
# copy files
# Rafael Serrano 4/24/2018
# trying to make a copy script one line long

from sys import argv
from os.path import exists

script, from_file, to_file = argv
#we open the "to_file" in write mode and we write to it what we read from the "from_file"
open(to_file, 'w').write(open(from_file).read())

