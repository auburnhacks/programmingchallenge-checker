###########################
#			  #
#   Auburn Flag problem   #
#			  #
###########################

from os import walk, getcwd, chdir
import subprocess
import collections

Score = collections.namedtuple('Score', ('name', 'tests_passed', 'time_elapsed'))

# Gets a list of all the folders in the current directory
dirs = [d[0] for d in walk(getcwd())]
vals = []

# CORRECT_OUTPUT represents an array of the test cases
CORRECT_OUTPUT = [
		"********",
		"********",
		"********"
		]
num_tests = len(CORRECT_OUTPUT)

for d in dirs[1:]:
	chdir(d)

	# Executes the makefile
	proc = subprocess.Popen(["python", "-c", "from os import system; system('./makefile.sh')"], stdout=subprocess.PIPE)
	
	# Captures the output of executing the makefile
	out = proc.communicate()[0].decode('ascii').split('\n')[:-1]
	
	# Turns the output into the same format as CORRECT_OUTPUT
	outputs = out[1:-1]
	
	# This is for me to see if someone's program didn't execute properly/to see their outputs
	print(d)
	print(outputs)

	# Makes a count of the number of cases passed
	# TODO: turn this into functools.reduce or something similar
	tests_passed = 0
	for i in range(len(CORRECT_OUTPUT)):
		if outputs[i] == CORRECT_OUTPUT[i]:
			tests_passed += 1

	vals.append(Score(out[0], tests_passed, float(out[-1])))
	
	chdir("../")

# Sort the values based on the Elapsed time and if they passed all the test cases or not
vals.sort(key=lambda x: (-x.tests_passed, x.time_elapsed))

outfile = open("auburn_flag_output.txt", "a")
for line in vals:
	outfile.write(str(line) + "\n")
