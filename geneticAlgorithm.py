from individual import Individual
from random import random

class GeneticAlgorithm():
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = None

    # create initial population
    def initialize_population(self, rectangle_list, box_height, box_width):
        for i in range(self.population_size):
            self.population.append(Individual(rectangle_list, box_height, box_width))
            self.best_solution = self.population[0]
    
    # order population from best to worst individual
    def order_population(self):
        self.population = sorted(self.population, key=lambda population: population.score, reverse=True)

    # check if best individual of current generation is better the overall best individual and if so replace it
    def best_individual(self, individual):
        if individual.score > self.best_solution.score:
            self.best_solution = individual
    
    # print best score and chromosome of each population
    def visualize_generation(self):
        best = self.population[0]
        print('Generation: ', best.generation,
              '\nBest score: ', best.score,
              '\nBest chromosome: ', best.chromosome)
    
    # calculate sum of all scores of a population to be able to distribute the probabilities of being selected as a parent relatively to the fitness of the individual
    def sum_scores(self):
        sum = 0
        for individual in self.population:
            sum += individual.score
        return sum
    
    # select parent for crossover
    def select_parent(self, sum_scores):
        parent = -1
        random_value = random() * sum_scores # the higher the score of a individual the more likeable to be selected as a parent
        sum = 0
        i = 0
        while i < len(self.population) and sum < random_value:
            sum += self.population[i].score
            parent += 1
            i += 1
        return parent
    
    # perform genetic algorithm
    def solve(self, mutation_probability, number_of_generations, rectangle_list, box_height, box_width):
        # create initial population
        self.initialize_population(rectangle_list, box_height, box_width)
        for individual in self.population:
            individual.fitness()
        self.order_population()
        self.visualize_generation()

        # create further populations
        for generation in range(number_of_generations):
            sum = self.sum_scores()
            new_population = []
            for new_individuals in range(0, self.population_size, 2):
                # select two parents
                parent1 = -1
                parent2 = -1
                while parent1 == parent2: # make sure parents are not two times the same individual
                    parent1 = self.select_parent(sum)
                    parent2 = self.select_parent(sum)
                
                # perform crossover
                children = self.population[parent1].crossover(self.population[parent2])

                #perform mutation
                new_population.append(children[0].mutation(mutation_probability))
                new_population.append(children[1].mutation(mutation_probability))

            self.population = list(new_population)

            for individual in self.population:
                individual.fitness()
            self.order_population()
            self.visualize_generation()
            best = self.population[0]
            self.best_individual(best)
        
        # print overall best solution
        print('\n*** Best solution - Generation: ', self.best_solution.generation,
              '\nScore: ', self.best_solution.score,
              '\nChromosome: ', self.best_solution.chromosome)
        
        # reutrn score of best solution
        return self.best_solution.score