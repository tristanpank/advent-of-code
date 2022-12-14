with open('input.txt') as f:
    commands = [line.strip() for line in f.readlines()]

# print(commands)

cycle = 0
x = 1
signal = 0

screen = ["", "", "", "", "", ""]

for command in commands:
    cycle += 1
    pixel = cycle - 1
    row = pixel // 40
    pixel = pixel - 40 * row
    if abs(x - pixel) <= 1:
        screen[row] += "#"
    else:
        screen[row] += "."

    if command[:4] == "addx":
        cycle += 1
        pixel = cycle - 1
        row = pixel // 40
        pixel = pixel - 40 * row
        if abs(x - pixel) <= 1:
            screen[row] += "#"
        else:
            screen[row] += "."
        if cycle == 20 or (cycle - 20) % 40 == 0:
            # print(cycle, x)
            signal += cycle * x
        # print(command[5:])
        x += int(command[5:])
    if cycle == 20 or (cycle - 20) % 40 == 0:
        # print(cycle, x)
        signal += cycle * x
    if command == "noop":
        continue

print(signal)

for row in screen:
    print(row)