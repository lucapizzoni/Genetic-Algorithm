from rectangle import rectangle_list
from geneticAlgorithm import GeneticAlgorithm

# define parameters
box_height = 25
box_width = 25
#print(i.chromosome)
population_size = 64 # = len(rectangle_list) * 2
mutation_probability = 0.01
number_of_generations = 100
ga = GeneticAlgorithm(population_size)
result = ga.solve(mutation_probability, number_of_generations, rectangle_list, box_height, box_width)