__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'

import random


class Walker:

    def __init__(self, start, home):
        self.start = start
        self.home = home
        self.steps = 0
        self.position = start

    def is_at_home(self):

        return self.position == self.home

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


class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        walker = Walker(self.start, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        list_of_walks = []
        for walks in range(num_walks):
            list_of_walks.append(self.single_walk())
        return list_of_walks


if __name__ == "__main__":
    walk_1 = Simulation(0, 10, 12345)
    print(walk_1.run_simulation(20))
    print(walk_1.run_simulation(20))
    walk_2 = Simulation(10, 0, 12345)
    print(walk_2.run_simulation(20))
    print(walk_2.run_simulation(20))
    walk_3 = Simulation(0, 10, 54321)
    print(walk_3.run_simulation(20))
    walk_4 = Simulation(10, 0, 54321)
    print(walk_4.run_simulation(20))
