from FourRooms import FourRooms
import numpy as np
import random

#global variables
aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

global env;
env = [];
#array that is the agents view of the environment

actSeq2 = [];
actSeq1 = [];

alreadyChecked = []

packageArray = [];
optimalPolicy = [[],[],[]]

red_opt = [];
green_opt = [];
blue_opt = [];

def moveAroundPixel(fourRoomsObj, move):
    actSeq = []
    emptyActSeq = []

    if move == FourRooms.UP:
        #if moved up and hit the wrong pixel
        #try and get around it by going left - up - right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.LEFT], newPos, gTypes[gridType]))
        set = FourRooms.RIGHT
        if(newPos==oldPos):
            #if you move left and hit a wall, try and move right
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
            #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.RIGHT], newPos, gTypes[gridType]))
            set = FourRooms.LEFT
            if(newPos==oldPos):
                #if you move right and you also hit a wall, return and continue with traversal
                return emptyActSeq;
            else:
                actSeq.append(aTypes[FourRooms.RIGHT])
        else:
            actSeq.append(aTypes[FourRooms.LEFT]);
        #move up twice if you managed to move left/right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.UP], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.UP])
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.UP], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.UP])
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(set)
        actSeq.append(aTypes[set])
        #go back to just above the pixel
        #update current action sequence
    elif move == FourRooms.DOWN:
        #if moved up and hit the wrong pixel
        #try and get around it by going left - up - right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.LEFT], newPos, gTypes[gridType]))
        set = FourRooms.RIGHT
        if(newPos==oldPos):
            #if you move left and hit a wall, try and move right
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
            #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.RIGHT], newPos, gTypes[gridType]))
            set = FourRooms.LEFT
            if(newPos==oldPos):
                #if you move right and you also hit a wall, return and continue with traversal
                return emptyActSeq;
            else:
                actSeq.append(aTypes[FourRooms.RIGHT])
        else:
            actSeq.append(aTypes[FourRooms.LEFT]);
        #move up twice if you managed to move left/right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.DOWN], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.DOWN])
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.DOWN], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.DOWN])
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(set)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[set], newPos, gTypes[gridType]))
        actSeq.append(aTypes[set])
        #go back to just above the pixel
        #update current action sequence
    elif move == FourRooms.LEFT:
        #if moved up and hit the wrong pixel
        #try and get around it by going left - up - right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.DOWN], newPos, gTypes[gridType]))
        set = FourRooms.UP
        if(newPos==oldPos):
            #if you move left and hit a wall, try and move right
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
            #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.UP], newPos, gTypes[gridType]))
            set = FourRooms.DOWN
            if(newPos==oldPos):
                #if you move right and you also hit a wall, return and continue with traversal
                return emptyActSeq;
            else:
                actSeq.append(aTypes[FourRooms.UP])
        else:
            actSeq.append(aTypes[FourRooms.DOWN]);
        #move up twice if you managed to move left/right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
       # print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.LEFT], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.LEFT])
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.LEFT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.LEFT], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.LEFT])
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(set)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[set], newPos, gTypes[gridType]))
        actSeq.append(aTypes[set])
        #go back to just above the pixel
        #update current action sequence
    elif move == FourRooms.RIGHT:
        #if moved up and hit the wrong pixel
        #try and get around it by going left - up - right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.DOWN)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.DOWN], newPos, gTypes[gridType]))
        set = FourRooms.UP
        if(newPos==oldPos):
            #if you move left and hit a wall, try and move right
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.UP)
            #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.UP], newPos, gTypes[gridType]))
            set = FourRooms.DOWN
            if(newPos==oldPos):
                #if you move right and you also hit a wall, return and continue with traversal
                return emptyActSeq;
            else:
                actSeq.append(aTypes[FourRooms.UP])
        else:
            actSeq.append(aTypes[FourRooms.DOWN]);
        #move up twice if you managed to move left/right
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.RIGHT], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.RIGHT])
        oldPos = fourRoomsObj.getPosition();
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[FourRooms.RIGHT], newPos, gTypes[gridType]))
        if (newPos == oldPos):
            #if one of the upward moves fail, return to traversal
            return emptyActSeq;
        else:
            actSeq.append(aTypes[FourRooms.RIGHT])
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(set)
        actSeq.append(aTypes[set])
        #go back to just above the pixel
        #update current action sequence
    #print("NEW CURRENT ACTION SEQUENCE TO MOVE AROUND PIXEL: ")
    #print(actSeq);
    return actSeq;
    #if none of these work, it means you cant get around the pixel
    #return an empty array and keep going on with act sequence

