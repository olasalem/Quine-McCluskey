from collections import defaultdict
from math import log, ceil
#n = raw_input()
def Xor(str1, str2):
	str1.replace("0b","")
	str2.replace("0b","")





print "Minterms:"
minterms = map(int , raw_input().split(","))
print minterms
print max(minterms)
#print log(max(minterms)+1,2) For testing
maxPower = ceil(log(max(minterms)+1,2))
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
			maxPower = max(maxPower,ceil(log(max(dontcares)+1,2)))
print maxPower

print d.items()
#if  d[0]:
#	print d[0] #Testing
coloumns = list()
primeimplicants = list()
for key in sorted(d):
	#iterate over each list and thenext list
	if not d[key] or not d[key+1]:
		"""for item in d[key]:
			primeimplicants.append(item)""" 
		continue
	else:
		mcol = defaultdict(list)
		for i in d[key]:
			for j in d[key+1]:
				if (bin(i^j).count("1")==1):
					print i, j, "IT IS WORKING :D"
					#mcol[key].append()
#print primeimplicants


	