from individual import Individual
from random import random

class GeneticAlgorithm():
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = None
        #self.list_of_solutions = []

    def initialize_population(self, rectangle_list, box_height, box_width):
        for i in range(self.population_size):
            self.population.append(Individual(rectangle_list, box_height, box_width))
            self.best_solution = self.population[0]
    
    def order_population(self):
        self.population = sorted(self.population, key=lambda population: population.score, reverse=True)

    def best_individual(self, individual):
        if individual.score > self.best_solution.score:
            self.best_solution = individual
    
    def visualize_generation(self):
        best = self.population[0]
        print('Generation: ', best.generation,
              '\nBest score: ', best.score,
              '\nBest chromosome: ', best.chromosome)
        
    def sum_scores(self):
        sum = 0
        for individual in self.population:
            sum += individual.score
        return sum
    
    def select_parent(self, sum_scores):
        parent = -1
        random_value = random() * sum_scores
        sum = 0
        i = 0
        #print('*** random value:', random_value)
        while i < len(self.population) and sum < random_value:
            #print('i: ', i, '- sum: ', sum)
            sum += self.population[i].score
            parent += 1
            i += 1
        return parent

    def solve(self, mutation_probability, number_of_generations, rectangle_list, box_height, box_width):
        self.initialize_population(rectangle_list, box_height, box_width)

        for individual in self.population:
            individual.fitness()
        self.order_population()

        self.visualize_generation()

        for generation in range(number_of_generations):
            sum = self.sum_scores()
            new_population = []
            for new_individuals in range(0, self.population_size, 2):
                parent1 = -1 #optional
                parent2 = -1 #optional
                while parent1 == parent2: #optional: make sure parents are not two times the same individual
                    parent1 = self.select_parent(sum)
                    parent2 = self.select_parent(sum)
                children = self.population[parent1].crossover(self.population[parent2])
                new_population.append(children[0].mutation(mutation_probability))
                new_population.append(children[1].mutation(mutation_probability))
                #new_population.append(children[0])
                #new_population.append(children[1])

            self.population = list(new_population)

            for individual in self.population:
                individual.fitness()
            self.order_population()
            self.visualize_generation()
            best = self.population[0]
            self.best_individual(best)
        print('\n*** Best solution - Generation: ', self.best_solution.generation,
              '\nScore: ', self.best_solution.score,
              '\nChromosome: ', self.best_solution.chromosome)
        return self.best_solution.chromosome