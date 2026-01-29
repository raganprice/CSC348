def frequency_analysis(message, sym_len):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    sym_len = len(symbols)

    frequency = {}
    i = 0
    while i < sym_len:
        frequency[symbols[i]] = 0
        i += 1

    count = len(message)
    i = 0
    while i < count:
        c = message[i]

        if c >= 'a' and c <= 'z': #function to convert lower case to upper - used for test "I love WFU (go Deacs!)""
            c = c.upper() 

        if c in frequency:
            frequency[c] += 1

        i += 1

    i = 0
    while i < sym_len:
        frequency[symbols[i]] = frequency[symbols[i]] / count
        i += 1

    return frequency              

print(frequency_analysis("AB CD", 0))







