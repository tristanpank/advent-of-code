with open('input.txt') as f:
    signals = [line.strip() for line in f.readlines()]

for signal in signals:
    curr_chars = []
    curr_chars.extend(signal[:13])
    for i in range(3, len(signal)):
        curr_chars.append(signal[i])
        found_marker = True
        for char in curr_chars:
            if curr_chars.count(char) > 1:
                found_marker = False
        if found_marker == True:
            print(i+1)
            break
        else:
            curr_chars.pop(0)

