################################################################################################################
#										   Libraries
################################################################################################################
from collections import defaultdict
from math import log, ceil
import difflib
from sets import Set
################################################################################################################
#										"""Some Variables"""
################################################################################################################
coloumns = dict()
templst = list()
taken = list()
flag = True
d = defaultdict(list)
maxPower = 0
countDict = defaultdict(list)
minterms = []
EPI = set() 
uncovered =set()
covered = set()
essentials = set()
Variables = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

################################################################################################################
#										"""Functions"""
################################################################################################################

def iterations(count):
	flag = False
	for key in range(0,len(coloumns.keys())-1):
		if d[key] is None:
			break
 		else:
 			if coloumns.keys()[key].count("-") == count:
 				for nkey in range(0,len(coloumns.keys())-1):
 					if nkey is not key:
	 					bitloc = Xor(int(maxPower),coloumns.keys()[key],coloumns.keys()[nkey])
				 		if bitloc != -2 and  bitloc != -1:
				 			flag = True
				 			tkey = list(coloumns.keys()[key])
				 			tkey [int(maxPower)-1-bitloc]= "-"
				 			tkey = ''.join(tkey)
				 			taken.append(tuple(set(coloumns[coloumns.keys()[key]]+coloumns[coloumns.keys()[nkey]])))
				 			coloumns[tkey] = tuple(set((coloumns[coloumns.keys()[key]] + coloumns[coloumns.keys()[nkey]])))
	return	(flag)
######################################################################################################################
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
def Ess():
	flag = False
	deleted = list()
	temp = list()
	try:
		for minterm in minterms:
			for v in primeImplicants:
				for i in v:
					if minterm is i : countDict[minterm].append(v)

			if len(countDict[minterm]) is 1 : 
				flag = True
				EPI.add(countDict[minterm][0])
		primeImplicants[:] = [item for item in primeImplicants if item not in EPI]
		
		for item in EPI:
			for j in item:
				if j in minterms:
					deleted.append(j)
		minterms[:] = [j for j in minterms if j not in deleted]
		temp [:] = [ item for item in primeImplicants for i in item for j in deleted if i is j]
		primeImplicants [:] = [item for item in primeImplicants if item  not in temp]
	except TypeError:
		None
	return flag
####################################################################################################3
def DC():
	deleted = set()
	temp = set()
	xx = False
	DominatedCols = list()
	try:
		for key1 in uncovered:
			for key2 in uncovered:
				if key1 is key2 or  len(countDict[key1])> len(countDict[key2]) : continue
				else :
					xx = True
					for v in countDict[key1]:
						if v not in countDict[key2]: 
							xx= False
							break
					if xx is False: continue
					else:
						xx = True
						deleted.add(key1)
						DominatedCols.append(key2)
		uncovered= uncovered - deleted #=[:] = [j for j in minterms if j not in DominatedCols]
		temp = set([v for item in deleted for v in PICopy if item in v])
		#primeImplicants [:] = [item for item in primeImplicants if item not in temp]
		PICopy [:] = [item for item in PICopy if item not in temp]

	except TypeError:
		None
	return xx

#####################################################################################################3
def DR():
	flag = False
	print "minterms",minterms
	set1 = set()
	set2 = set()
	temp = set()
	#for item1 in  primeImplicants:
		#for item2 in primeImplicants:
	for item1 in  PICopy:
		for item2 in PICopy:
			if item1 is item2 or len(item1) > len(item2): continue
			else:
				set1 = set([i for i in item1])
				set2 = set ([i for i in item2])
				if set1.issubset(set2):
					flag = True
					temp.add(item1)
	#primeImplicants [:] = [item for item in primeImplicants if item not in temp]
	PICopy [:] = [item for item in PICopy if item not in temp]
	print "rows dominated",temp
	return flag


	
####################################################################################################################
def output(str1):
	strx = ""
	for i in range (0,len(str1)):
		c = str1[i]
		if c is "1":
			strx += Variables[i]
		elif c is "0":
			strx = strx+ Variables[i]+"`"
		elif c is "-": continue
	if strx is "":
		strx = "1"
	return strx
