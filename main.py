import numpy as np
import bisect as bi
#n: bidding levels; m:number of data; mm: number of bidders.
def datagen(m,mm,typ='u'):
    func={'u':np.random.uniform,'e':np.random.exponential,'n':np.random.normal}
    ans=[sorted(func[typ](size=mm),reverse=True) for i in range(m)]
    if typ=='n':
        for i in range(m):
            for j in range(mm):
                ans[i][j]+=10
    return ans
def bib(a,x):
    s=list(a)
    s.reverse()
    return len(s)-bi.bisect(s,x)
data=datagen(10,10)
c=0.1
def optlevels(data,m):
    pre={0:-1,1:0}
    opt={0:0,1:0}
    band=np.r_[max([max(i) for i in data])+0.12:-0.1:-c]
    n=len(band)
    tsum={}
    pre={i:0 for i in range(n)}
    for i in range(1,n):
        tsum[i]=sum([data[j][1]>=band[i] and band[i] or 0 for j in range(m)])
    for i in range(2,n):
        for j in range(1,i):
            tmp=0
            for u in range(m):
                if bib(data[u], band[i])<=1:
                    continue
                if bib(data[u],band[j])>=2:
                    continue
                if bib(data[u],band[j])==0:
                    tmp+=band[i]
                    continue
                cnt=bib(data[u],band[i])-bib(data[u],band[j])
                tmp+=(cnt*band[j]+band[i])/(1.0+cnt)
            if tsum[i]<tsum[j]+tmp:
                tsum[i]=tsum[j]+tmp
                pre[i]=j
    t=n-1
    level=[]
    while t:
        level+=[band[t]]
        t=pre[t]
    level+=[band[0]]
    return level
def second_price(data):
    return sum([i[1] for i in data])
def second_bid(data):
    return sum([level[bi.bisect(level,i[1])-1] for i in data])
def extended_sp(data,level):
    ans=0
    for i in data:
        x=bi.bisect(level,i[1])-1
        t1=bib(i,level[x])
        t2=bib(i,level[min(x+1,len(level)-1)])
        t=t1-t2
        if t<0:
            print t1,t2
            print data,level
            raw_input()
        if t2:
            ans+=(t*level[x+1]+level[x])/(t+1.0)
        else:
            ans+=level[x]
    return ans
m=100
sp,esp,sb=[],[],[]
typ='n'
mm=10
for c in [0.05,0.1,0.15,0.2,0.25,0.3]:
    for k in range(5):
        print 'c---',c
        data=datagen(m,mm,typ)
        level=optlevels(data, m)
    #     print 'sp',second_price(data)
    #     print 'esp',esp(data, level)
        data=datagen(m,mm,typ)
        tmp1=second_price(data)
        tmp2=extended_sp(data, level)
        tmp3=second_bid(data)
        sp+=[tmp1]
        esp+=[tmp2]
        sb+=[tmp3]
f=file('%s_c.txt'%typ,'w')
f.write(str(sp)+'\n'+str(esp)+'\n'+str(sb))
f.close()