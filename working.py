################################################################################################################
#										   Libraries
################################################################################################################
from collections import defaultdict
from math import log, ceil
import difflib
from sets import Set
Variables = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]

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
				 			# print flag
				 			tkey = list(coloumns.keys()[key])
				 			tkey [int(maxPower)-1-bitloc]= "-"
				 			tkey = ''.join(tkey)
				 			taken.append(tuple(set(coloumns[coloumns.keys()[key]]+coloumns[coloumns.keys()[nkey]])))
				 			coloumns[tkey] = tuple(set((coloumns[coloumns.keys()[key]] + coloumns[coloumns.keys()[nkey]])))
	templst = [coloumns[x] for x, v in coloumns.items() if coloumns[x] not in taken]
	# print "Iteration # ", count ,"templst",templst
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
def DCR():
	DominatedCols = list()
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
	print "b3d zft duplicate",primeImplicants
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
	deleted = set()
	temp = set()
	xx = False
	try:
		for key1 in minterms:
			for key2 in minterms:
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
		#print "DominatedCols",DominatedCols
		minterms[:] = [j for j in minterms if j not in DominatedCols]
		for item in deleted:
			for v in primeImplicants:
				for i in v:
					if item is i: temp.add(v)
		primeImplicants [:] = [item for item in primeImplicants if item not in temp]
	except TypeError:
		None
	#print minterms
	print "b3d zft cols",primeImplicants
	return flag
####################################################################################################################
def output(str1):
	strx = ""
	for i in range (0,len(str1)):
		c = str1[len(str1)-i-1]
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
	# print dontcares
	# print max(dontcares)
	# print int(log(max(dontcares)+1,2))+1
	for dontcare in dontcares:
		if dontcare not in d[bin(dontcare).count("1")]:
			d[bin(dontcare).count("1")].append(dontcare)
			maxPower = max(maxPower,ceil(log(max(dontcares)+1,2)))
primeimplicants = list(list())
for key in sorted(d):
	if d[key+1] is not None:
		# print d[key]
		# print d[key+1]
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
					# print position
					xstr = ""
					for k in range(0,len(str1)):
						if k!= position : xstr+= str2[k]
						else : xstr += '-'
					coloumns[xstr] = (i,j)
if minterms is not None:
	primeimplicants = [[x for x in minterms if x not in taken]]
count = 0
epi = list()
while flag == True:
	flag = False
	count += 1
	templst,flag = iterations(count)
	epi.append(templst)

	primeimplicants.append(taken)

primeImplicants = []
primeImplicants [:]= [v for k,v in coloumns.items()]
print"primeimplicants table:"

print "final PI:"
for i in primeImplicants:
	print i
while (True):
	if minterms is not None:

		flag = DCR()
		print "mintermssssss",minterms
		print "prrrrrr",primeImplicants
	if flag is False: break
EPI.update(set(primeImplicants))

function = []
function [:] = [key for i in EPI for key,value in coloumns.items() if value is i ]
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

