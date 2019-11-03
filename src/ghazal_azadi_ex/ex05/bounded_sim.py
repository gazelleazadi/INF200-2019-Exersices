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
        if not self.is_at_home():
            rand = random.randint(0, 1)

            if self.position == self.right_limit and rand == 1:
                pass
            elif self.position == self.left_limit and rand == 0:
                pass
            else:
                if rand == 0:
                    self.position -= 1
                else:
                    self.position += 1
            self.steps += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit
        random.seed(seed)

    def single_walk(self):
        walker = BoundedWalker(self.start, self.home, self.left_limit,
                               self.right_limit)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()


if __name__ == "__main__":
    for left_limit in (0, -10, -100, -1000, -10000):
        bounded_simulation = []
        walk_2 = BoundedSimulation(0, 20, 12345, left_limit, 20)
        bounded_simulation.append(walk_2.run_simulation(20))
        print(f'Left Limit: {left_limit} -> Path lengths is:'
              f' {bounded_simulation}')
