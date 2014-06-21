#!/usr/bin/env python
def rules(hkl):
    (h,k,l) = hkl.strip('(').strip(')').split(',')
    try:
        hh = int(h)
        hrule = rulefixed
    except ValueError:
        if h=='h':
            hh = 1
        else:
            hh = int(h.strip('h'))
        hrule = rulefactor
    try:
        kk = int(k)
        krule = rulefixed
    except ValueError:
        if k=='k':
            kk = 1
        else:
            kk = int(k.strip('k'))
        krule = rulefactor
    try:
        ll = int(l)
        lrule = rulefixed
    except ValueError:
        if l=='l':
            ll = 1
        else:
            ll = int(l.strip('l'))
        lrule = rulefactor
    return ((hh,hrule),(kk,krule),(ll,lrule))

def rulefixed(x,k):
    if x==k:
        return True
    else:
        return False

def rulefactor(x,k):
    if x%k:
        return False
    else:
        return True

import sys

((hh,hrule),(kk,krule),(ll,lrule)) = rules(sys.argv[2])
fin = open(sys.argv[1])
for line in fin:
    try:
        (h,k,l) = line.split()[:3]
        h,k,l = int(h),int(k),int(l)
        if hrule(h,hh) and krule(k,kk) and lrule(l,ll):
            print line.strip()
    except ValueError:
        pass
fin.close()

