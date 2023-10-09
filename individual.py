from random import random

class Individual():
  def __init__(self, rectangle_list, box_height, box_width, generation=0):
    self.rectangle_list = rectangle_list
    self.box_height = box_height
    self.box_width = box_width
    self.score = 0
    self.generation = generation
    self.chromosome = []
    
    # assign all rectancgles of individuals of initial population a random position
    for i in range(len(rectangle_list)):
        import random
        x = random.randint(0, box_height-1)
        y = random.randint(0, box_width-1)
        self.chromosome.append([x,y])
    
    # call make feasible
    self.make_feasible()
  
  # make individual feasible
  def make_feasible(self):
    # delet all rectangles that go beyond the borders of the box
    for r in range(len(self.chromosome)):
      if self.chromosome[r] != []: # if rectangle is used
        if (self.chromosome[r][0] + self.rectangle_list[r].height - 1) >= self.box_height:
          self.chromosome[r] = []
        elif (self.chromosome[r][1] + self.rectangle_list[r].width - 1) >= self.box_width:
          self.chromosome[r] = []
    
    # if two rectangles overlap, the smaller rectangle gets deleted
    # create box with all values = -1
    box = []
    for i in range(self.box_height):
        box.append([])
        for j in range(self.box_width):
            box[i].append(-1)
    
    area_current = 0
    area_other = 0
    available = False

    # iterate over all rectangles
    for r in range(len(self.chromosome)): 

      other_rectangle = -1
      multiple_overlaps = False
      
      if self.chromosome[r] != []: # only do process if rectangle is being used
        # iterate over all fields that the rectangle would need
        for i in range(self.rectangle_list[r].height):
          for j in range(self.rectangle_list[r].width):
            if box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] == -1: # if field is available
              if other_rectangle == -1: # and if there has been no overlap so far
                available = True
            else:
              available = False
              # check for multiple overlaps
              if other_rectangle != box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] and other_rectangle != -1:
                multiple_overlaps = True
              other_rectangle = box[self.chromosome[r][0]+i][self.chromosome[r][1]+j]

        # if not available
        if available == False:

          # calculate size of current and other rectangle
          area_current = self.rectangle_list[r].height * self.rectangle_list[r].width # calculate area of current rectangle
          area_other = self.rectangle_list[other_rectangle].height * self.rectangle_list[other_rectangle].width # calculate area of other rectangle

          # if new rectangle bigger then old rectangle and there are not multiple overlaps
          if area_current > area_other and multiple_overlaps == False:

            # delete other rectangle from box
            for i in range(self.box_height):
              for j in range(self.box_width):
                if box[i][j] == other_rectangle:
                  box[i][j] = -1
            
            # don't use other rectangle -> set to empty list
            self.chromosome[other_rectangle] = []

            # write current rectangle in box
            for i in range(self.rectangle_list[r].height): # iterate over all fields that rectangle would need
              for j in range(self.rectangle_list[r].width):
                box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] = r
          
          # if old rectangle bigger then new rectangle or there are multiple overlaps
          else:
            self.chromosome[r] = [] # otherwise eliminate the current rectangle
        
        # if available
        else:
            # iterate over all fields that rectangle needs
            for i in range(self.rectangle_list[r].height):
              for j in range(self.rectangle_list[r].width):
                # write rectangle in box
                box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] = r

  # calculate fitness of an individual (score is the space of the box that is occupied by rectangles)
  def fitness(self):
    used_space = 0
    for r in range(len(self.chromosome)):
      if self.chromosome[r] != []:
        used_space += self.rectangle_list[r].height * self.rectangle_list[r].width
    self.score = used_space
  
  # perform crossover
  def crossover(self, other_individual):
    
    # define cutoff
    cutoff  = 28
    #cutoff = round(random() * len(self.chromosome))
    #cutoff1 = 24
    #cutoff2 = 28

    # create two new individuals    
    children = [Individual(self.rectangle_list, self.box_height, self.box_width, self.generation + 1),
                Individual(self.rectangle_list, self.box_height, self.box_width, self.generation + 1)]
    
    # do the crossover
    child1_chromosome = other_individual.chromosome[0:cutoff] + self.chromosome[cutoff::]
    child2_chromosome = self.chromosome[0:cutoff] + other_individual.chromosome[cutoff::]
    #child1_chromosome = other_individual.chromosome[0:cutoff1] + self.chromosome[cutoff1:cutoff2] + other_individual.chromosome[cutoff2::]
    #child2_chromosome = self.chromosome[0:cutoff1] + other_individual.chromosome[cutoff1:cutoff2] + self.chromosome[cutoff2::]
  
    # assign the chromosomes to the children
    children[0].chromosome = child1_chromosome
    children[1].chromosome = child2_chromosome

    # make both children feasible
    children[0].make_feasible()
    children[1].make_feasible()
    
    return children
  
  # perform  mutation
  def mutation(self, rate):
    for r in range(len(self.chromosome)):
      # if the rectangle is not used so far
      if self.chromosome[r] == []:
        # perform mutation only with a certain probability
        if random() < rate:
          # give the rectangle a random position in the box
          self.chromosome[r] = [round(random() * (self.box_height-1)), round(random() * (self.box_width-1))]
    
    # make the mutated individual feasible
    self.make_feasible()

    return self