from collections import defaultdict
from math import log, ceil
import difflib
#n = raw_input()
"""def Xor(str1, str2):
	str1.replace("0b","")
	str2.replace("0b","")
"""
def bitdif(i,j):
	str1 = bin(i)
	str2 = bin(j)
	#print str1,str2
	str1 = str1.replace("0b","")
	str2 = str2.replace("0b","")
	str1 = ''.join(['0']*(maxPower-len(str1))) + str1
	str2 = ''.join(['0']*(maxPower-len(str2))) + str2
	#print str1,str2
	xstr = ""
	#str1 = bin(i)
	#str2 = bin(j)
	for x,s in enumerate(difflib.ndiff(str1,str2)):
		if s[0] == " ":
			xstr += str1[x]
		#print str1[i]
		elif s[0] == "-" :
			xstr += "-"
		#print i,j,xstr
	coloumns[xstr] = (i,j)
	return
print "Minterms:"
minterms = map(int , raw_input().split(","))
print minterms
print max(minterms)
#print log(max(minterms)+1,2) For testing
maxPower = int(log(max(minterms)+1,2))+1
d = defaultdict(list)
for minterm in minterms:
	if minterm not in d[bin(minterm).count("1")]:
		d[bin(minterm).count("1")].append(minterm)
print "Don't Cares:"
try:
	dontcares = map(int , raw_input().split(","))
except ValueError:
	dontcares = None
if(dontcares != None):
	print dontcares
	print max(dontcares)
	#print log(max(dontcares),2)
	print ceil(log(max(dontcares)+1,2))
	for dontcare in dontcares:
		if dontcare not in d[bin(dontcare).count("1")]:
			d[bin(dontcare).count("1")].append(dontcare)
			maxPower = max(maxPower,int(log(max(dontcares)+1,2))+1)
print maxPower

print d.items()
#if  d[0]:
#	print d[0] #Testing
coloumns = dict()
primeimplicants = list()
taken = list()
for key in sorted(d):
	#iterate over each list and thenext list
	if   d[key+1] is not None:
	#	continue
	#else:
		print d[key]
		print d[key+1]
		#mcol = defaultdict(list)
		for i in d[key]:
			for j in d[key+1]:
				if (bin(i^j).count("1")==1):
					taken.append(i)
					taken.append(j)
					#print i , j 
						#print i, j, "IT IS WORKING :D"
					#mcol[key].append()
					bitdif(i,j)
primeimplicants = [x for x in minterms if x not in taken]
print coloumns
print primeimplicants
					
#print primeimplicants


	from collections import defaultdict
from math import log, ceil
import difflib
#n = raw_input()
"""def Xor(str1, str2):
	str1.replace("0b","")
	str2.replace("0b","")
"""
def bitdif(i,j):
	str1 = bin(i)
	str2 = bin(j)
	#print str1,str2
	str1 = str1.replace("0b","")
	str2 = str2.replace("0b","")
	str1 = ''.join(['0']*(maxPower-len(str1))) + str1
	str2 = ''.join(['0']*(maxPower-len(str2))) + str2
	#print str1,str2
	xstr = ""
	#str1 = bin(i)
	#str2 = bin(j)
	for x,s in enumerate(difflib.ndiff(str1,str2)):
		if s[0] == " ":
			xstr += str1[x]
		#print str1[i]
		elif s[0] == "-" :
			xstr += "-"
		#print i,j,xstr
	coloumns[xstr] = (i,j)
	return
print "Minterms:"
minterms = map(int , raw_input().split(","))
print minterms
print max(minterms)
#print log(max(minterms)+1,2) For testing
maxPower = int(log(max(minterms)+1,2))+1
d = defaultdict(list)
for minterm in minterms:
	if minterm not in d[bin(minterm).count("1")]:
		d[bin(minterm).count("1")].append(minterm)
print "Don't Cares:"
try:
	dontcares = map(int , raw_input().split(","))
except ValueError:
	dontcares = None
if(dontcares != None):
	print dontcares
	print max(dontcares)
	#print log(max(dontcares),2)
	print ceil(log(max(dontcares)+1,2))
	for dontcare in dontcares:
		if dontcare not in d[bin(dontcare).count("1")]:
			d[bin(dontcare).count("1")].append(dontcare)
			maxPower = max(maxPower,int(log(max(dontcares)+1,2))+1)
print maxPower

print d.items()
#if  d[0]:
#	print d[0] #Testing
coloumns = dict()
primeimplicants = list()
taken = list()
for key in sorted(d):
	#iterate over each list and thenext list
	if   d[key+1] is not None:
	#	continue
	#else:
		print d[key]
		print d[key+1]
		#mcol = defaultdict(list)
		for i in d[key]:
			for j in d[key+1]:
				if (bin(i^j).count("1")==1):
					taken.append(i)
					taken.append(j)
					#print i , j 
						#print i, j, "IT IS WORKING :D"
					#mcol[key].append()
					bitdif(i,j)
primeimplicants = [x for x in minterms if x not in taken]
print coloumns
print primeimplicants
					
#print primeimplicants


	