from rectangle import Rectangle
from individual import Individual
from geneticAlgorithm import GeneticAlgorithm

# create rectangles
#'''
rectangle_list = []
rectangle_list.append(Rectangle(2, 1))
rectangle_list.append(Rectangle(1, 2))
rectangle_list.append(Rectangle(1, 1))
rectangle_list.append(Rectangle(1, 3))
rectangle_list.append(Rectangle(1, 3))
'''
'''
rectangle_list = []
rectangle_list.append(Rectangle(2, 12))
rectangle_list.append(Rectangle(7, 12))
rectangle_list.append(Rectangle(8, 6))
rectangle_list.append(Rectangle(3, 6))
rectangle_list.append(Rectangle(3, 5))
rectangle_list.append(Rectangle(5, 5))
rectangle_list.append(Rectangle(3, 12))
rectangle_list.append(Rectangle(3, 7))
rectangle_list.append(Rectangle(5, 7))
rectangle_list.append(Rectangle(2, 6))
rectangle_list.append(Rectangle(3, 2))
rectangle_list.append(Rectangle(4, 2))
rectangle_list.append(Rectangle(3, 4))
rectangle_list.append(Rectangle(4, 4))
rectangle_list.append(Rectangle(9, 2))
rectangle_list.append(Rectangle(11, 2))
rectangle_list.append(Rectangle(4, 14))
rectangle_list.append(Rectangle(5, 2))
rectangle_list.append(Rectangle(2, 2))
rectangle_list.append(Rectangle(9, 7))
rectangle_list.append(Rectangle(5, 5))
rectangle_list.append(Rectangle(2, 5))
rectangle_list.append(Rectangle(7, 7))
rectangle_list.append(Rectangle(3, 5))
rectangle_list.append(Rectangle(6, 5))
rectangle_list.append(Rectangle(3, 2))
rectangle_list.append(Rectangle(6, 2))
rectangle_list.append(Rectangle(4, 6))
rectangle_list.append(Rectangle(6, 3))
rectangle_list.append(Rectangle(10, 3))
rectangle_list.append(Rectangle(6, 3))
rectangle_list.append(Rectangle(10, 3))
#'''

# define parameters
box_height = 60
box_width = 60
#i = Individual(rectangle_list, box_height, box_width)
#print(i.chromosome)
population_size = 64 # = len(rectangle_list) * 2
mutation_probability = 0.05
number_of_generations = 100
ga = GeneticAlgorithm(population_size)
result = ga.solve(mutation_probability, number_of_generations, rectangle_list, box_height, box_width)
#print('Best solution: ', result)