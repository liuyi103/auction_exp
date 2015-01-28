import pulp as pp
prob=pp.LpProblem('lyc',pp.LpMaximize)
x=pp.LpVariable.dict('x',[0,1],cat=pp.LpBinary)
prob+=sum(x),''
prob+=x[0]+x[1]>=5,''
prob.writeLP('a.lp')
prob.solve()
print prob.objective
for i in range(2):
    print x[i].value()
