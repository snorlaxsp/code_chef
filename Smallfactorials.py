#Solutions to the problem Small factorials in Codechef
import sys

i = 1
lines = sys.stdin.readlines()
number = int(lines[0])
 
for count in xrange(int(number)):
	inpt = int(lines[count + 1])
	i = 1
	for count2 in xrange(1,int(inpt + 1)):
		i = i*count2
	print i
