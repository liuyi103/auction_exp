import numpy as np
import bisect
find=bisect.bisect
n,m=100,100
f=file('ijcai.txt','w')
f.close()

#n is the number of data; m is the number of bidders
def genInstance(m):
    return sorted(np.random.exponential(size=(m)))

def getRevenue(instance, levels):
    '''
    Get the revenue for a single instance
    :param instance: A sorted list
    :param levels:  A sorted list, should start with 0
    :return:
    '''
    top, second = instance[-1], instance[-2]
    l1, l2 = find(levels, top), find(levels, second)
    if l1 == l2:
        return levels[l1-1]
    cnt_l2 = len(instance) - 1 - find(instance, levels[l2-1])
    return (cnt_l2 * levels[l2-1] + levels[l2]) / (cnt_l2 + 1.0)

# num_instance = 20
#
# '''
# In the following code, we want to select 5 bid levels from level_base
# '''
# level_base = np.r_[0:1:0.01]
# print level_base
# for m in range(10, 110, 10):
#     instances = [genInstance(m) for i in range(num_instance)]
#     dp = {(0, 1):[0]}
#     for k, level in enumerate(level_base):
#         if k == 0:
#             continue
#         for n_level in range(1, 6):
#             if (k-1, n_level-1) not in dp:
#                 break
#             dp[k][n_level]
import math

def getr(lastlevel, level, n):
    '''

    :param lastlevel:
    :param level:
    :param n: the number of bidders
    :return: the revenue
    '''
    # case 1, if there are more than one between the two levels.
    p1 = 0
    for k in range(2, n+1):
        p1 += lastlevel*(1-math.exp(-lastlevel))**(n-k)*(math.exp(-lastlevel)-math.exp(-level))**k*math.factorial(n)/math.factorial(k)/math.factorial(n-k)
    # case 2, the top one is above level
    p2 = 0
    for k in range(1,n):
        p2 += math.factorial(n)/math.factorial(k)/math.factorial(n-1-k)*(lastlevel+k*level)/(k+1.)*(1-math.exp(-lastlevel))**(n-k-1)*(math.exp(-lastlevel)-math.exp(-level))**k*math.exp(-level)
    return p1+p2
for n in range(10, 110, 10):
    factor = -math.log(1./n, math.e)*3
    dp = np.zeros((101, 6))
    for i in range(1, 101):
        level = i * 0.01 * factor
        for k in range(6):  # k is the number of bid levels used.
            for j in range(i):
                lastlevel = j * 0.01 * factor
                dp[i][k] = max(dp[i][k], dp[j][k-1] + getr(lastlevel, level, n))
    print dp[-1,-1]
# for m in range(10,110,10):
#     print m
#     for kk in range(20):
#         data=np.random.exponential(size=(n,m))
#         up=np.max(data)
#         up=round(up,1)
#         levels=np.r_[up+0.1:-0.1:-0.1]
#         t=len(levels)
#         pre=[[0]]
#         a=[0]
#         data=np.sort(data)
#         rev=lambda x,y,z:0 if (find(data[x],levels[y])!=m-1 or find(data[x],levels[z])>m-2)\
#          else (levels[y]*(m-1.0-find(data[x],levels[z]))+levels[z])/(m-find(data[x],levels[z]))
#         trev1=lambda y,z:sum([rev(x,y,z)for x in range(n)])
#         trev2=lambda y,z:sum([levels[z] for x in range(n) if data[x][-1]<levels[y] and data[x][-2]>levels[z]])
#         trev=lambda y,z:trev1(y,z)+trev2(y,z)
#         for i in range(t):
#             tmp=0
#             for j in range(n):
#                 if data[j][-2]>levels[i]:
#                     tmp+=levels[i]
#             a.append(tmp)
#             pre.append([i])
#             for j in range(i):
#                 tmp=trev(j,i)+a[j]
#                 if tmp>a[-1]:
#                     a[-1]=tmp
#                     pre[-1]=pre[j]+[i]
#         data=np.sort(np.random.exponential(size=(n,m)))
#         ans1,ans2,ans3=a[0],0,0
#         for i in range(1,len(pre[-1])):
#             ans1+=trev(pre[-1][i-1],pre[-1][i])
#         print ans1
#         levels=np.array(levels)[pre[-1]][::-1]
#         ans2=np.sum(data[:,-2])
#         ans3=np.sum([levels[find(levels,data[i][-2])-1] for i in range(n)])
#         f=file('ijcai.txt','a')
#         f.write(str(m)+','+str(ans1)+','+str(ans2)+','+str(ans3)+'\n')