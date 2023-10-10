from rectangle import rectangle_list
from geneticAlgorithm import GeneticAlgorithm
import time

# define parameters
box_height = 25
box_width = 25
mutation_probability = 0.5
population_size = 64
number_of_generations = 100

# perform genetic algorithm
ga = GeneticAlgorithm(population_size)
ga.solve(mutation_probability, number_of_generations, rectangle_list, box_height, box_width)