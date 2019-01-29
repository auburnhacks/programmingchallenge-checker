from os import walk, getcwd, chdir, system
import sys
import subprocess
import collections

Score = collections.namedtuple('Score', ('name', 'val', 'time'))

dirs = [d[0] for d in walk(getcwd())]
vals = []

CORRECT_OUTPUT = 7

for d in dirs[1:]:
	chdir(d)
	proc = subprocess.Popen(["python", "-c", "from os import system; system('./makefile.sh')"], stdout=subprocess.PIPE)
	out = proc.communicate()[0].decode('ascii').split('\n')[:-1]
	vals.append(Score(out[0], float(out[1]), float(out[2])))
	chdir("../")

vals.sort(key=lambda x: x.time if x.val == CORRECT_OUTPUT else float('inf'))

outfile = open("output.txt", "a")
for line in vals:
	outfile.write(str(line) + "\n")
