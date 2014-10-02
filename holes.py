#Solution to Holes in the text (HOLES) for codechef

import sys

score = 0 
lines = sys.stdin.readlines()
number = int(lines[0])
 
for count in xrange(int(number)):
	inpt = (lines[count + 1])
	score = 0
	for b in inpt:
		if b in "B":
			score = score + 2
		elif b in "ADOPQR":
			score = score + 1
	print score


