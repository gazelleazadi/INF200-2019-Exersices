def letter_freq(txt):
    txt = txt.lower()
    letter_new = {}
    for i in txt:
        letter_new[i] = txt.count(i)
    return letter_new

# Using Dictionary that holds unique "Key Values" pair.


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):
        print('{:3}{:10}'.format(letter, count))
