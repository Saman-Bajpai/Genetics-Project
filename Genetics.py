"""
Topics from class covered: Genetic drift, habitat fragmentation, and the downside of zoos.

  Genetic diversity is perhaps one of the most important driving forces behind life itself, as it pushes evolution forward and leads to the different traits exhibited by the flora and fauna we love so much (that includes us)! Even on a smaller scale, genetic diversity is essential in improving the resilience of a species. A tiny population will quickly become homogenous, as most of the members share a high percentage of DNA with potential partners. A small homogenous population suffers many potential threats, including:
- The spread of damaged alleles becoming pervasive.
- Mutations not happening often enough or quick enough to force evolution.
- The chance disappearance of traits as they fail to pass on to offspring.
  Small homogenous populations are especially vulnerable during genetic drift events, which are any worldly phenomena that cause a dramatic shift in genetic diversity. A simple example is an earthquake that kills 20% of the population. If your population is in the thousands, then it’s likely it will bounce back in a few cycles. However, if the population is only 10, then there’s a high chance that the only 2 carriers of a potential trait will be killed off, removing that trait from the species forever.
  Unfortunately, this is a common threat to the overall biodiversity of our planet. Habitat fragmentation leads to an otherwise large population being split up into much smaller populations, which are at an increased risk for genetic drift events. This is also one of the biggest downsides to zoos; even if we are successfully able to have a species reproduce a few cycles, they may still be vulnerable to disease and loss of traits that differentiate them from each other. Because of this, many animals are as good as extinct once their population reaches a low enough threshold.
  A trait can recover quickly in a large population, or through steady spread over many reproduction cycles. Although there may not be many in a species that exhibit a recessive trait, they can still be carriers and pass it onto their descendants. The purpose of this project is to showcase how having too small a population can lead to loss in biodiversity.
"""

#Punnett Square possibilities
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

import math
import random
import os

#initialize array of (BB), (Bb), (bb), of size populationSize.
#Percent of each adjustable.

#Preferable to use a multiple of 2, we don't want someone to spend an eternity of loneliness :( (if you do use an odd number, they will simply die off without reproducing)

# - - - - - - - - - - - - - - - SETUP  - - - - - - - - - - - - - - - #
initialPopulationSize = 16
BBAll = 1 / 3
BbAll = 1 / 3
bbAll = 1 / 3

population = []
newPopulation = []


# - - - - - - - - - - - - - - - CORE FUNCTIONS  - - - - - - - - - - - - - - - #
def populationPrint():
  global population
  print(population)


def tallyPopulation():
  global population
  if (len(population) == 0):
    print("Population went extinct! :(")
    return
  BB = 0
  Bb = 0
  bb = 0
  for i in population:
    if (i == "bb"):
      bb += 1
    elif (i == "Bb"):
      Bb += 1
    elif (i == "BB"):
      BB += 1
  return [BB, Bb, bb]


def printPopulation(tally):
  BB = tally[0]
  Bb = tally[1]
  bb = tally[2]
  print("\nBB: " + str(BB) + "(" + str(round(BB * 100 / len(population), 2)) +
        "%) Bb: " + str(Bb) + "(" + str(round(Bb * 100 / len(population), 2)) +
        "%) bb: " + str(bb) + "(" + str(round(bb * 100 / len(population), 2)) +
        "%)")
  print("Dominant: " + str(BB + Bb) + "(" +
        str(round((BB + Bb) * 100 / len(population), 2)) + "%) Recessive: " +
        str(bb) + "(" + str(round(bb * 100 / len(population), 2)) + "%)")


#We don't want our species to turn out like the Hapsburgs; However, since it is a random scramble, there is still a chance that we end up recreating Game of Thrones anyways.
def scramble(pop):
  random.shuffle(pop)