def checkGrid(num, currentActSeq, newActSeq, fourRoomsObj, motion):
    count = len(packageArray)+1;
    #print("GRID: ", num)
    #print("SEARCHING FOR PIXEL: ", count)
    if (num > count):
        #print("WRONG PIXEL FOUND")
        # if the agent has found the pixel in the wrong order
        # set the action sequence to move around the pixel
        # pop the last move from the action sequence
        # reset the epoch
        prevPos = resetPos(fourRoomsObj);
        #print("AGENT LOCATION RESET")
        # move to the position just before terminal state
        for i in newActSeq:
            currentActSeq.append(i)
        currentActSeq.pop()
        moveToNewPos(fourRoomsObj, currentActSeq);
        # move around the pixel
        prevPos = fourRoomsObj.getPosition();
        # print("RESTARTING FROM ", prevPos, "via the action sequence: ")
        # print(currentActSeq)
        cas = moveAroundPixel(fourRoomsObj, motion)
        newActSeq.append(cas);
        if(num in alreadyChecked):
            n = random.randint(0, 1)
            if(n == 1):
                seq = actSeq2;
            else:
                seq = actSeq1;
            n = random.randint(0, 1)
            if(n==1):
                alreadyChecked.append(num);
                max_row, max_col, env2 = Vertical(fourRoomsObj, fourRoomsObj.getPackagesRemaining(), seq);
                setNewPolicy2(max_row, max_col, seq);
            else:
                alreadyChecked.remove(num);
                max_row, max_col, env1 = Horizontal(fourRoomsObj, fourRoomsObj.getPackagesRemaining(), seq);
                setNewPolicy1(max_row, max_col, seq);
            return
        else:
            alreadyChecked.append(num)
    elif num == count:
        print("CORRECT PACKAGE FOUND!", count)
        packageArray.append(gTypes[count])
        addOptimalPolicy(currentActSeq, newActSeq, count)

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
        fourRoomsObj.showPath(-1)
        if(fourRoomsObj.isTerminal()==False):
            for k in reverseSeq:
                gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(k)
                #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[k], newPos, gTypes[gridType]))
        else:
            fourRoomsObj.showPath(-1, "scenario_1.jpg");

def addOptimalPolicy(actSeq, currentActSeq, count):
    #print("Current Act Seq:", currentActSeq)
    #print("Act Seq:", actSeq)
    i = 0

    if(count == 1):
        actSeq = actSeq[0:len(actSeq)-2]

    for i in range(len(currentActSeq)):
        if (currentActSeq[i] == FourRooms.UP):
            actSeq.append(0)
        if (currentActSeq[i] == FourRooms.DOWN):
            actSeq.append(1)
        if (currentActSeq[i] == FourRooms.LEFT):
            actSeq.append(2)
        if (currentActSeq[i] == FourRooms.RIGHT):
            actSeq.append(3)

    print("ADDING OPTIMAL:")

    if(count==1):
        red_opt = actSeq;
    elif(count==2):
        green_opt = actSeq;
    elif(count==3):
        blue_opt = actSeq;

    actSeq1 = actSeq;
    actSeq2 = actSeq;

    for act in actSeq:
        #print(aTypes[act])
        optimalPolicy[count-1].append(aTypes[act])

    print(optimalPolicy[count-1])
    print("Searching for next optimal policy . . . (this may take a while)")

def right_move(row, cP, pP, fourRoomsObj, actSeq, cas):
    prInitial = fourRoomsObj.getPackagesRemaining();
    pr = 0;
    while (pP != cP):
        gridType, newPos, pr, isTerminal = fourRoomsObj.takeAction(FourRooms.RIGHT)
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[3], newPos, gTypes[gridType]))
        #fourRoomsObj.showPath(-1);
        cas.append(FourRooms.RIGHT)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr<prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.RIGHT)
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
        #fourRoomsObj.showPath(-1);
        cas.append(FourRooms.LEFT)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.LEFT)
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
        #fourRoomsObj.showPath(-1);
        cas.append(FourRooms.UP)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.UP)
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
        #fourRoomsObj.showPath(-1);
        cas.append(FourRooms.DOWN)
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.DOWN)
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
        #cas.append(FourRooms.UP);
        #print("Agent took {0} action and moved to {1} of type {2}".format(aTypes[0], newPos, gTypes[gridType]))
        fourRoomsObj.showPath(-1);
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.UP)
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
        #fourRoomsObj.showPath(-1);
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.DOWN)
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
        #fourRoomsObj.showPath(-1);
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.LEFT)
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
        #fourRoomsObj.showPath(-1);
        if (len(packageArray) == 3):
            displayOptimalPolicy(fourRoomsObj, actSeq, cas)
            exit(1)
        if pr < prInitial:
            checkGrid(gridType, actSeq, cas, fourRoomsObj, FourRooms.RIGHT)
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
    global env;
    max_row = 0;
    max_col = 0;

    # Create FourRooms Object
    fourRoomsObj = FourRooms('rgb')

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()));

    startPack = fourRoomsObj.getPackagesRemaining();
    p = startPack;
    # Optimal policies

    while(p!=(startPack-3)):
        env1 = [];
        #print("H1")
        max_row, max_col, env1 = Horizontal(fourRoomsObj, p, actSeq2);
        setNewPolicy1(max_row, max_col, actSeq2);
        #sets the act sequence for the first horizontal traversal

        env3 = [];
        #print("V2")
        max_row, max_col, env3 = Vertical(fourRoomsObj, p, actSeq2);
        setNewPolicy2(max_row, max_col, actSeq2);
        # sets the appends to act sequence for second vertical traversal

        prevPos = resetPos(fourRoomsObj);
        currPos = fourRoomsObj.getPosition();

        env2 = [];
        #print("V1")
        max_row, max_col, env2 = Vertical(fourRoomsObj, p, actSeq1);
        setNewPolicy2(max_row, max_col, actSeq1);
        # sets the act sequence for the first vertical traversal

        #print("H2")
        max_row, max_col, env4 = Horizontal(fourRoomsObj, p, actSeq1);
        setNewPolicy1(max_row, max_col, actSeq1);


if __name__ == "__main__":
    main()
