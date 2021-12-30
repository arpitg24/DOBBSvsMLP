import numpy as np
from itertools import permutations	
from docplex.mp.model import Model	

m = int(input()) #number of houses
d = int(input()) #number of houses to patrol in one pure strategy

Vx = np.array([int(x) for x in input().split()]) #value of goods in each house for leader
Vq = np.array([int(q) for q in input().split()]) #value of goods in each house for follower
cx = int(input()) #reward to the leader for catching the follower
cq = int(input()) #cost to the follower for getting caught
py = np.array([float(p) for p in input().split()]) #probability of getting caught
X = np.full((d),1)
z = np.zeros((m-d))
X = np.append(X,z)
strats = set(permutations(X))
strats = list(strats)
print(strats)
strats_size = len(strats)

#leader pycx + (1−py)(−vy,x),
#follower −pycq + (1−py)(vy,q)e
#		follower     (leader,follower)
#leader		1 	        2
#	1              (-V2x,V2q)
#	2 	(-V1x,V1q) 

R = np.zeros((strats_size,m,2)) #payoff matrix
R_l = np.size(R,0) #dimension for leader
R_f = np.size(R,1)  #dimension for follower

for strat in range(R_l):		 
	for house in range(R_f):
		if(strats[strat][house]==1):
			R[strat][house][0] = py[house]*cx + (1-py[house])*(-Vx[house])
			R[strat][house][1] = -py[house]*cq + (1-py[house])*(Vq[house])
		else:
			R[strat][house][0] = -Vx[house]
			R[strat][house][1] = Vq[house]

print('PayOff Matrix: ')
print(R)

mdl = Model(name='LP')
strat_lead = mdl.continuous_var_list(R_l,0,1,'strat_lead')
strat_fol = mdl.binary_var_list(R_f,name='strat_fol')

mdl.add_constraint(mdl.sum(i for i in strat_lead)==1)
mdl.add_constraint(mdl.sum(j for j in strat_fol)==1)

for j in range(R_f):
	mdl.add_constraint(mdl.sum(strat_lead[i]*np.max(R[i][:][1]) for i in range(R_l)) >= mdl.sum(strat_lead[i]*R[i][j][1] for i in range(R_l)))

mdl.maximize(mdl.sum(strat_lead[i]*R[i][np.argmax(R[i][:][1])][0] for i in range(R_l)))

sols = mdl.solve()
print(sols)