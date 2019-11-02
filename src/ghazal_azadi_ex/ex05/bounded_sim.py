from walker_sim import Walker
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


class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit
        random.seed(seed)

    def bounded_single_walk(self):
        walker = BoundedWalker(self.start, self.home, self.left_limit,
                               self.right_limit)
        return walker.move()


    def bounded_run_simulation(self, num_walks):
        list_of_walks = []
        for walks in range(num_walks):
            list_of_walks.append(self.bounded_single_walk())
        return list_of_walks


if __name__ == "__main__":
    for left_limit in (0, -10, -100, -1000, -10000):
        bounded_walker = []
        bounded_simulation = []
        walk_1 = BoundedWalker(0, 20, left_limit, 20)
        walk_2 = BoundedSimulation(0, 20, 12345, left_limit, 20)
        bounded_walker.append(walk_1.move())
        bounded_simulation.append(walk_2.bounded_run_simulation(20))
        print(f'Left Limit: {left_limit} -> Path lengths of bounded walker is:'
              f' {bounded_walker}')
        print(f'Left Limit: {left_limit} -> Path lengths of bounded simulation'
              f' for 20 walks is: {bounded_simulation}')
