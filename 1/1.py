with open('input.txt', 'r') as f:
    content = f.readlines()
    # print(content)
    calories = {}
    elf_num = 1
    curr_calories = 0
    for item in content[:-1]:
        if item == '\n':
            calories[elf_num] = curr_calories
            elf_num += 1
            curr_calories = 0
        else:
            curr_calories += int(item[:-1])
    calories[elf_num] = curr_calories + int(content[-1])
    elves = [key for key in calories.keys()]
    
    max_elves = elves[:3]
    max_elves.sort(key=lambda x: calories[x])
    print(max_elves)

    for elf in elves[3:]:
        if calories[elf] > calories[max_elves[0]]:
            index = 3
            for i in range(1, 3):
                if calories[elf] < calories[max_elves[i]]:
                    index = i
                    break
            max_elves.insert(index, elf)
            max_elves.pop(0)
            
    total = 0
    for elf in max_elves:
        total += calories[elf]
    print(total)


    # answer for part 1
    # curr_max = elves[0]
    # curr_max_cals = calories[elves[0]]
    # for elf in elves[1:]:
    #     if calories[elf] > curr_max_cals:
    #         curr_max = elf
    #         curr_max_cals = calories[elf]
    # print(curr_max)
    # print(calories[curr_max])