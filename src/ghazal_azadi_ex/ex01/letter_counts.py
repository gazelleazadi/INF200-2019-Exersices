# First Part of the Question


def letter_freq(txt):
    txt = txt.lower()
    letter_new = {}
    i: letter
    for i in txt:
        letter_new[i] = txt.count(i)
    return letter_new

# Using Dictionary that holds unique "Key Values" pair.


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))


# Second Part of the Question
def letter_freq(txt):
    txt = txt.lower()
    txt = sorted(txt)
    letter_new = {}
    i: letter
    for i in txt:
        letter_new[i] = txt.count(i)
    return letter_new


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print("{:3}{:10}".format(letter, count))
