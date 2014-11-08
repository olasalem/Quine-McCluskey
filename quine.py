from collections import defaultdict
from math import log, ceil
#n = raw_input()
def Xor(n,str1, str2):
	str1 = str1.replace("0b","")
	str2 = str2.replace("0b","")
	str1 = ''.join(['0']*(n-len(str1))) + str1
	str2 = ''.join(['0']*(n-len(str2))) + str2
	
	lstXor = list()
	for i in range (0,len(str1)):
		if(str1[i] != str2[i]):
			lstXor.append(n-(i+1))
	if(len(lstXor)==0): return -2
	elif(len(lstXor)==1): return lstXor[0]
	else: return -1

#input = raw_input().split(' ')
#str1 = bin(int(input[0]))
#str2 = bin(int(input[1]))
#print Xor(8,str1,str2)


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
		mcol = defaultdict(list)
		for i in d[key]:
			for j in d[key+1]:
				if (bin(i^j).count("1")==1):
					print i, j, "IT IS WORKING :D"



