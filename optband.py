from FuncDesigner import *
from openopt import *
import math
import numpy as np
import matplotlib.pyplot as plt
def c(x,y,z):
    return math.factorial(x)/math.factorial(y)/math.factorial(z)/math.factorial(x-y-z)
n=5
m=10
def mainfun():
    p=oovar()
    startPoint={p:[1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.07,0.03,0.01]}
    cons=[p[i]>p[i+1] for i in range(n-1)]+[p[0]==1,p[n-1]==0.000]
    rev1=lambda i,k:(1-p[i])*p[i+1]**(m-1-k)*(p[i]-p[i+1])**k*c(m,1,k)*(p[i]*k+p[i+1])/(k+1.)
    rev2=lambda i: p[i]*(p[i-1]**m-p[i]**m-m*(1-p[i])*p[i]**(m-1))
    objective=sum([rev1(i,k)for i in range(1,n-1) for k in range(1,m-1)])+sum([rev2(i) for i in range(1,n-1)])
    prob = NSP(objective, startPoint, constraints = cons)
    solver = 'ralg'
    r = prob.maximize(solver)
    opt=r(p)
    p=opt
    rev1=lambda i,k:(1-p[i])*p[i+1]**(m-1-k)*(p[i]-p[i+1])**k*c(m,1,k)*(p[i]*k+p[i+1])/(k+1.)
    rev2=lambda i: p[i]*(p[i-1]**m-p[i]**m-m*(p[i-1]-p[i])*p[i]**(m-1))
    objective=sum([rev1(i,k)for i in range(1,n-1) for k in range(1,m-1)])+sum([rev2(i) for i in range(1,n-1)])
    print sum([rev1(i,k)for i in range(1,n-1) for k in range(1,m-1)]),sum([rev2(i) for i in range(1,n-1)])
    return opt[:n],objective
for n in range(3,10):
    bands=[]
    objs=[]
    for m in range(5,55,5):
        band,obj=mainfun()
        f=file('record.txt','a')
        f.write('%d %d %s %f\n'%(n,m,str(band),obj))
        f.close()
        bands+=[band[1:-1]]
        objs+=[obj]
    plt.title('optimal bidding levels and corresponding revenue when n=%d'%n)
    plt.xlabel('number of bidders')
    plt.ylabel('revenue (red) or bidding levels (blue)')
    plt.plot(range(5,55,5),bands,label='bidding levels',color='b')
    plt.plot(range(5,55,5),objs,label='revenue',color='r')
    #plt.legend(loc='bottomright')
    plt.savefig('n%d.pdf'%n)
    plt.clf()
