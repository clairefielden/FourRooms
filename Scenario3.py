from multiprocessing.dummy import active_children
from turtle import pos
from FourRooms import FourRooms
import numpy as np


aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

q_r = np.zeros((13, 13, 4))
q_g = np.zeros((13, 13, 4))
q_b = np.zeros((13, 13, 4))
q = 0.4
df = 0.5
lr = 0.7

def get_next_action(q_values, fourRoomsObj):
    if np.random.random() < q:
        rows, cols = fourRoomsObj.getPosition()
        ans = np.argmax(q_values[rows, cols])
        return ans
    else:  # choose a random action
        return np.random.randint(4)


def train(fourRoomsObject):
    global q_r
    global q_g
    global q_b
    fourRoomsObject.newEpoch()
    position = fourRoomsObject.getPosition()
    print('Agent starts at: {0}'.format(fourRoomsObject.getPosition()))
    while fourRoomsObject.getPackagesRemaining() > 2:
        act = get_next_action(q_r, fourRoomsObject)
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObject.takeAction(act)
        print("Agent took {0} action and moved to {1} of type {2}. Packages Remaining : {3}".format(aTypes[act], newPos,
                                                                                                    gTypes[gridType],
                                                                                                    packagesRemaining))
        if gridType == 1:
            reward = 100
        elif gridType > 0:
            reward = -10000
        else:
            reward = -100
        old_q_value = q_r[position[0], position[1], act]
        temporal_difference = reward + (df * np.max(q_r[newPos])) - old_q_value

        new_q_value = old_q_value + (lr * temporal_difference)
        q_r[position[0], position[1], act] = new_q_value
        position = newPos
    while fourRoomsObject.getPackagesRemaining() > 1:
        if isTerminal:
            break
        act = get_next_action(q_g, fourRoomsObject)
        print(act)
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObject.takeAction(act)
        print(aTypes[act], "ACTION:")
        print("Package Type: ", gTypes[gridType])
        print("Packages remaing: ", packagesRemaining)
        if gridType == 2:
            reward = 100
        elif gridType > 0:
            reward = -10000
        else:
            reward = -100
        old_q_value = q_g[position[0], position[1], act]
        temporal_difference = reward + (df * np.max(q_g[newPos])) - old_q_value
        # update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (lr * temporal_difference)
        q_g[position[0], position[1], act] = new_q_value
        position = newPos
    while fourRoomsObject.getPackagesRemaining() > 0:
        if isTerminal:
            break
        act = get_next_action(q_b, fourRoomsObject)
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObject.takeAction(act)
        print("Agent took {0} action and moved to {1} of type {2}. Packages Remaining : {3}".format(aTypes[act], newPos,
                                                                                                    gTypes[gridType],
                                                                                                    packagesRemaining))
        if gridType == 3:
            reward = 100
        elif gridType > 0:
            reward = -10000
        else:
            reward = -100
        old_q_value = q_b[position[0], position[1], act]
        temporal_difference = reward + (df * np.max(q_b[newPos])) - old_q_value
        # update the Q-value for the previous state and action pair
        new_q_value = old_q_value + (lr * temporal_difference)
        q_b[position[0], position[1], act] = new_q_value
        position = newPos
    return fourRoomsObject;

def main():
    global epoch

    fourRoomsObj = FourRooms('rgb')
    for epoch in range(800):
        print("Epoch =", epoch)
        print("____________________\n")
        fourRoomsObj = train(fourRoomsObj)
    global ep
    ep = 1
    for ep in range(500):
        print("Epoch =", ep)
        print("____________________\n")
        fourRoomsObj = train(fourRoomsObj)

    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()



