# Artifial Bee Colony Algorithm
import random
import numpy as np
import matplotlib.pyplot as plt

# Objective Function : Maximize f and Minimize fitness
# 인자 갯수에 따라 함수 조절. 첫번째 인자는 x1, 두번째 인자는 x2.. 이런 식으로. 이때 인자 갯수는 유동적이므로, *args를 사용.
def f(*args):
    x1 = args[0]
    x2 = args[1]
    return -(x1-3)**2-(x2-2)**2 +3*x1*x2

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
        self.LOWER_BOUND = -100
        self.UPPER_BOUND = 100
        self.FOOD_SOURCE_LIST = [] # Food source list
        self.FITNESS_LIST = [] # Fitness list
        self.TRIAL_LIST = [0 for i in range(self.FOOD_SOURCE)]
        self.PROBABILITY_LIST = [] # Probability list
        self.BEST_FITNESS = 0
        self.BEST_FOOD_SOURCE = [] # Best food source list
        self.BEST_FITNESS_LIST = [] # Best fitness list
        self.BEST_FOOD_SOURCE_LIST = [] # Best food source list
    
        for i in range(self.FOOD_SOURCE): # Initialize food source list
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
            # Using Clip to prevent food source from exceeding the boundary
            new_food_source[v] = np.clip(self.FOOD_SOURCE_LIST[k][v] + random.uniform(-1,1)*(self.FOOD_SOURCE_LIST[k][v] - self.FOOD_SOURCE_LIST[random.randint(0,self.FOOD_SOURCE-1)][v]),self.LOWER_BOUND,self.UPPER_BOUND)
                
            new_fitness = fitness(x1 = new_food_source[0],x2 = new_food_source[1])
            if new_fitness < self.FITNESS_LIST[k]:
                self.FOOD_SOURCE_LIST[k] = new_food_source
                self.FITNESS_LIST[k] = new_fitness
                self.TRIAL_LIST[k] = 0
            else:
                self.TRIAL_LIST[k] += 1

    def Calculate_Probability(self):
        # Calculate probability of food source
        for i in range(self.FOOD_SOURCE):
            self.PROBABILITY_LIST.append(self.FITNESS_LIST[i]/sum(self.FITNESS_LIST))

    def Onlooker_Bee(self):
        ''' select random number (r). If r < probability of food source, proceed onlooker bee, if not, select another random number.'''
        for i in range(self.ONLOOKER_BEE): # Updation rule for onlooker bee's number
            # select what source to be updated.
            # At leat 1 food source should be selected
            r = random.uniform(0,1)
            k = 0
            while r > 0:
                r -= self.PROBABILITY_LIST[k]
                k += 1
            k -= 1

            v = random.randint(0,self.DIMENSION-1)
            new_food_source = self.FOOD_SOURCE_LIST[k][:] # Select a random food source
            # Using Clip to prevent food source from exceeding the boundary
            new_food_source[v] = np.clip(self.FOOD_SOURCE_LIST[k][v] + random.uniform(-1,1)*(self.FOOD_SOURCE_LIST[k][v] - self.FOOD_SOURCE_LIST[random.randint(0,self.FOOD_SOURCE-1)][v]),self.LOWER_BOUND,self.UPPER_BOUND)
            new_fitness = fitness(x1 = new_food_source[0],x2 = new_food_source[1])
            if new_fitness < self.FITNESS_LIST[k]:
                self.FOOD_SOURCE_LIST[k] = new_food_source
                self.FITNESS_LIST[k] = new_fitness
                self.TRIAL_LIST[k] = 0
            else:
                self.TRIAL_LIST[k] += 1


    def Scout_Bee(self):
        # Updation rule for scout bee
        # IF trial number of food source > trial limit, then replace food source with new food source
        for i in range(self.SCOUT_BEE):
            for j in range(self.FOOD_SOURCE):
                if self.TRIAL_LIST[j] > self.TRIAL_LIMIT:
                    self.FOOD_SOURCE_LIST[j] = []
                    for k in range(self.DIMENSION): # Initialize food source list
                        self.FOOD_SOURCE_LIST[j].append(random.uniform(self.LOWER_BOUND,self.UPPER_BOUND))
                    self.FITNESS_LIST[j] = fitness(x1 = self.FOOD_SOURCE_LIST[j][0],x2 = self.FOOD_SOURCE_LIST[j][1])
                    self.TRIAL_LIST[j] = 0
    
    def Check_Best_Answer(self):
        # Check best answer
        for i in range(self.FOOD_SOURCE):
            if self.FITNESS_LIST[i] < self.BEST_FITNESS:
                self.BEST_FITNESS = self.FITNESS_LIST[i]
                self.BEST_FOOD_SOURCE = self.FOOD_SOURCE_LIST[i]

    
    def Run(self):
        while True:
            self.Employed_Bee()
            self.Calculate_Probability()
            self.Onlooker_Bee()
            self.Scout_Bee()
            self.Check_Best_Answer()
            print("Count: ",len(self.BEST_FITNESS_LIST), "Best fitness: ",self.BEST_FITNESS, " Best food source: ",self.BEST_FOOD_SOURCE)
            self.BEST_FITNESS_LIST.append(self.BEST_FITNESS)
            self.BEST_FOOD_SOURCE_LIST.append(self.BEST_FOOD_SOURCE)
            if len(self.BEST_FITNESS_LIST) > self.MAX_GENERATION:
                break

    def Print_Result(self):
        print("=========================================")
        print("Best fitness: ",self.BEST_FITNESS)
        print("Best food source: ",self.BEST_FOOD_SOURCE)

if __name__ == "__main__":
    ABC = ARTIFICIAL_BEE_COLONY()
    ABC.Run()
    ABC.Print_Result()
