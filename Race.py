from random import randint
'''
class turkey:
    def __init__(self,spd,agi,int,chance):
        self.spd = spd
        self.agi = agi
        self.int = int
        self.chance = chance

    def randStats(self):
        self.spd = randint(1,10)
        self.agi = randint(1,10)
        self.int = randint(1,10)


turkey1 = turkey(0,0,0,0)
turkey1.randStats()
'''



## Generates all of the turkeys for the race with randomized stats
## Might add a system that calculates their odds of winning later
## Might also add randomized names.
def turkeyGen(turkeyNum):
    turkeyDict = {

    }

    for i in range(turkeyNum):

        ## Holds the values for creating the turkey.
        tempList = []

        '''
        Generates 3 values for each turkey, speed, agility, and intelligence.
        Speed is obvious, agility determines chance to dodge, and
        intelligence determines chance to beat obstacles.
        A fourth value is added for the distance the turkey is.
        '''
        for j in range(3):
            tempList.append(randint(1,10))
        tempList.append(1000)

        turkeyDict.update({str("Turkey " + str(i + 1)): list(tempList)})
        tempList.clear()
    

    print(turkeyDict)
    return turkeyDict

def turkeyRace(turkeyDict):

    print("Let the race begin!")

    '''
    The obstacles dictionary contains different obstacles for use in the race.
    Each obstacle has 2 values, the attribute it uses, 2 for agility, 3 for 
    intelligence, and how high that skill needs to be for a penalty
    to be avoided.
    '''
    obstacles = {
        "Logs": [3,3],
        "Mud": [3,5],
        "Hoops": [2,3],
        "Boulder": [2,5],
    }

    while True:
        ## Determines whether or not there will be an obstacle.
        isObstacle = randint(1,5)
        if isObstacle == 5:
            isObstacle = False

        ## Check the IsObstacle variable for a "False" value.
        if not isObstacle:
            print("No obstacle on this stretch!")
            for i in turkeyDict:
                turkeyDict[i][3] -= turkeyDict[i][0] * 15
        ## If the isObstacle variable is not False, runs this code
        else:
            ## A disgusting way to iterate, but it works. I think.
            for i in turkeyDict:
                if turkeyDict[i][obstacles[isObstacle][0]] <= obstacles[isObstacle][1]:
                    turkeyDict[i][3] -= turkeyDict[i][0] * 5
                else:
                    turkeyDict[i][3] -= turkeyDict[i][0] * 10
        ## Checks to see if the user wants to continue the race, also acts as a way to stop an infinite loop from happening.
        while True:
            choice = input("Would you like to continue this race? (Y/N) ")
            if choice == "Y" or choice == "N":
                break
            else:
                print("Must be Y (Yes) or N (No)")

        ## Checks if a turkey's distance value has reached 0, meaning they've won.
        for i in turkeyDict:
            if turkeyDict[i][3] <= 0:
                print("The race is over! ")
                break



while True:
    turkeyNum = int(input("How many turkeys will participate in the race? "))
    turkeyDict = turkeyGen(turkeyNum)
    turkeyRace(turkeyDict)

    while True:
        choice = input("Would you like to race again? (Y/N) ")
        if choice == "Y" or "N":
            break
        else:
            print("Must be Y (Yes) or N (No)")
    
    if choice == "Y":
        continue
    elif choice == "N":
        break
        

