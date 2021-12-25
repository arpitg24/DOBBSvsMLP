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
strats_size = len(strats)

#leader pycx + (1−py)(−vy,x),
#follower −pycq + (1−py)(vy,q)
#		follower     (leader,follower)
#leader		1 	        2
#	1              (-V2x,V2q)
#	2 	(-V1x,V1q) 

R = np.zeros((strats_size,m,2)) #payoff matrix
R_l = np.size(R,0) #dimension for leader
R_f = np.size(R,1)  #dimension for follower

for strat in range(R_l):		 
	for house in range(R_f):
		print(strats[house])
		if(strats[strat][house]==1):
			R[strat][house][0] = py[house]*cx + (1-py[house])*(-Vx[house])
			R[strat][house][1] = -py[house]*cq + (1-py[house])*(Vq[house])
		else:
			R[strat][house][0] = -Vx[house]
			R[strat][house][1] = Vq[house]

print('PayOff Matrix: ')
print(R)

mdl_lead = Model(name='leader')

x = mdl_lead.continuous_var_list(R_l,0,1,'x')
q = mdl_lead.binary_var_list(R_f,name='q')

mdl_lead.add_constraint(mdl_lead.sum(i for i in x)==1)

mdl_lead.maximize(mdl_lead.sum(R[i][np.argmax(R[i][:][1])][0]*q[np.argmax(R[i][:][1])]*x[i] for i in range(R_l)))

sols_lead = mdl_lead.solve()
print(sols_lead)

x = []
for i in range(R_l):
	x.append(sols_lead['x_{}'.format(i)])

mdl_fol = Model(name='follower')

q = mdl_fol.binary_var_list(R_f,name='q')

mdl_fol.add_constraint(mdl_fol.sum(j for j in q)==1)

mdl_fol.maximize(mdl_fol.sum(R[i][j][0]*x[i]*q[j] for i in range(R_l) for j in range(R_f)))

sols_fol = mdl_fol.solve()
print(sols_fol)


