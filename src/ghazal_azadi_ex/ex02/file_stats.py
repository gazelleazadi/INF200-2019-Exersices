def char_counts(textfilename):
    # Function which returns the number of occurrence of character code i.

    import io
    with io.open(textfilename, 'r', encoding='utf8') as file:
        txt = file.read()
    # Reading the file

    order = []
    for i in txt:
        order.append(ord(i))
    # Unicode code point of the character

    srt = {}
    for i in order:
        srt[i] = order.count(i)
    # Counting the unicode

    result = [0] * 256
    index = list(srt.keys())
    value = list(srt.values())
    for i in range(len(index)):
        result[index[i]] = value[i]
    # A list of 256 items, and the i-th item of this list is
    # the number of occurrence of the character with the code i.

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)
            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
