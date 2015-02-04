# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:55:29 2015

@author: liuyi103
"""

import matplotlib.pyplot as plt
ss=file('ijcai.txt','r').readlines()
ans1,ans2,ans3=[0]*10,[0]*10,[0]*10
for i in ss:
    exec 'n,t1,t2,t3='+i
    ans1[n/10-1]+=t1/20
    ans2[n/10-1]+=t2/20
    ans3[n/10-1]+=t3/20
plt.plot(range(10,110,10)[:-1],ans1[:-1],label='ESP')
plt.plot(range(10,110,10)[:-1],ans2[:-1],label='SV')
plt.plot(range(10,110,10)[:-1],ans3[:-1],label='SP')
plt.xlabel('number of bidders',size=15)
plt.ylabel('revenue',size=15)
plt.legend(loc='lower right')

plt.savefig('dp.pdf',dpi=1200)
plt.show()