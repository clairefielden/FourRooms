from FourRooms import FourRooms
import numpy as np
import sys

#global variables
aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

global env;
env = [];
#array that is the agents view of the environment

packageArray = [];
optimalPolicy = [[],[],[]]

def displayOptimalPolicy(fourRoomsObj, actSeq, currentActSeq):
    fourRoomsObj.newEpoch()
    isTerminal = False;
    print("\nOPTIMAL POLICY:")
    for i in range(3):
        actSeq = optimalPolicy[i]
        reverseSeq = [];
        for j in range(len(actSeq)):
            if actSeq[j] == aTypes[0] and isTerminal==False:
                currPos = fourRoomsObj.getPosition();
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
                if(newPos!=currPos):
                    reverseSeq.insert(0, FourRooms.DOWN)
                print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[0], newPos, gTypes[gridType]))
            elif actSeq[j] == aTypes[1] and isTerminal==False:
                currPos = fourRoomsObj.getPosition();
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
                if(newPos!=currPos):
                    reverseSeq.insert(0, FourRooms.UP)
                print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[1], newPos, gTypes[gridType]))
            elif actSeq[j] == aTypes[2] and isTerminal==False:
                currPos=fourRoomsObj.getPosition();
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
                if(newPos!=currPos):
                    reverseSeq.insert(0, FourRooms.RIGHT)
                print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[2], newPos, gTypes[gridType]))
            elif actSeq[j] == aTypes[3] and isTerminal==False:
                currPos = fourRoomsObj.getPosition();
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
                if(newPos!=currPos):
                    reverseSeq.insert(0, FourRooms.LEFT)
                print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[3], newPos, gTypes[gridType]))
        if(fourRoomsObj.isTerminal()==False):
            for k in reverseSeq:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(k)
                #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[k], newPos, gTypes[gridType]))

    fourRoomsObj.showPath(-1);
    fourRoomsObj.showPath(-1, "scenario_2.jpg");

def addOptimalPolicy(actSeq, currentActSeq):
    #print("Current Act Seq:", currentActSeq)
    #print("Act Seq:", actSeq)

    i = 0
    for i in range(len(currentActSeq)):
        if (currentActSeq[i] == FourRooms.UP):
            actSeq.append(0)
        if (currentActSeq[i] == FourRooms.DOWN):
            actSeq.append(1)
        if (currentActSeq[i] == FourRooms.LEFT):
            actSeq.append(2)
        if (currentActSeq[i] == FourRooms.RIGHT):
            actSeq.append(3)

    index = len(packageArray)-1
    #print("ADDING OPTIMAL:")

    for act in actSeq:
        #print(aTypes[act])
        optimalPolicy[index].append(aTypes[act])

def right_move(row, cP, pP, fourRoomsObj, actSeq, cas):
    prInitial = fourRoomsObj.getPackagesRemaining();
    pr = 0;
    while (pP != cP):
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[3], newPos, gTypes[gridType]))
        cas.append(FourRooms.RIGHT)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr<prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        if(isTerminal==True):
            fourRoomsObj.newEpoch()
            break;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
        # insert the new block at the end of the row
        row.insert(len(row), 0);
    return row, pr;

def left_move(row, cP, pP, fourRoomsObj, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    while (pP != cP):
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[2], newPos, gTypes[gridType]))
        cas.append(FourRooms.LEFT)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
        # insert the new block at the beginning of the row
        row.insert(0, 0);
    return row, pr;

def up_move(column, fourRoomsObj, pP, cP, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining()
    gridType = 0
    newPos = fourRoomsObj.getPosition()
    isTerminal = fourRoomsObj.isTerminal()
    for y in range(column):
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[0], newPos, gTypes[gridType]))
        cas.append(FourRooms.UP)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
    return cP, pP, pr;

def down_move(column, fourRoomsObj, pP, cP, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    isTerminal = fourRoomsObj.isTerminal();
    for y in range(column):
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[1], newPos, gTypes[gridType]))
        cas.append(FourRooms.DOWN)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
    return cP, pP, pr;

def up_move_2(col, cP, pP, fourRoomsObj, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    while (pP != cP):
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
        cas.append(FourRooms.UP);
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[0], newPos, gTypes[gridType]))
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if (gTypes[gridType] in packageArray or gridType == 0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
        # insert the new block at the beginning of the row
        col.insert(0, [0]);
    return col, pr;

def down_move_2(col, cP, pP, fourRoomsObj, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    while (pP != cP):
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        cas.append(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[1], newPos, gTypes[gridType]))
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
        # insert the new block at the end of the col
        col.insert(len(col), [0]);
    return col, pr;

def left_move_2(row, fourRoomsObj, pP, cP, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    isTerminal = fourRoomsObj.isTerminal();
    for x in range(row):
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
        cas.append(FourRooms.LEFT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[2], newPos, gTypes[gridType]))
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
    return cP, pP, pr;

def right_move_2(row, fourRoomsObj, pP, cP, actSeq, cas):
    pr = 0;
    prInitial = fourRoomsObj.getPackagesRemaining();
    isTerminal = fourRoomsObj.isTerminal();
    for x in range(row):
        if (isTerminal == True):
            fourRoomsObj.newEpoch()
            break;
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
        cas.append(FourRooms.RIGHT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[3], newPos, gTypes[gridType]))
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            if(gTypes[gridType] in packageArray or gridType==0):
                pass;
            else:
                print("Package found :", gTypes[gridType], "at: ", newPos)
                packageArray.append(gTypes[gridType])
                addOptimalPolicy(actSeq, cas)
                fourRoomsObj.newEpoch()
                break;
            prInitial = pr;
        pP = cP;
        cP = newPos;
        if cP == pP:
            break;
    return cP, pP, pr;

