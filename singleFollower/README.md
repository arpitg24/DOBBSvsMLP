# DOBSS vs Multiple LP comparison

## Problem description

The game consists of two agents of single type: leader(security agent) and follower(robber).The world is represented by m houses numbered 1 through m . The robber attempts to steal goods from a house and the security agents patrols the world.

Security agent's set of pure strategies consists fo d houses to patrol in order without visiting the same house twice. Robber's set of pure strategies consists of houses for a robbery attempt.

The reward for the leader and the follower are described in a payoff matrix with a higher reward for the leader if it catches the follower early on in its patrol path.

### Input method
Provide input to he programs using an input file (input.txt)
For eg. python3 multipleLP.py < input.txt 
the input file must be in the following format:
* number of houses(m)
* number of houses for the leader to patrol in one pure strategy
* value of goods in each house for leader(space seperated integers containing m entries)
* value of goods in each house for follower (space seperated integers containing m entries)
* reward to leader for catching the follower
* cost to the follower for getting caught
* probability of getting caught in that house (space seperated floats containing m entries)

### DOBBS method
In this method we create two models named leader and follower with their corresponding LPs. The program outputs the payoff matrix as well as the probability for using each strategy for leader and follower.

![Screenshot from 2021-12-15 21-52-12](https://user-images.githubusercontent.com/52707368/146224623-48e4fc07-aaab-4b0a-894f-b2d60ce29f6b.png)


### Multiple LPs method
In this method we create a single model named LP and the program outputs the leader's strategy. 

![Screenshot from 2021-12-15 21-53-53](https://user-images.githubusercontent.com/52707368/146224697-9c5fb13a-815a-41da-9143-eeb2c3f32e85.png)

