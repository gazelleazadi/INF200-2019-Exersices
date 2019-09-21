from random import randint

__author__ = 'ghazalazadi'
__email__ = 'ghaz@nmbu.no'


def guessed_num():
    """Returns the number being guessed by the user
    """
    input_num = 0
    while input_num < 1:
        input_num = int(input('Your guess: '))
    return input_num


def true_num():
    """Returns 2 * random number (between 1,6)  being created by the randint function
    """
    return randint(1, 6) + randint(1, 6)


def check_fun(main, guess):
    """Checks if the true number is equal to the guessed number
    """
    return main == guess


if __name__ == '__main__':

    result = False
    time = 3
    # The game would be finished after 3 times of wrong guessed numbers
    main = true_num()
    while result is False and time > 0:
        guess = guessed_num()
        result = check_fun(main, guess)

        if result is False:
            print('Wrong, try again!')
            time -= 1

    if time > 0:
        print('You won {} points.'.format(time))
    else:
        print('You lost. Correct answer: {}.'.format(main))
