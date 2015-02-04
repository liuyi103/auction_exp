# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:52:11 2015

@author: liuyi103
"""

import numpy as np
import bisect
find=bisect.bisect
n,m=100,100
#n is the number of data; m is the number of bidders
for m in range(10,110,10):
    print m
    for kk in range(20):
        data=np.random.exponential(size=(n,m))
        up=np.max(data)
        up=round(up,1)
        levels=np.r_[up+0.1:-0.1:-0.1]
        t=len(levels)
        pre=[[0]]
        a=[0]
        data=np.sort(data)
        rev=lambda x,y,z:0 if (find(data[x],levels[y])!=m-1 or find(data[x],levels[z])>m-2)\
         else (levels[y]*(m-1.0-find(data[x],levels[z]))+levels[z])/(m-find(data[x],levels[z]))
        trev1=lambda y,z:sum([rev(x,y,z)for x in range(n)])
        trev2=lambda y,z:sum([levels[z] for x in range(n) if data[x][-1]<levels[y] and data[x][-2]>levels[z]])
        trev=lambda y,z:trev1(y,z)+trev2(y,z)
        for i in range(t):
            tmp=0
            for j in range(n):
                if data[j][-2]>levels[i]:
                    tmp+=levels[i]
            a.append(tmp)
            pre.append([i])
            for j in range(i):
                tmp=trev(j,i)+a[j]
                if tmp>a[-1]:
                    a[-1]=tmp
                    pre[-1]=pre[j]+[i]
        data=np.sort(np.random.exponential(size=(n,m)))
        ans1,ans2,ans3=a[0],0,0
        for i in range(1,len(pre[-1])):
            ans1+=trev(pre[-1][i-1],pre[-1][i])
        print ans1
        levels=np.array(levels)[pre[-1]][::-1]
        ans2=np.sum(data[:,-2])
        ans3=np.sum([levels[find(levels,data[i][-2])-1] for i in range(n)])
        f=file('ijcai.txt','a')
        f.write(str(m)+','+str(ans1)+','+str(ans2)+','+str(ans3)+'\n')
    
    