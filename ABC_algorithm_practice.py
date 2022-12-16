# Artifial Bee Colony Algorithm
import random
import numpy as np
import matplotlib.pyplot as plt

# Objective Function : Maximize f and Minimize fitness
def f(x1,x2):
    return x1**2 - x1*x2 + x2**2 + 2*x1 +4*x2 + 3

def fitness(x1,x2):
    if f(x1,x2)>0:
        return 1/(f(x1,x2)+1)
    else:
        return 1+abs(f(x1,x2))

class ARTIFICIAL_BEE_COLONY:
    def __init__(self):
        self.FOOD_SOURCE = 5
        self.DIMENSION = 2
        self.MAX_GENERATION = 100
        self.EMPLOYED_BEE = 3
        self.ONLOOKER_BEE = 2
        self.SCOUT_BEE = 1
        self.TRIAL_LIMIT = 10
        self.LOWER_BOUND = -5
        self.UPPER_BOUND = 5
        self.FOOD_SOURCE_LIST = []
        self.FITNESS_LIST = []
        self.TRIAL_LIST = []
        self.PROBABILITY_LIST = []
        self.BEST_FITNESS = 0
        self.BEST_FOOD_SOURCE = []
        self.BEST_FITNESS_LIST = []
        self.BEST_FOOD_SOURCE_LIST = []
    
        for i in range(self.FOOD_SOURCE): # Initialize trial list
            food_source = []
            for j in range(self.DIMENSION): # Initialize food source list
                food_source.append(random.uniform(self.LOWER_BOUND,self.UPPER_BOUND))
            self.FOOD_SOURCE_LIST.append(food_source)
            self.FITNESS_LIST.append(fitness(x1 = food_source[0],x2 = food_source[1]))
        self.BEST_FITNESS = min(self.FITNESS_LIST)

    def Employed_Bee(self):
        # Updation rule for employed bee
        for i in range(self.EMPLOYED_BEE):
            k = random.randint(0,self.FOOD_SOURCE-1) # Select a random food source
            v = random.randint(0,self.DIMENSION-1) # Select a random dimension
            new_food_source = self.FOOD_SOURCE_LIST[k][:]
            new_food_source[v] = self.FOOD_SOURCE_LIST[k][v] + random.uniform(-1,1)*(self.FOOD_SOURCE_LIST[k][v] - self.FOOD_SOURCE_LIST[random.randint(0,self.FOOD_SOURCE-1)][v])
            new_fitness = fitness(x1 = new_food_source[0],x2 = new_food_source[1])
            if new_fitness < self.FITNESS_LIST[k]:
                self.FOOD_SOURCE_LIST[k] = new_food_source
                self.FITNESS_LIST[k] = new_fitness
                self.TRIAL_LIST[k] = 0
            else:
                self.TRIAL_LIST[k] += 1

    def Calcuate_Probability(self):
        # Calculate probability of food source
        for i in range(self.FOOD_SOURCE):
            self.PROBABILITY_LIST.append(self.FITNESS_LIST[i]/sum(self.FITNESS_LIST))

    def Onlooker_Bee(self):
        ''' select random number (r). If r < probability of food source, proceed onlooker bee, if not, select another random number.'''
        for i in range(self.ONLOOKER_BEE):
            r = random.uniform(0,1)
            for j in range(self.FOOD_SOURCE):
                if r < self.PROBABILITY_LIST[j]:
                    k = j
                    break
            v = random.randint(0,self.DIMENSION-1)
            new_food_source = self.FOOD_SOURCE_LIST[k][:]
            new_food_source[v] = self.FOOD_SOURCE_LIST[k][v] + random.uniform(-1,1)*(self.FOOD_SOURCE_LIST[k][v] - self.FOOD_SOURCE_LIST[random.randint(0,self.FOOD_SOURCE-1)][v])
            new_fitness = fitness(x1 = new_food_source[0],x2 = new_food_source[1])
            if new_fitness < self.FITNESS_LIST[k]:
                self.FOOD_SOURCE_LIST[k] = new_food_source
                self.FITNESS_LIST[k] = new_fitness
                self.TRIAL_LIST[k] = 0
            else:
                self.TRIAL_LIST[k] += 1

        

    def Check_Trial_Limit(self):
        pass

    def Scout_Bee(self):
        pass

    
    def Run(self):
        while True:
    
            self.Employed_Bee()
            self.Calcuate_Probability()
            self.Onlooker_Bee()
            self.Check_Trial_Limit()
            self.Scout_Bee()
            self.BEST_FITNESS_LIST.append(self.BEST_FITNESS)
            self.BEST_FOOD_SOURCE_LIST.append(self.BEST_FOOD_SOURCE)
            if len(self.BEST_FITNESS_LIST) > self.MAX_GENERATION:
                break

    def Print_Result(self):
        pass

if __name__ == "__main__":
    ABC = ARTIFICIAL_BEE_COLONY()
    ABC.Run()
    ABC.Print_Result()
