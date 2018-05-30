mwyaf = 1071
lleiaf = 462
ffactorau = []

# Algorithm Euclid
while mwyaf != 0 and lleiaf != 0:
	lluosrif = 0
	while mwyaf >= lleiaf:
		mwyaf -= lleiaf
		lluosrif += 1
	mwyaf, lleiaf = lleiaf, mwyaf
	# cyfnewid enwau'r newidynnau
	ffactorau.append(lluosrif)
ffactorau.append(mwyaf)
ffactorau.append(lleiaf)

print(max(ffactorau))