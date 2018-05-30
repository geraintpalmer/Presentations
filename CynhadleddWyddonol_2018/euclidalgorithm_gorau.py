def tynnu_lluosrifau(mwyaf, lleiaf):
    """
    Faint o weithiau mae un rhif yn mynd mewn i rhif arall
    """
    lluosrif = 0
    while mwyaf >= lleiaf:
        mwyaf -= lleiaf
        lluosrif += 1
    return mwyaf, lleiaf, lluosrif

def ffactor_mwyaf_cyffredin(mwyaf, lleiaf):
    """
    Algorithm Euclid y canfod ffactor mwyaf cyffredin dau rhif
    """
    ffactorau = []
    while mwyaf != 0 and lleiaf != 0:
        lleiaf, mwyaf, lluosrif = tynnu_lluosrifau(mwyaf, lleiaf)
        ffactorau.append(lluosrif)
    ffactorau.append(mwyaf)
    ffactorau.append(lleiaf)
    return max(ffactorau)

print(ffactor_mwyaf_cyffredin(1071, 462))