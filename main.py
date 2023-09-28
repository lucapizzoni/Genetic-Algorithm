from rectangle import Rectangle
from individual import Individual


# create rectangles
rectangle_list = []
rectangle_list.append(Rectangle(2, 1))
rectangle_list.append(Rectangle(1, 2))
rectangle_list.append(Rectangle(1, 1))
rectangle_list.append(Rectangle(1, 3))
rectangle_list.append(Rectangle(1, 3))
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
'''

# define parameters
box_height = 3
box_width = 3
individual = Individual(rectangle_list, box_height, box_width);
#population_size = 64 # = len(rectangle_list) * 2
#mutation_probability = 0.01
#number_of_generations = 100
#ga = GeneticAlgorithm(population_size)
#result = ga.solve(mutation_probability, number_of_generations, spaces, prices, limit)
#print(result)





'''
# create box with all values = 0
box = []
for i in range(box_height):
    box.append([])
    for j in range(box_width):
        box[i].append(0)

'''






'''
from rectangle import Rectangle


for rectangle in rectangle_list:
    for i in range(len(box)):
        for j in reversed(range(len(box))):
                if box[j][i] == 0:
                    available = 1
                    for h in range(rectangle.height):
                        for w in range(rectangle.width):
                            print(box[j-h][i-w])
'''