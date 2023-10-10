from rectangle import rectangle_list
from geneticAlgorithm import GeneticAlgorithm
import time

# define parameters
box_height = 25
box_width = 25

#mutation_probability = 0.5
population_size = 64
number_of_generations = 100

number_of_tests = 30

def test_mutation_probability(number_of_tests, mutation_probabilities):
    with open("output.txt", "w") as file:
        for probability in mutation_probabilities:
            sum_scores = 0
            sum_times = 0
            avg_score = 0
            avg_time = 0

            file.write(str(probability) + '\n')

            for test in range(number_of_tests):
                start_time = time.time()
                ga = GeneticAlgorithm(population_size)
                test_score = ga.solve(probability, number_of_generations, rectangle_list, box_height, box_width)
                test_time = time.time() - start_time
                sum_scores += test_score
                sum_times += test_time
            
            avg_score = sum_scores / number_of_tests
            avg_time = sum_times / number_of_tests

            file.write(str(round(avg_score)) + '\n')
            file.write(str(round(avg_time)) + '\n')
            file.write('\n')

def test_population_size(number_of_tests, population_sizes):
    with open("output.txt", "w") as file:
        for size in population_sizes:
            sum_scores = 0
            sum_times = 0
            avg_score = 0
            avg_time = 0

            file.write(str(size) + '\n')

            for test in range(number_of_tests):
                start_time = time.time()
                ga = GeneticAlgorithm(size)
                test_score = ga.solve(mutation_probability, number_of_generations, rectangle_list, box_height, box_width)
                test_time = time.time() - start_time
                sum_scores += test_score
                sum_times += test_time
            
            avg_score = sum_scores / number_of_tests
            avg_time = sum_times / number_of_tests

            file.write(str(round(avg_score)) + '\n')
            file.write(str(round(avg_time)) + '\n')
            file.write('\n')

def test_number_of_generations(number_of_tests, numbers_of_generations):
    with open("output.txt", "w") as file:
        for number in numbers_of_generations:
            sum_scores = 0
            sum_times = 0
            avg_score = 0
            avg_time = 0

            file.write(str(number) + '\n')

            for test in range(number_of_tests):
                start_time = time.time()
                ga = GeneticAlgorithm(population_size)
                test_score = ga.solve(mutation_probability, number, rectangle_list, box_height, box_width)
                test_time = time.time() - start_time
                sum_scores += test_score
                sum_times += test_time
            
            avg_score = sum_scores / number_of_tests
            avg_time = sum_times / number_of_tests

            file.write(str(round(avg_score)) + '\n')
            file.write(str(round(avg_time)) + '\n')
            file.write('\n')

mutation_probabilities = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
test_mutation_probability(number_of_tests, mutation_probabilities)
#mutation_probability = 

#population_sizes = [50, 75, 100, 150, 200, 300, 400, 500]
#test_population_size(number_of_tests, population_sizes)
#population_size =

#numbers_of_generations = [100, 200, 300, 400, 500]
#test_number_of_generations(number_of_tests, numbers_of_generations)