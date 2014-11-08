from collections import defaultdict
from math import log, ceil
import difflib
#n = raw_input()
"""def Xor(str1, str2):
	str1.replace("0b","")
	str2.replace("0b","")
"""
coloumns = dict()
"""def bitdif(i,j):
	str1 = bin(i)
	str2 = bin(j)
	#print str1,str2
	str1 = str1.replace("0b","")
	str2 = str2.replace("0b","")
	str1 = ''.join(['0']*(int(maxPower)-len(str1))) + str1
	str2 = ''.join(['0']*(int(maxPower)-len(str2))) + str2
	print "Strings are: ",str1,str2
	xstr = ""
	#str1 = bin(i)
	#str2 = bin(j)
	for x,s in enumerate(difflib.ndiff(str1,str2)):
		print "X is: ",x
		if x==len(str1): continue
		if s[0] == " ":
			xstr += str1[x]
		#print str1[i]
		elif(s[0] == "-" or s[0]=="+" ) :
			xstr += "-"
		#print i,j,xstr
	coloumns[xstr] = (i,j)
	return"""
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

# input = raw_input().split(' ')
# str1 = bin(int(input[0]))
# str2 = bin(int(input[1]))
# print Xor(8,str1,str2)
print "Minterms:"
minterms = map(int , raw_input().split(","))
#print minterms
#print max(minterms)
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
primeimplicants = list()
taken = list()
for key in sorted(d):
	#iterate over each list and thenext list
	if d[key+1] is not None:
	#	continue
	#else:
		print d[key]
		print d[key+1]
		#mcol = defaultdict(list)
		for i in d[key]:
			for j in d[key+1]:
				if (bin(i^j).count("1")==1):
					str1 = bin(i)
					str2 = bin(j)
					str1 = str1.replace("0b","")
					str2 = str2.replace("0b","")
					str1 = ''.join(['0']*(int(maxPower)-len(str1))) + str1
					str2 = ''.join(['0']*(int(maxPower)-len(str2))) + str2
					position = -1;
					taken.append(i)
					taken.append(j)
					strx = bin(i^j).replace("0b","")
					strx = ''.join(['0']*(int(maxPower)-len(strx))) + strx
					for m in range (0,len(strx)):
						if(strx[m]=="1"): position = m;
					print position
					xstr = ""
					for k in range(0,len(str1)):
						if k!= position : xstr+= str2[k]
						else : xstr += '-'
					coloumns[xstr] = (i,j)
					#bitdif(i,j)
primeimplicants = [x for x in minterms if x not in taken]
# for x in enumerate(coloumns.keys()):
#  	if x[0]+1 > len(coloumns):
#  		print x[0]+1
# for key in enumerate(coloumns.keys()):
# 	if (key[0]+2) < len(coloumns):
# 		Xor(maxPower,coloumns[key[1]],coloumns[])
#print primeimplicants

#print primeimplicants
# print coloumns
# coloumns = {x : coloumns[x] for x in sorted(coloumns.keys(), key = lambda key: key.count('1'))}
# print coloumns
del taken [:]
#taken =list(tuple)
for key in range(0,len(coloumns.keys())-1):
 	if coloumns.items()[key+1] is not None:
 		# for i in coloumns.keys()[key]:
 		# 	for j in coloumns.keys()[key+1]:
 		# 
 		bitloc = Xor(int(maxPower),coloumns.keys()[key],coloumns.keys()[key+1])
 		#print bitloc , coloumns.items()[key] , coloumns.items()[key+1]
 		if bitloc != -2 and  bitloc != -1:
 			tkey = list(coloumns.keys()[key])
 			#print tkey
 			tkey [int(maxPower)-1-bitloc]= "-"
 			#print tkey
 			tkey = ''.join(tkey)
 			taken.append(coloumns[coloumns.keys()[key]]+coloumns[coloumns.keys()[key+1]])
 			coloumns[tkey] = coloumns[coloumns.keys()[key]] + coloumns[coloumns.keys()[key+1]]
#print taken
print coloumns 
primeimplicants = [coloumns[x] for x, v in coloumns.items() if coloumns[x] not in taken]
print primeimplicants