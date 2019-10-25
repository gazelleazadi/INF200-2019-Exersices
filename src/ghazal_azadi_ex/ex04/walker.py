import random


class Walker:

    def __init__(self, position, home_position):
        self.position = position
        self.home_position = home_position
        self.state = True
        self.steps = 0

    def is_at_home(self):

        if self.position == self.home_position:
            self.state = True
        else:
            self.state = False

        return self.state

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

    def walking_process(self):
        while not self.is_at_home():
            Walker.move(self)
        return Walker.get_steps(self)


if __name__ == "__main__":
    for distance in (1, 2, 5, 10, 20, 50, 100):
        path_lengths = []
        # five simulations
        for i in range(5):
            walk = Walker(0, distance)
            path_lengths.append(walk.walking_process())
        print(f'Distance: {distance} -> Path Lengths: {path_lengths}')
