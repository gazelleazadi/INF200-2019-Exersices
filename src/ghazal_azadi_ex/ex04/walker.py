__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'

import random


class Walker:

    def __init__(self, position, home_position):
        self.position = position
        self.home_position = home_position
        # self.state = True
        self.steps = 0

    def is_at_home(self):

        # if self.position == self.home_position:
        # self.state = True
        # else:
        # self.state = False
        return self.position == self.home_position

    def move(self):
        if not self.is_at_home():
            rand = random.randint(0, 1)
            if rand == 0:
                self.position -= 1
            else:
                self.position += 1

            self.steps += 1

    def get_position(self):

        return self.position

    def get_steps(self):
        return self.steps


# Defining walking process function
def walking_process(start, home):
    w = Walker(start, home)
    while not w.is_at_home():
        w.move()
    return w.get_steps()

# if __name__ == "__main__":
# for distance in (1, 2, 5, 10, 20, 50, 100):
# path_lengths = []
# five simulations
# for i in range(5):
# walk = Walker(0, distance)
# path_lengths.append(walking_process())
# print(f'Distance: {distance} -> Path Lengths: {path_lengths}')
