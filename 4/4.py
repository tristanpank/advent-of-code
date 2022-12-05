with open('input.txt') as f:
    file_content = f.readlines()

pairs = []
for pair in file_content:
    new_pair = pair.strip()
    new_pair2 = new_pair.split(',')
    pairs.append(new_pair2)

overlap = 0
for pair in pairs:
    
    elf1_nums = pair[0].split('-')
    elf2_nums = pair[1].split('-')
    elf1 = [num for num in range(int(elf1_nums[0]), int(elf1_nums[1])+1)]
    elf2 = [num for num in range(int(elf2_nums[0]), int(elf2_nums[1])+1)]


    if len(elf1) > len(elf2):
        main_set = set(elf1)
        adding_list = elf2
    else:
        main_set = set(elf2)
        adding_list = elf1
    
    length1 = len(main_set)
    for num in adding_list:
        if num in main_set:
            print(elf1)
            print(elf2)
            overlap += 1
            break
    # length2 = len(main_set)
    
    # if length1 == length2:
    #     print(elf1)
    #     print(elf2)
    #     overlap += 1

print(overlap)