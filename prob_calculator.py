import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**color):
    self.contents = []
    for k,v in color.items():
      for i in range (v):
        self.contents.append(k)
    

  def draw(self,draws):
    self.draws = draws
    draw = []
    if draws > len(self.contents):
      return self.contents
    for i in range(draws):
      random_ball = random.randint(0,(len(self.contents)-1))
      draw.append(self.contents[random_ball])
      self.contents.remove(self.contents[random_ball])
    return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors = hat_copy.draw(num_balls_drawn)

    for c in colors:
      if c in expected_balls_copy:
        expected_balls_copy[c]-=1
  
    if(all(x<=0 for x in expected_balls_copy.values())):
        count = count+1


  return count/num_experiments
