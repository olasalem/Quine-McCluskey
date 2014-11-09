from collections import defaultdict
from math import log, ceil
import difflib
from sets import Set
################################################################################################################
										"""Some Variables"""
################################################################################################################
coloumns = dict()
templst = list()
taken = list()
flag = True
d = defaultdict(list)
maxPower = 0
################################################################################################################
										"""Functions"""
################################################################################################################

def iterations():
	flag = False
	for key in range(0,len(coloumns.keys())-1):
		if d[key] is None:
			break
 		else:
 			bitloc = Xor(int(maxPower),coloumns.keys()[key],coloumns.keys()[key+1])
	 		if bitloc != -2 and  bitloc != -1:
	 			flag = True
	 			# print flag
	 			tkey = list(coloumns.keys()[key])
	 			tkey [int(maxPower)-1-bitloc]= "-"
	 			tkey = ''.join(tkey)
	 			taken.append(coloumns[coloumns.keys()[key]]+coloumns[coloumns.keys()[key+1]])
	 			coloumns[tkey] = coloumns[coloumns.keys()[key]] + coloumns[coloumns.keys()[key+1]]
	templst = [coloumns[x] for x, v in coloumns.items() if coloumns[x] not in taken]
	return	(templst, flag)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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

####################################################################################################################
												"""Main"""
####################################################################################################################
print "Minterms:"
try:
	minterms = map(int , raw_input().split(","))
except ValueError:
	minterms = None
if minterms is not None:	
	maxPower = ceil(log(max(minterms)+1,2))
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
	print int(log(max(dontcares)+1,2))+1
	for dontcare in dontcares:
		if dontcare not in d[bin(dontcare).count("1")]:
			d[bin(dontcare).count("1")].append(dontcare)
			maxPower = max(maxPower,ceil(log(max(dontcares)+1,2)))
primeimplicants = list(list())
for key in sorted(d):
	if d[key+1] is not None:
		print d[key]
		print d[key+1]
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
if minterms is not None:
	primeimplicants = [[x for x in minterms if x not in taken]]
count = 0
while flag == True:
	flag = False
	count += 1
	print "iteration number", count
	templst,flag = iterations()
	primeimplicants.append(templst)
	print "taken " ,taken
	print "coloumns " ,coloumns
	print "templst" , templst
	coloumns.clear()
print "Last Iteration: ", primeimplicants
