import matplotlib.pyplot as plt
import numpy as np
typ='n'
maps={'u':'uniform distribution','e':'exponential distribution','n':'normal distribution'}
f=file('%s_c.txt'%typ,'r')
s1,s2,s3=f.readlines()
sp,esp,sb=[],[],[]
exec 'sp='+s1
exec 'esp='+s2
exec 'sb='+s3
print sp,esp,sb
plt.title('How number of bidding levels affect the revenue? (%s)'%maps[typ])
plt.xlabel('the gap between neighboring bidding levels')
plt.ylabel('revenue')
plt.plot([0.05,0.1,0.15,0.2,0.25,0.3],[np.mean(sp[i*5:i*5+5]) for i in range(6)], label='second value')
plt.plot([0.05,0.1,0.15,0.2,0.25,0.3],[np.mean(esp[i*5:i*5+5]) for i in range(6)], label='extended second price')
plt.plot([0.05,0.1,0.15,0.2,0.25,0.3],[np.mean(sb[i*5:i*5+5]) for i in range(6)], label='second price')
plt.legend(loc='bottum_right')
plt.show()