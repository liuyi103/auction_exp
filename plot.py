import matplotlib.pyplot as plt
plt.title('How reports and values affect the utility?')
plt.plot([1,3],[0,2.0/3],label='report 1')
plt.plot([1,3],[-2./3,4./3],label='report 2')
plt.ylabel('utility')
plt.xlabel('value')
plt.legend()
plt.show()