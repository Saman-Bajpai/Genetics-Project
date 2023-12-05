# BB Bb bb

#BB x BB
#
#BB BB
#BB BB
#
#BB x Bb
#
#BB BB
#Bb Bb
#
#Bb x Bb
#
#BB Bb
#Bb bb
#
#Bb x bb
#
#Bb Bb
#bb bb
#
#BB x bb
#
#Bb Bb
#Bb Bb
#
#bb x bb
#
#bb bb
#bb bb


import random

#initialize array of (BB), (Bb), (bb), of size populationSize.
#Percent of each adjustable.

#Preferable to use a multiple of 2, we don't want someone to spend an eternity of loneliness :( (if you do use an odd number, they will simply die off without reproducing)
#Note to self: >15000 seems to be the limit. Will investigate why.
populationSize = 1500;
cycles = 13;
BBAll = 1/3;
BbAll = 1/3;
bbAll = 1/3;

population = [];
newPopulation = [];

#Do the inputted amounts equal 100%?
if(BBAll+BbAll+bbAll != 1):
    raise ValueError("Population frequencies do not add up to 100% - please retype!\n\nIf using rational repeating numbers, please type in fraction form, i.e '1/3.'")

#Not pure random, b/c of pseudorandomness inherent in computer programming, I think this process is slightly prejudiced towards bb, but that should be unnoticed for medium-sized populations.
randomSeed = 0;
for i in range(populationSize):
    randomSeed = random.random();
    if(randomSeed <= bbAll):
        population.append("bb");
    elif(randomSeed >= 1-BbAll):
        population.append("Bb");
    else:
        population.append("BB");
        
def populationPrint():
    global population;
    print(population);
    
def tallyPopulation():
    global population, populationSize;
    BB = 0;
    Bb = 0;
    bb = 0;
    for i in population:
        if(i == "bb"):
            bb+=1;
        elif(i == "Bb"):
            Bb+=1;
        elif(i == "BB"):
            BB+=1;
    print("\nBB: " + str(BB) + "(" + str(BB*100/populationSize) + "%) Bb: " +str(Bb) + "(" + str(Bb*100/populationSize) + "%) bb: "+str(bb) + "(" + str(bb*100/populationSize) + "%)");
    print("Dominant: " +str(BB+Bb)+ "(" + str((BB+Bb)*100/populationSize) + "%) Recessive: " + str(bb) + "(" + str(bb*100/populationSize) + "%)");
    return;

#We don't want our species to become the Hapsburgs.
def scramble():
    global population;
    random.shuffle(population);
    
# Preconditions:
# Assume our all our test subjects are split exactly 50/50 into male and female, are monogamous and have 4 kids, each of which embody the 4 possible genetic combinations of the parents.
# So, basically, population doubles each cycle, without previous population values.

def reproduce():
    global population, newPopulation, populationSize;
    scramble();
    #Keeping this repetative just to keep a uniform look.
    for j in range(0, populationSize, 2):
        if(population[j] + population[j+1] == "BBBB"):
            newPopulation.append("BB");
            newPopulation.append("BB");
            newPopulation.append("BB");
            newPopulation.append("BB");
        elif(population[j] + population[j+1] == "BBBb" or population[j] + population[j+1] == "BbBB"):
            newPopulation.append("BB");
            newPopulation.append("BB");
            newPopulation.append("Bb");
            newPopulation.append("Bb");
        elif(population[j] + population[j+1] == "BbBb"):
            newPopulation.append("BB");
            newPopulation.append("Bb");
            newPopulation.append("Bb");
            newPopulation.append("bb");
        elif(population[j] + population[j+1] == "Bbbb" or population[j] + population[j+1] == "bbBb"):
            newPopulation.append("Bb");
            newPopulation.append("Bb");
            newPopulation.append("bb");
            newPopulation.append("bb");
        elif(population[j] + population[j+1] == "BBbb" or population[j] + population[j+1] == "bbBB"):
            newPopulation.append("Bb");
            newPopulation.append("Bb");
            newPopulation.append("Bb");
            newPopulation.append("Bb");
        elif(population[j] + population[j+1] == "bbbb"):
            newPopulation.append("bb");
            newPopulation.append("bb");
            newPopulation.append("bb");
            newPopulation.append("bb");
        else:
            raise ValueError("Somehow you got a combo not found in a punnett square.\n\nCongrats, you created a monster!");

    population = newPopulation;
    newPopulation = [];
    populationSize *= 2;

tallyPopulation()
for i in range(cycles):
    reproduce()
tallyPopulation()