# Preconditions:
# Assume our all our test subjects are split exactly 50/50 into male and female, are monogamous and have 4 kids in their lifetime, each of which embody the 4 possible genetic combinations of the parents.
# So, basically, population doubles each cycle, without previous population values.
def reproduce(buff=None):
  global population, newPopulation
  if (len(population) < 2):
    print("Population went extinct! :(")
    exit()
  scramble(population)
  #The odd one out doesn't get to reproduce. :(
  if (len(population) % 2 == 1):
    population.pop()
  #Could shorten it by using for loops, but I'm purposely keeping this repetative so we know what's going on underneath the hood.
  for j in range(0, len(population), 2):
    if (population[j] + population[j + 1] == "BBBB"):
      newPopulation.append("BB")
      newPopulation.append("BB")
      newPopulation.append("BB")
      newPopulation.append("BB")
      if (buff == "D" or buff == "B"):
        newPopulation.append("BB")
        newPopulation.append("BB")
        newPopulation.append("BB")
        newPopulation.append("BB")
    elif (population[j] + population[j + 1] == "BBBb"
          or population[j] + population[j + 1] == "BbBB"):
      newPopulation.append("BB")
      newPopulation.append("BB")
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      if (buff == "D" or buff == "B"):
        newPopulation.append("BB")
        newPopulation.append("BB")
        newPopulation.append("Bb")
        newPopulation.append("Bb")
    elif (population[j] + population[j + 1] == "BbBb"):
      newPopulation.append("BB")
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      newPopulation.append("bb")
      if (buff == "D" or buff == "B"):
        newPopulation.append("BB")
        newPopulation.append("Bb")
        newPopulation.append("Bb")
        newPopulation.append("bb")
    elif (population[j] + population[j + 1] == "Bbbb"
          or population[j] + population[j + 1] == "bbBb"):
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      newPopulation.append("bb")
      newPopulation.append("bb")
      if (buff == "B"):
        newPopulation.append("Bb")
        newPopulation.append("Bb")
        newPopulation.append("bb")
        newPopulation.append("bb")
    elif (population[j] + population[j + 1] == "BBbb"
          or population[j] + population[j + 1] == "bbBB"):
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      newPopulation.append("Bb")
      if (buff == "B"):
        newPopulation.append("Bb")
        newPopulation.append("Bb")
        newPopulation.append("Bb")
        newPopulation.append("Bb")
    elif (population[j] + population[j + 1] == "bbbb"):
      newPopulation.append("bb")
      newPopulation.append("bb")
      newPopulation.append("bb")
      newPopulation.append("bb")
      if (buff == "R" or buff == "B"):
        newPopulation.append("bb")
        newPopulation.append("bb")
        newPopulation.append("bb")
        newPopulation.append("bb")
    else:
      raise ValueError(
          "Somehow we got a combo not found on this punnett square.\n\nCongrats, we created a monster! I'm going to terminate the program before things get out of hand..."
      )

  population = newPopulation
  newPopulation = []


# - - - - - - - - - - - - - - - EVENTS  - - - - - - - - - - - - - - - #
#
#Percent reaching adulthood(reproducing age): 100 = 2x pop growth, 50 = no growth, 25 = 2x decline
#This is due to predators, starvation, etc. Just part of life.
#
#Disaster: deletes % of population
#   Sole survivor: only 1 specimen keeps recessive gene
#
#Extinction event: Reduces population to 10 lucky survivors
#
#
#More babies!:
#Selective 1: if both parents exhibit recessive traits, they reproduce twice (bool = true)
#Selective 2: if both parents exhibit dominant traits, they reproduce twice (bool = false)
#


def extinction(pop):
  if (len(population) < 10):
    print("Population is already below 10, stop bullying them :(")
    return
  for i in range(0, len(population) - 10):
    population.pop()


def indiscriminateKiller(pop, percent):
  if (percent > 100 or percent < 0):
    print("Please enter a percentage between 0-100. Preferably not 0 or 100.")
    return
  if (len(population) == 0):
    print("Population went extinct! :(")
    return

  scramble(population)
  for i in range(0, math.floor(pop * (percent / 100))):
    population.pop()


def genocide(pop, type, percent):
  if (percent > 100 or percent < 0):
    print("Please enter a percentage between 0-100. Preferably not 0 or 100.")
    return
  if (len(population) == 0):
    print("Population went extinct! :(")
    return
  for i in range(0, math.floor(population.count(type) * percent / 100)):
    population.remove(type)


# - - - - - - - - - - - - - - - INITIALIZE  - - - - - - - - - - - - - - - #
def takeValues():
  global initialPopulationSize, BBAll, BbAll, bbAll
  print("Enter population size:(Recommended: 10-100) (Press 2 to skip)\n\n")
  initialPopula
  tionSize = int(input())
  if (initialPopulationSize < 2 or initialPopulationSize > 1000):
    initialPopulationSize = 16
  print(
      "\nEnter percentage starting with BB? (i.e 1/3, 0.25)(Default 1/3) (Press 1 to skip)\n\n"
  )
  BBAll = float(eval(input()))
  if (BBAll == 2):
    BBAll = 1 / 3
  print(
      "\nEnter percentage starting with Bb? (i.e 1/3, 0.25)(Default 1/3) (Press 2 to skip)\n\n"
  )
  BbAll = float(eval(input()))
  if (BbAll == 2):
    BbAll = 1 / 3
  print(
      "\nEnter percentage starting with bb? (i.e 1/3, 0.25)(Default 1/3) (Press 2 to skip)\n\n"
  )
  bbAll = float(eval(input()))
  if (bbAll == 2):
    bbAll = 1 / 3


#Do the inputted amounts equal 100%?
def initialize():
  global initialPopulationSize, BBAll, BbAll, bbAll
  if (BBAll + BbAll + bbAll != 1):
    print(
        "Population frequencies do not add up to 100% - please retype!\n\nIf using rational repeating numbers, please type in fraction form, i.e '1/3.'"
    )
    takeValues()
  #I don't think I have to check for <100 because the other two numbers would violate at least one of these two conditions.
  if (BBAll < 0 or BbAll < 0 or bbAll < 0):
    print("Very funny. Please put in positive percentages.")
    takeValues()
  #Initializer
  #Not pure random, b/c of pseudorandomness inherent in computer programming, I think this process is slightly prejudiced towards bb, but that should be unnoticed for medium-sized populations.
  randomSeed = 0
  for i in range(initialPopulationSize):
    randomSeed = random.random()
    if (randomSeed <= bbAll):
      population.append("bb")
    elif (randomSeed >= 1 - BbAll):
      population.append("Bb")
    else:
      population.append("BB")


