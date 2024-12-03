from multiprocessing.dummy import active_children
from turtle import pos
from FourRooms import FourRooms
import numpy as np


# Create FourRooms Object
fourRoomsObj = FourRooms('rgb') 
aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']
q_values_red = np.zeros((13, 13, 4))  
q_values_green= np.zeros((13, 13, 4))  
q_values_blue = np.zeros((13, 13, 4))  
epsilon = 0.4  #the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.5 #discount factor for future rewards
learning_rate = 0.7 #the rate at which the agent should learn

#define an epsilon greedy algorithm that will choose which action to take next (i.e., where to move next)
def get_next_action(q_values):
    if np.random.random() < epsilon:
            rows, cols = fourRoomsObj.getPosition()
            ans = np.argmax(q_values[rows, cols])                
            return ans
    else: #choose a random action
            return np.random.randint(4) 
                    
def train():
    global q_values_red
    global q_values_green
    global q_values_blue
    fourRoomsObj.newEpoch()
    position = fourRoomsObj.getPosition()
    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))
    while fourRoomsObj.getPackagesRemaining()>2: 
            act = get_next_action(q_values_red)
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)
            print("Agent took {0} action and moved to {1} of type {2}. Packages Remaining : {3}".format (aTypes[act], newPos, gTypes[gridType], packagesRemaining))
            if gridType == 1:
                reward = 100
            elif gridType > 0:
                reward = -10000
            else:
                reward = -100
            old_q_value = q_values_red[position[0], position[1], act]
            temporal_difference = reward + (discount_factor * np.max(q_values_red[newPos])) - old_q_value
            #update the Q-value for the previous state and action pair
            new_q_value = old_q_value + (learning_rate * temporal_difference)
            q_values_red[position[0], position[1],act] = new_q_value 
            position = newPos 
    while fourRoomsObj.getPackagesRemaining()>1: 
            if isTerminal:
                break
            act = get_next_action(q_values_green)
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)
            print("Agent took {0} action and moved to {1} of type {2}. Packages Remaining : {3}".format (aTypes[act], newPos, gTypes[gridType], packagesRemaining))
            if gridType == 2:
                reward = 100
            elif gridType > 0:
                reward = -10000
            else:
                reward = -100
            old_q_value = q_values_green[position[0], position[1], act]
            temporal_difference = reward + (discount_factor * np.max(q_values_green[newPos])) - old_q_value
            #update the Q-value for the previous state and action pair
            new_q_value = old_q_value + (learning_rate * temporal_difference)
            q_values_green[position[0], position[1],act] = new_q_value 
            position = newPos   
    while fourRoomsObj.getPackagesRemaining()>0: 
            if isTerminal:
                break
            act = get_next_action(q_values_blue)
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)
            print("Agent took {0} action and moved to {1} of type {2}. Packages Remaining : {3}".format (aTypes[act], newPos, gTypes[gridType], packagesRemaining))
            if gridType == 3:
                reward = 100
            elif gridType > 0:
                reward = -10000
            else:
                reward = -100
            old_q_value = q_values_blue[position[0], position[1], act]
            temporal_difference = reward + (discount_factor * np.max(q_values_blue[newPos])) - old_q_value
            #update the Q-value for the previous state and action pair
            new_q_value = old_q_value + (learning_rate * temporal_difference)
            q_values_blue[position[0], position[1],act] = new_q_value 
            position = newPos 

def main():
    global numEpochs
    for episode in range(800): 
        print("Episode =", episode)
        print("____________________\n")
        train()
    global epsilon 
    epsilon = 1 
    for episode in range(500): 
        print("Episode =", episode)
        print("____________________\n")
        train()
  
        
    fourRoomsObj.showPath(-1)
        
if __name__ == "__main__":
    main()
        