def resetPos(fourRoomsObj):
    fourRoomsObj.newEpoch();
    return -1;

def moveToNewPos(fourRoomsObj, actSeq):
    #print(actSeq)
    for act in actSeq:
        if (fourRoomsObj.isTerminal() == True):
            fourRoomsObj.newEpoch()
            break;
        else:
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act);

def setNewPolicy1(max_r, max_c, actSeq):
    #print("Max Column: ", max_c, "Max Row: ", max_r);
    if (max_c < 0):
        for y in range(max_c * -1):
            actSeq.append(FourRooms.DOWN);
    else:
        for y in range(max_c):
            actSeq.append(FourRooms.UP);
    if (max_r < 0):
        for y in range(max_r * -1):
            actSeq.append(FourRooms.LEFT);
    else:
        for y in range(max_r):
            actSeq.append(FourRooms.RIGHT);

def setNewPolicy2(max_r, max_c, actSeq):
    #print("Max Column: ", max_c, "Max Row: ", max_r);
    if (max_r < 0):
        for y in range(max_r * -1):
            actSeq.append(FourRooms.LEFT);
    else:
        for y in range(max_r):
            actSeq.append(FourRooms.RIGHT);
    if (max_c < 0):
        for y in range(max_c * -1):
            actSeq.append(FourRooms.DOWN);
    else:
        for y in range(max_c):
            actSeq.append(FourRooms.UP);