# - - - - - - - - - - - - - - - UI  - - - - - - - - - - - - - - - #
#Note that 15-35 percent of your species fails to make it to adulthood.
os.system('cls' if os.name == 'nt' else 'clear')
print(
    "\n~~The Importance of Population Size in Genetic Diversity~~\n\n\n\nWelcome! This simple text-based terminal simulation offers a variety of tools for you to toy with the genetic distribution of a population.\nThe goal of this project is to show how small, homogenous populations are at an increased risk for losing traits compared to large, heterogenous populations.\n\nINSTRUCTIONS:\nYou will choose a population size to start with. Every season, you can choose to perform an action. The game lasts until your species either goes extinct or the population exceeds 1,000.\n\nTo select options, press the number associated with the option, followed by the [ENTER] key.\n\nPress [ENTER] to start.\n\n"
)
startInput = input()
os.system('cls' if os.name == 'nt' else 'clear')
takeValues()
initialize()
done = False
# - - - - - - - - - - - - - - - GAME  - - - - - - - - - - - - - - - #

os.system('cls' if os.name == 'nt' else 'clear')
Ask = ""
while (not done):
  print(
      "Your species makes it through the winter, and in the spring reproduces.\n"
  )
  if (Ask == str(1)):
    print("Nothing extraordinary happened this season.")
    reproduce()
  elif (Ask == str(2)):
    print(
        "After a company stripped the area of its natural resources, only 10 members of the species remain."
    )
    extinction(population)
  elif (Ask == str(3)):
    print(
        "After a damaging series of wildfires, 40% of the population has been decreased."
    )
    reproduce()
    indiscriminateKiller(len(population), 40)
  elif (Ask == str(4)):
    print(
        "After a damaging tsunami, 75% of the population has been decreased.")
    indiscriminateKiller(len(population), 75)
    reproduce()
  elif (Ask == str(5)):
    print(
        "This season brought good rain and soil. The number of children your species has this season doubles!"
    )
    reproduce("B")
  elif (Ask == str(6)):
    print(
        "Due to subtle changes in the environment, the dominant trait in your species has allowed certain couples to gather more resources and therefore produce more children."
    )
    reproduce("D")
  elif (Ask == str(7)):
    print(
        "Due to subtle changes in the environment, the recessive trait in your species has allowed certain couples to gather more resources and therefore produce more children."
    )
    reproduce("R")
  elif (Ask == str(8)):
    print(
        "Predators find it easier to find and capture prey with dominant traits. Members with BB or Bb alleles are 50% more likely to be eaten."
    )
    reproduce()
    genocide(population, "BB", 50)
    genocide(population, "Bb", 50)
  elif (Ask == str(9)):
    print(
        "Disease breaks out, and members with a bb allele are 50% more susceptible to developing complecations leading to death."
    )
    reproduce()
    genocide(population, "bb", 50)
  elif (Ask == str(0)):
    reproduce()
    print("Game has ended.")
    done = True
  printPopulation(tallyPopulation())
  print("\n\nPopulation: " + str(len(population)) + "\n\n")

  if (len(population) > 1000):
    done = True
  if (not done):
    print(
        "What event would you next like to inflict upon your species?\n\n1 Nothing\n2 Near-extinction event\n3 Wildfire\n4 Tsunami\n5 Year of plenty\n6 Dominance pays off\n7 Recessiveness pays off\n8 Bright colors make easy targets\n9 Disease resistance\n0 End game"
    )
    Ask = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    indiscriminateKiller(len(population), random.random() * 20 + 15)

if (len(population) < 2):
  print(
      "Let alone their traits, your species has gone extinct in its entirety. Please rerun the program if you would like to seek a different ending.\n\nEXTINCTION ENDING"
  )
  exit()
if (len(population) > 1000):
  print(
      "Your species is flourishing well. There is no longer any need to worry about its population.\n\n"
  )

if (tallyPopulation()[2] == 0):
  print("Your species no longer exhibits the recessive trait.")
  if (tallyPopulation()[1] != 0):
    print(
        "However, there are still carriers of the trait in the population, and hopefully they can pass it on to their descendants.\n\nHOPEFUL FUTURE ENDING"
    )
  if (tallyPopulation()[1] == 0):
    print(
        "What's more, there are no more carriers of the recessive allele, so the trait has gone extinct. \n\nBAD ENDING: NO MORE RECESSIVE GENES"
    )
elif (tallyPopulation()[0] == 0):
  if (tallyPopulation()[1] == 0):
    print(
        "Your population no longer exhbits the dominant trait; It has gone extinct.\n\nBAD ENDING: NO MORE DOMINANT GENES"
    )
else:
  print(
      "Your population has survived with moderate biodiversity. However, its gene pool is still at risk of being homogenized by an environmental event.\n\nNEUTRAL ENDING"
  )

exit()
