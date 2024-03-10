import math as m
import random as rand

population = []
POPULATIONSIZE = 10

class specimen:
    def __repr__(self):
        return f"Gene: {self.gene}, MutateRate: {self.mutateRate}, Fitness {self.fitnessValue}\n"
    def __init__(self, gene) -> None:
        self.gene = gene
        self.mutateRate = 0.05
        self.fitnessValue = 99999

    def fitnessFunc(self):
        x = self.gene
        self.fitnessValue = 0.1*x**5-0.2*x**3+x**2-2*x - 1


    def mutate(self):
        if rand.random() < self.mutateRate:
            self.gene = rand.gauss(self.gene, 0.2)

def CompFitness(x):
    for i in x:
        i.fitnessFunc()
    

def rank(pop):
    pop.sort(key = lambda x: abs(x.fitnessValue))


def mate(a,b):
    offspring = specimen(0.5*(a.gene + b.gene))
    offspring.mutate()
    return offspring


for i in range(POPULATIONSIZE):
    population.append(specimen(rand.uniform(0,m.pi)))

CompFitness(population)

lineage = []
generation = 1
while abs(population[0].fitnessValue) >= 0.001:
    print("===============================================")
    print(f"generation {generation}")
    if len(population)%2 == 0:
        population = population[:int(len(population)/2)]
    else:
        raise
    #print("sort done")
    #print([i for i in population])
    for i in range(len(population)-1):
        population.append(mate(population[i], population[i+1]))
    population.append(specimen(rand.uniform(0,m.pi)))
    #print("mate done")
    CompFitness(population)
    #print("fitness done")
    #print([i for i in population])
    rank(population)
    #print("rank done")
    print("Generation Best Fitness: ", population[0].fitnessValue)
    print("Generation Best Gene: ", population[0].gene)
    generation += 1
    lineage.append(population[0].gene)
    print("lineage: ", lineage)

