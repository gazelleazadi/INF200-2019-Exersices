from walker_sim import Walker, Simulation
import random

__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)

        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        while not self.is_at_home():
            rand = random.randint(0, 1)

            if self.position == self.right_limit and rand == 1:
                continue
            elif self.position == self.left_limit and rand == 0:
                continue
            else:
                if rand == 0:
                    self.position -= 1
                else:
                    self.position += 1
                self.steps += 1
        return self.steps


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)

        self.left_limit = left_limit
        self.right_limit = right_limit

    def bounded_single_walk(self):
        walker = BoundedWalker(self.start, self.home, self.left_limit,
                               self.right_limit)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def bounded_run_simulation(self, num_walks):
        list_of_walks = []
        for walks in range(num_walks):
            list_of_walks.append(self.bounded_single_walk())
        return list_of_walks
