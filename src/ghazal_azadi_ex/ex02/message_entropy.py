def letter_freq(txt):
    txt = txt.lower()
    letter_new = {}
    for i in txt:
        letter_new[i] = txt.count(i)
    return letter_new


def entropy(message):
    # Function which calculates the entropy of the given msg.
    import math
    p = []
    freq = []
    number = len(message)
    n = list(letter_freq(message).values())
    # "n" is the number that each character is repeated in the message.
    # we convert it to list to be able to use or change it afterwards.
    # Names are chosen based on the entropy formula.
    for i in range(len(n)):
        p.append(n[i] / number)
        freq.append(p[i] / math.log(p[i], 2))
        # The formula of entropy
    h = - sum(freq)
    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        try:
            entropy(msg)
        except ZeroDivisionError:
            print('{:25}: {:8.3f} bits'.format(msg, 0))
        else:
            print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
