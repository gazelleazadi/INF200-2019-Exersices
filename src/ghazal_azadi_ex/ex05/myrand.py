from random import seed
import math

__author__ = 'Ghazal_Azadi'
__email__ = '@ghazal.azadi@nmbu.no'


class LCGRand:
    slope = 7 ** 5
    congruence_class = (2 ** 31) - 1

    def __init__(self, seed):
        self.hidden_state = seed

    def rand(self):
        self.hidden_state *= self.slope
        self.hidden_state %= self.congruence_class

        return self.hidden_state

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        return RandIter(self, length=math.inf)


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = 0


    def __iter__(self):
        if self.num_generated_numbers != 0:
            raise RuntimeError("Iter is called twice")
        self.num_generated_numbers += 1
        return self

    def __next__(self):
        if self.num_generated_numbers == 0:
            raise RuntimeError("Next can not be called before iteration")
        if self.num_generated_numbers > self.length:
            raise StopIteration(f'Can generalise just for {self.length} times')
        rand_num = self.generator.rand()
        self.num_generated_numbers += 1
        return rand_num
