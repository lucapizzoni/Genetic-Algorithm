import random

class Individual():
  def __init__(self, rectangle_list, box_height, box_width, generation=0):
    self.rectangle_list = rectangle_list
    self.box_height = box_height
    self.box_width = box_width
    self.score = 0
    self.generation = generation
    self.chromosome = []
    
    # assign all rectancgles a random position
    for i in range(len(rectangle_list)):
        x = random.randint(0, box_height-1)
        y = random.randint(0, box_width-1)
        self.chromosome.append([x,y])
    
    self.make_feasible()
  
  def make_feasible(self):
    # delet all rectangles that go beyond the borders of the box
    for r in range(len(self.chromosome)):
      if (self.chromosome[r][0] + self.rectangle_list[r].height - 1) >= self.box_height:
        self.chromosome[r] = []
      elif (self.chromosome[r][1] + self.rectangle_list[r].width - 1) >= self.box_width:
        self.chromosome[r] = []

    #print('Chromosome before eliminating overlaps: ', self.chromosome)
    
    # if two rectangles overlap, the smaller rectangle gets deleted
    # create box with all values = -1
    box = []
    for i in range(self.box_height):
        box.append([])
        for j in range(self.box_width):
            box[i].append(-1)
    #print(box)

    area_current = 0
    area_other = 0
    available = False

    for r in range(len(self.chromosome)): # iterate over all rectangles

      other_rectangle = -1
      multiple_overlaps = False
      #print(r)
      
      # only do process if rectangle is being used
      if self.chromosome[r] != []: # if rectangle is used
        for i in range(self.rectangle_list[r].height): # iterate over all fields that rectangle would need
          for j in range(self.rectangle_list[r].width):
            #print('I,J: ', i,j)
            #print(box[i][j])
            #print(r, ': ', box[self.chromosome[r][0]+i][self.chromosome[r][1]+j])
            if box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] == -1: # if field is available
              if other_rectangle == -1:
                available = True
            else:
              available = False
              #print('Before: ', other_rectangle)
              #print('Now: ', box[self.chromosome[r][0]+i][self.chromosome[r][1]+j])
              if other_rectangle != box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] and other_rectangle != -1:
                multiple_overlaps = True
              other_rectangle = box[self.chromosome[r][0]+i][self.chromosome[r][1]+j]
              #print(other_rectangle)
              #break
        #print(available)

        # if not available
        if available == False:

          # calculate size of current and other rectangle
          area_current = self.rectangle_list[r].height * self.rectangle_list[r].width # calculate area of current rectangle
          area_other = self.rectangle_list[other_rectangle].height * self.rectangle_list[other_rectangle].width # calculate area of other rectangle
          #print('Area current: ', area_current, 'Area other: ', area_other)
          
          #print(len(other_rectangle))
          # if new rectangle bigger then old rectangle
          #print('R', r, ': ', multiple_overlaps)
          if area_current > area_other and multiple_overlaps == False:

            # delete other rectangle from box
            for i in range(self.box_height):
              for j in range(self.box_width):
                if box[i][j] == other_rectangle:
                  box[i][j] = -1
            
            # don't use other rectangle -> set to empty list
            self.chromosome[other_rectangle] = []
            #self.chromosome[box[i][j]] = [] # if the area of the current rectangle is bigger then from the other eliminate the other rectangle

            # write current rectangle in box
            for i in range(self.rectangle_list[r].height): # iterate over all fields that rectangle would need
              for j in range(self.rectangle_list[r].width):
                box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] = r
          
          # if old rectangle bigger then new rectangle
          else:
            self.chromosome[r] = [] # otherwise eliminate the current rectangle
        
        # if available
        else:
            for i in range(self.rectangle_list[r].height): # iterate over all fields that rectangle would need
              for j in range(self.rectangle_list[r].width):
                box[self.chromosome[r][0]+i][self.chromosome[r][1]+j] = r
            
    
    #print('Chromosome after eliminating overlaps: ', self.chromosome)
    #print(bo