import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    self.n_of_contents = 0

    for key, val in kwargs.items():
      for i in range(val):
        self.contents.append(key)
      self.n_of_contents += val

    self.n = copy.copy(self.n_of_contents - 1)

  def draw(self, num_of_balls):
    removed = []

    if num_of_balls > self.n_of_contents:
      return num_of_balls

    for i in range(num_of_balls):
      rand = random.randint(0, (self.n_of_contents - 1))
      removed.append(self.contents.pop(rand))
      self.n_of_contents -= 1

    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected = {}

  probability = 0

  for key, val in expected_balls.items():
    expected.setdefault(key, 0)

  for i in range(num_experiments):
    draw = hat.draw(num_balls_drawn)
    if isinstance(draw, int):
      return draw

    for ball in draw:
      for key in expected:
        if key == ball:
          expected[key] += 1

        else:
          break

    print(expected_balls)
    for val in expected_balls.values():
      print(val)
      probability += (val / hat.n)

    return probability
