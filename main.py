from rectangle import rectangle_list
from geneticAlgorithm import GeneticAlgorithm

# define parameters
box_height = 25
box_width = 25
population_size = 200
mutation_probability = 0.5
number_of_generations = 400

# perform genetic algorithm
ga = GeneticAlgorithm(population_size)
ga.solve(mutation_probability, number_of_generations, rectangle_list, box_height, box_width)