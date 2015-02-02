# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:58:47 2015

@author: liuyi103
"""
import numpy as np
import math
pr=lambda x,y:abs(np.e**(-x)-np.e**(-y))
tosel=np.r_[4:-0.01:-0.01]
for m in range(5,10,5):
    prof=-np.ones((401,11))
    pre=np.zeros((401,11))
    for i in range(400):
        
        for j in range(11):
            if j==0:
                tmp=np.e**(-tosel[i])
                prof[i,j]=(1-m*tmp*(1-tmp)**(m-1))*tosel[i]
                continue
            for k in range(i):
                if prof[k,j-1]>0:
                    tmp=prof[k,j-1]+sum([(u*(tosel[k]-tosel[i])/(u+1.0)+tosel[i])*m*\
                    np.e**(-tosel[k])*math.factorial(m-1)/math.factorial(u)/math.factorial(m-1-u)\
                    *pr(tosel[k],tosel[i])**u*(1-np.e**(-i))**(m-1-u) for u in range(1,m)])+\
                    tosel[i]*((1-np.e**(-tosel[i]))**m-(1-np.e**(-tosel[i+1]))**m*(1+(m-1)*np.e**(-tosel[i+1])))
    print prof[:,0] 
                
                
