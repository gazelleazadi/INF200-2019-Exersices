from random import randint as rand_num

__author__ = 'ghazalazadi'
__email__ = 'ghaz@nmbu.no'


def guessed_num():
    """Returns the number being guessed by the user
    """
    inp_num = 0
    while inp_num < 1:
        inp_num = int(input('Your guess: '))
    return inp_num


def true_num():
    """Returns 2 * random number ( between 1,6) being created by the randint function
    """
    return rand_num(1, 6) + rand_num(1, 6)


def check_fun(f, g):
    """Checks if the true number is equal to the guessed number
    """
    return f == g


if __name__ == '__main__':

    h = False
    i = 3
    # The game would be finished after 3 times of wrong guessed numbers
    j = true_num()
    while h is False and i > 0:
        k = guessed_num()
        h = check_fun(j, k)

        if h is False:
            print('Wrong, try again!')
            i -= 1

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(j))
