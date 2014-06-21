#!/usr/bin/env python
import sys
from math import sin, cos, radians
try:
    numshells=int(sys.argv[2])
except IndexError:
    numshells=10
fin=open(sys.argv[1])
fin.readline()
fin.readline()
(a,b,c,alpha,beta,gamma,sg)=fin.readline().strip().split()
a,b,c,alpha,beta,gamma = float(a),float(b),float(c),float(alpha),float(beta),float(gamma)
(sa, sb, sc) = (sin(radians(alpha)), sin(radians(beta)), sin(radians(gamma)))
(ca, cb, cc) = (cos(radians(alpha)), cos(radians(beta)), cos(radians(gamma)))
D = 1.0 - ca**2 - cb**2 -cc**2 +2.0*ca*cb*cc
(s11,s22,s33,s12,s13,s23)=((sa/a)**2/D, 
                (sb/b)**2/D, 
                (sc/c)**2/D, 
                2.0*(ca*cb-cc)/a/b/D,
                2.0*(ca*cc-cb)/a/c/D,
                2.0*(cb*cc-ca)/b/c/D)
h,k,l,Ihkl,sigmaI,resolution=[],[],[],[],[],[]
for line in fin:
    tokens=[int(line[:4]),int(line[4:8]),int(line[8:12]),float(line[12:20]),float(line[20:28])]
    h.append(tokens[0])
    k.append(tokens[1])
    l.append(tokens[2])
    Ihkl.append(tokens[3])
    sigmaI.append(tokens[4])
    resolution.append(pow(s11*h[-1]**2+s22*k[-1]**2+s33*l[-1]**2+s12*h[-1]*k[-1]+s13*h[-1]*l[-1]+s23*k[-1]*l[-1],-0.5))
fin.close()
nref = len(h)
sr = sorted(resolution,reverse=True)
shells, isr, nr, shid = [], [], [], []
i0, s0 =  [], []
for i in range(numshells):
    shells.append(sr[int(nref*i/numshells)])
    isr.append(0.0)
    nr.append(0)
    i0.append(0.0)
    s0.append(0.0)
shells.append(sr[-1])
i_over_s = 0.0
for i in range(nref):
    i_over_s += Ihkl[i]/sigmaI[i]
    dd=resolution[i]
    for (j,edge) in enumerate(shells):
        if dd>=edge:
            shid.append(j)
            break
i_over_s /= float(nref)
for i in range(nref):
    nr[shid[i]-1] += 1
    isr[shid[i]-1] += Ihkl[i]/sigmaI[i]
    i0[shid[i]-1] += Ihkl[i]
    s0[shid[i]-1] += sigmaI[i]
print "  Resolution   Number of      <I>     <sigma>     <I/sigma>   <I>/<sigma>"
print " Low    High  reflections        "
for i in range(numshells):
    print "%6.3f %6.3f %8d     %8.3f  %8.3f    %8.3f     %8.3f" % (shells[i],shells[i+1],nr[i],i0[i]/nr[i],s0[i]/nr[i],isr[i]/nr[i],i0[i]/s0[i])
print     "%6.3f %6.3f %8d     %8.3f  %8.3f    %8.3f     %8.3f" % (shells[0],shells[-1],nref,sum(i0)/nref,sum(s0)/nref,i_over_s,sum(i0)/sum(s0))

