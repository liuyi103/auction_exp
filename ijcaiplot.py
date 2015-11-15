# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 20:55:29 2015

@author: liuyi103
"""

import matplotlib.pyplot as plt
import seaborn
ss=file('ijcai.txt','r').readlines()
ans1,ans2,ans3=[0]*10,[0]*10,[0]*10
for i in ss:
    exec 'n,t1,t2,t3='+i
    ans1[n/10-1]+=t1/20
    ans2[n/10-1]+=t2/20
    ans3[n/10-1]+=t3/20

plt.plot(range(10, 100, 10), ans1[ : -1], '.-', label = 'extended second price')
plt.plot(range(10, 100, 10), ans2[ : -1], '*-', label = 'second value')
plt.plot(range(10, 100, 10), ans3[ : -1], '>-', label = 'second price')
plt.xticks(range(10, 100, 10), [str(i) for i in range(10, 100, 10)])
plt.xlim((0, 100))
plt.ylim((0, 500))
plt.xlabel('number of bidders',size=15)
plt.ylabel('revenue',size=15)
plt.legend(loc='upper left')
plt.savefig('dp.pdf',dpi=1200)
plt.show()