def Horizontal(fourRoomsObj, p, actSeq):
    global env;
    if (len(actSeq) != 0):
        moveToNewPos(fourRoomsObj, actSeq);
    # set positions
    prevPos = -1;
    currPos = fourRoomsObj.getPosition();

    #set the max columns and rows
    max_c = 0;
    max_r = 0;

    #set the counts
    column = 0;
    row_count = 0;

    # start at y = 0 and move up
    # skip the first UP move
    # move up continuously until you hit a wall
    while (prevPos != currPos):
        row = [0];
        # at y = 0
        # left while there is no wall
        currentActSeq = [];
        for i in range(column):
            currentActSeq.append(FourRooms.UP)
        row, p = left_move(row, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);

        row_count = (len(row))-1;
        if (row_count > abs(max_r)):
            max_r = row_count * -1;
            max_c = column;
            #print("New max: ", max_r, "at column ", max_c);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        currPos, prevPos, p = up_move(column, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        currentActSeq = [];
        for i in range(column):
            currentActSeq.append(FourRooms.UP)

        # right while there is no wall
        row, p = right_move(row, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);

        row_count = len(row)- row_count;
        if (row_count-1 > abs(max_r)):
            max_r = row_count-1;
            max_c = column;
            #print("New max: ", max_r, "at column ", max_c);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        # insert the row at the beginning of the environment
        env.insert(0, row);

        column = column + 1;
        # move up the number of columns in the count
        currentActSeq = [];
        currPos, prevPos, p = up_move(column, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        currentActSeq = [];
        # now continue scanning rows

    # reset positions
    prevPos = resetPos(fourRoomsObj);
    if (len(actSeq) != 0):
        moveToNewPos(fourRoomsObj, actSeq);
    currPos = fourRoomsObj.getPosition();

    # start at y = -1 and move down
    column = 1;
    row_count = 0;
    currentActSeq = [];
    # traversing -y
    currPos, prevPos, p = down_move(column, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
    currentActSeq = [];
    while (prevPos != currPos):
        row = [0];
        # at y = -1
        # left while there is no wall
        currentActSeq = [];
        for i in range(column):
            currentActSeq.append(FourRooms.DOWN)
        row, p = left_move(row, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];
        row_count = (len(row))-1;

        if (row_count-1 > abs(max_r)):
            max_r = (row_count-1) * -1;
            max_c = column * -1;
            #print("New max: ", max_r, "at column ", max_c);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        currPos, prevPos, p = down_move(column, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        # right while there is no wall
        currentActSeq = [];
        for i in range(column):
            currentActSeq.append(FourRooms.DOWN)
        row, p = right_move(row, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];
        row_count = len(row) - row_count;
        if (row_count-1 > abs(max_r)):
            max_r = row_count-1;
            max_c = column * -1;
            #print("New max: ", max_r, "at column ", max_c);

        # add the row to the end of the environment
        env.insert(len(env), row);

        # increment the columns and keep moving downwards
        column = column + 1;
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        currPos, prevPos, p = down_move(column, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        currentActSeq = [];

    return max_r, max_c, env;

def Vertical(fourRoomsObj, p, actSeq):
    if(len(actSeq)!=0):
        moveToNewPos(fourRoomsObj, actSeq);
    env = [];
    # set positions
    prevPos = -1;
    currPos = fourRoomsObj.getPosition();

    #set the max columns and rows
    max_c = 0;
    max_r = 0;

    #set the counts
    row = 0;
    col_count = 0;

    # start at x = 0 and move up
    # skip the first LEFT move
    # LEFT continuously until you hit a wall
    while (prevPos != currPos):
        col = [[0]];
        # at x = 0
        # up while there is no wall
        currentActSeq = [];
        for i in range(row):
            currentActSeq.append(FourRooms.LEFT)
        col, p = up_move_2(col, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];

        col_count = (len(col))-1;
        if (col_count > abs(max_c)):
            max_c = col_count;
            max_r = row*-1;
            #print("New max: Column", max_c, "at row ", max_r);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        #after reset, must go left until we are back
        currPos, prevPos, p = left_move_2(row, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        currentActSeq = [];

        # down while there is no wall
        currentActSeq = [];
        for i in range(row):
            currentActSeq.append(FourRooms.LEFT)
        col, p = down_move_2(col, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];

        col_count = ((len(col))-1) - col_count;
        if (col_count > abs(max_c)):
            max_c = (col_count)*-1;
            max_r = row*-1;
            #print("New max: Column", max_c, "at column ", max_r);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        # insert the col at the beginning of the environment
        env.insert(0, col);

        row = row + 1;
        currentActSeq = [];
        # move left the number of rows in the count
        currPos, prevPos, p = left_move_2(row, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        # now continue scanning columns
        currentActSeq = [];

    # reset positions
    prevPos = resetPos(fourRoomsObj);
    if (len(actSeq) != 0):
        moveToNewPos(fourRoomsObj, actSeq);
    currPos = fourRoomsObj.getPosition();

    # start at x = 1 and move down
    row = 1;
    col_count = 0;

    currentActSeq = [];
    # traversing +x
    currPos, prevPos, p = right_move_2(row, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
    currentActSeq = [];
    while (prevPos != currPos):
        col = [[0]];
        # at x=1
        # up while there is no wall
        currentActSeq = [];
        for i in range(row):
            currentActSeq.append(FourRooms.RIGHT)
        col, p = up_move_2(col, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];

        col_count = (len(col))-1;

        if (col_count > abs(max_c)):
            max_c = col_count;
            max_r = row;
            #print("New max: column", max_c, "at row ", max_r);

        # reset positions
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        currPos, prevPos, p = right_move_2(row, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        # down while there is no wall

        currentActSeq = [];
        for i in range(row):
            currentActSeq.append(FourRooms.RIGHT)
        col, p = down_move_2(col, currPos, prevPos, fourRoomsObj, actSeq, currentActSeq);
        currentActSeq = [];

        col_count = ((len(col))-1) - col_count;
        if (col_count > abs(max_c)):
            max_c = col_count*-1;
            max_r = row;
            #print("New max: column", max_c, "at row ", max_r);

        # add the col to the end of the environment
        env.insert(len(env), col);

        # increment the rows and keep scanning vertically
        row = row + 1;
        prevPos = resetPos(fourRoomsObj);
        if (len(actSeq) != 0):
            moveToNewPos(fourRoomsObj, actSeq);
        currPos = fourRoomsObj.getPosition();

        currentActSeq = [];
        currPos, prevPos, p = right_move_2(row, fourRoomsObj, prevPos, currPos, actSeq, currentActSeq);
        currentActSeq = [];
    return max_r, max_c, env;

def main():
    print(sys.argv[0])
    if(len(sys.argv)>1):
        stochastic = True;
    else:
        stochastic = False;

    global env;
    max_row = 0;
    max_col = 0;

    # Create FourRooms Object
    fourRoomsObj = FourRooms('multi', stochastic)


    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()));

    startPack = fourRoomsObj.getPackagesRemaining();
    p = startPack;
    # Optimal policies

    actSeq1 = []
    actSeq2 = []

    while(p!=(startPack-3)):
        env1 = [];
        #print("H1")
        max_row, max_col, env1 = Horizontal(fourRoomsObj, p, actSeq2);
        setNewPolicy1(max_row, max_col, actSeq2);
        #sets the act sequence for the first horizontal traversal

        prevPos = resetPos(fourRoomsObj);
        currPos = fourRoomsObj.getPosition();

        env2 = [];
        #print("V1")
        max_row, max_col, env2 = Vertical(fourRoomsObj, p, actSeq1);
        setNewPolicy2(max_row, max_col, actSeq1);
        # sets the act sequence for the first vertical traversal

        env3 = [];
        #print("V2")
        max_row, max_col, env3 = Vertical(fourRoomsObj, p, actSeq2);
        setNewPolicy2(max_row, max_col, actSeq2);
        # sets the appends to act sequence for second vertical traversal

        #print("H2")
        max_row, max_col, env4 = Horizontal(fourRoomsObj, p, actSeq2);
        setNewPolicy1(max_row, max_col, actSeq1);

if __name__ == "__main__":
    main()
