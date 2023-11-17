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
    
    for i in turkeyDict:
        print(turkeyDict)
    return turkeyDict

def turkeyRace(turkeyDict):
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
        if randint(1,10) in range(6,10):
            for i in turkeyDict:
                pass
                

        else:
            for i in turkeyDict:
                pass
        break



while True:
    turkeyNum = int(input("How many turkeys will participate in the race? "))
    turkeyDict = turkeyGen(turkeyNum)
    turkeyRace(turkeyDict)

