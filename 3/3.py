with open('example.txt', 'r') as f:
    file_sacks = f.readlines()

sacks = []
for sack in file_sacks:
    sacks.append(sack.replace('\n', ""))

score = 0

for i in range(0, len(sacks), 3):
    elf1 = sacks[i]
    elf2 = sacks[i+1]
    elf3 = sacks[i+2]

    for item in elf1:
        if item in elf2 and item in elf3:
            shared = item
            break
    if shared.islower():
        score += ord(shared) - 96
    else:
        score += ord(shared) - 38
print(score)



# score = 0
# for sack in sacks:
#     half = int(len(sack) / 2)
#     comp1 = sack[:half]
#     comp2 = sack[half:]
#     repeat = None
#     for item in comp1:
#         if item in comp2:
#             repeat = item
#             break
#     if repeat.islower():
#         score += ord(repeat) - 96
#     else:
#         score += ord(repeat) - 38
# print(score)