####################################################################################################################
#											"""Main"""
####################################################################################################################
print "Minterms:"
mintermsSet = set()
PICopy = []
try:
	minterms = map(int , raw_input().split(","))
	while min(minterms) < 0 or max(minterms) >= 2**16:
		print "Minterms: Should be between 0 and 2^16"
		minterms = map(int , raw_input().split(","))
	mintermsSet = set(minterms)
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
	while min(dontcares) < 0 or max(dontcares) >= 2**16:
		print "Don`t Cares: Should be between 0 and 2^16"
		dontcares = map(int , raw_input().split(","))
except ValueError:
	dontcares = None
if(dontcares != None):
	for dontcare in dontcares:
		if dontcare not in d[bin(dontcare).count("1")]:
			d[bin(dontcare).count("1")].append(dontcare)
			maxPower = max(maxPower,ceil(log(max(dontcares)+1,2)))
for key in sorted(d):
	if d[key+1] is not None:
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
					xstr = ""
					for k in range(0,len(str1)):
						if k!= position : xstr+= str2[k]
						else : xstr += '-'
					coloumns[xstr] = (i,j)
try:
	primeimplicants = [x for x in minterms if x not in taken]
except TypeError:
	None
count = 0
while flag == True:
	count += 1
	flag = iterations(count)
primeImplicants = []
primeImplicants [:]= [v for k,v in coloumns.items()]
# print primeImplicants
"""print"primeimplicants table:"
for i in primeImplicants:
	print i"""
set1 = set()
set2 = set()
duplicates = set()
for v in primeImplicants:
	for u in primeImplicants:
		if v is u or len(v) > len (u) : continue
		else:
			set1 = set([i for i in v])
			set2 = set([j for j in u])
			if set1.issubset(set2): 
				duplicates.add(v)
primeImplicants [:] = [v for v in primeImplicants if v not in duplicates]
try:
	for x in minterms:
	 	if x not in taken:
	 		essentials.add(x)
	 		tstr = bin(x).replace("0b","")
			tstr = ''.join(['0']*(int(maxPower)-len(tstr))) + tstr
			coloumns[tstr] = (x)
			print tstr
except TypeError:
	None
print "final PI:"
PICopy = list(primeImplicants)
for i in primeImplicants:
	print i
print "Done"
print "PI after DRC",primeImplicants
print "Eseesntials", EPI
function = []
function [:] = [key for i in EPI for key,value in coloumns.items() if value is i ]
print "********************"
print coloumns
print "********************"
print "minterm remaining", minterms
print "primeimplicants", primeImplicants
uncoveredPI = set(PICopy)
print "Minterms copy:"
print mintermsSet
for m in mintermsSet:
	if m not in covered:
		count = 0
		tempEssent = tuple()
		for t in PICopy:
			if m in t:
				count += 1
				if count is 1:
					tempEssent = t
		if count is 1:
			essentials.add(tempEssent)
			uncoveredPI.remove(tempEssent)
			for x in tempEssent:
				if x in mintermsSet:
					covered.add(x)
print "Essential Prime Implicants:"
print essentials
print minterms
#while minterms is not None:
	#flag = Ess()	
	#flag1 = DC()
	#flag2 = DR()
	#if flag1 is False: break
#print "Done"
#print "PI after DRC",PICopy
#print "Eseesntials", EPI
remaining = set()
uncovered = mintermsSet - covered
covered.clear()
for m in uncovered:
	if m not in covered:
		for t in uncoveredPI:
			if m in t:
				remaining.add(t)
				for x in t:
					covered.add(x)
				break
#print function
#print EPI
print essentials
if minterms is not None:
	cover = list(essentials) + list(remaining)
else:
	cover = primeImplicants 
print "Cover:"
function [:] = [key for i in cover for key,value in coloumns.items() if value is i ]
for i in function:
	print i
	print output(i)
v  = list()
v = Variables[0:int(maxPower)]
finalOutput = list()
finalOutput [:] = [output(i) for i in function]
print "function ", str(v).replace(']',')').replace('[','(').replace("'",""), "=",

if "1" in finalOutput:print "1"
else:
	for i in range (0,len(finalOutput)):
		print finalOutput[i],
		if i is not len(finalOutput)-1:
			print "+",
	print " "