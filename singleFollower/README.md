# DOBSS vs Multiple LP comparison

## Problem description

The game consists of two agents of single type: leader(security agent) and follower(robber).The world is represented by m houses numbered 1 ... m . The robber attempts to steal goods from a house and the security agents patrols the world.

Security agent's set of pure strategies consists fo d houses to patrol in order without visiting the same house twice. Robber's set of pure strategies consists of houses for a robbery attempt.

The reward for the leader and the follower are described in a payoff matrix with a higher reward for the leader if it catches the follower early on in its patrol path.

### DOBBS method
In this method we create two models named leader and follower with their corresponding LPs. The program outputs the payoff matrix as well as the probability for using each strategy for leader and follower

### Multiple LPs method
In this method we create a single model named LP and the program outputs the leader's strategy. 


