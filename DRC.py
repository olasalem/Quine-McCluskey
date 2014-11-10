from collections import defaultdict
minterms = []
EPI = list() 
primeImplicants = []
count = defaultdict(list)

def DCR():
	flag = False
	deleted = list()
	Dominatedrows = list()

	for minterm in minterms:
		for v in primeImplicants:
			for i in v:
				if minterm is i : count[minterm].append(v)

		if len(count[minterm]) is 1 : 
			flag = True
			EPI.append(count[minterm][0])
	primeImplicants[:] = [item for item in primeImplicants if item not in EPI]
	
	for item in EPI:
		for j in item:
			if j in minterms:
				deleted.append(j)
	minterms[:] = [j for j in minterms if j not in deleted]
	"""for item in deleted:
		if item in count:
			del count[item]"""
	
	xx = False
	for key1 in minterms:
		for key2 in minterms:
			if key1 is key2 or  len(count[key1])> len(count[key2]) : continue
			else :
				xx = True
				print count[key1], count[key2]
				for v in count[key1]:
					if v not in count[key2]: 
						xx= False
						break
				if xx is False: continue
				else:
					xx = True
					print key1,key2
					Dominatedrows.append(key2)
	print "Dominatedrows",Dominatedrows
	minterms[:] = [j for j in minterms if j not in Dominatedrows]
	print minterms

	return flag

minterms = [0 ,2, 5, 6, 7, 8, 10, 12, 13, 14, 15]
primeImplicants = [(0,2,8,10), (2,6,10,14),(8,10,12,14),(12,13,14,15), (14,15,6,7), (5,7,13,15)]
while (True):
	flag = DCR()
	print "minterms", minterms
	print EPI
	print primeImplicants
	if flag == False: break
print "Done"
print primeImplicants





