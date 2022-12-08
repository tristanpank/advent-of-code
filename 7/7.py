
def main():
    with open('input.txt') as f:
        terminal_lines = [line.strip() for line in f.readlines()]

    # directories = {'/': 0}
    # path = []
    # used_files = []
    # all_paths = []


    # for line in terminal_lines:
    #     if line == "$ cd /":
    #         path = ['/']
    #     elif line == "$ ls":
    #         continue
    #     elif line[:4] == "$ cd":
    #         if line[-2:] == "..":
    #             path.pop()
    #         else:
    #             path.append(line.split()[2])
    #     elif line[:3] == "dir":
    #         directory = line.split()[1]
    #         if directory not in directories:
    #             directories[directory] = 0
    #     else:
    #         file = line.split()
    #         filename = file[1]
    #         if filename not in used_files:
    #             total = 0
    #             for directory in path:
    #                 directories[directory] += int(file[0])
    #                 total += int(file[0])
    #             path.insert(0, total)
    #             all_paths.append(path)
    #             print(path)

    # total = 0
    # for directory in directories.keys():
    #     if directories[directory] < 100000:
    #         total += directories[directory]

    parent_directory = {'score': 0}
    path = []

    for line in terminal_lines:
        if line == "$ cd /":
            path = []
        elif line[:4] == "$ cd":
            if line[-2:] == "..":
                path.pop()
            else:
                path.append(line.split()[2])
        elif line == "$ ls":
            continue
        elif line[:3] == "dir":
            new_directory = line.split()[1]
            curr_dict = parent_directory
            for directory in path:
                curr_dict = curr_dict[directory]
            if new_directory not in curr_dict:
                curr_dict.update({new_directory: {'score': 0}})
        else:
            file = line.split()
            filename = file[1]
            curr_dict = parent_directory
            parent_directory["score"] += int(file[0])
            for directory in path:
                curr_dict = curr_dict[directory]
                curr_dict["score"] += int(file[0])
            curr_dict.update({file[0]: filename})

    directories = {'/': parent_directory['score']}
    # print(parent_directory)
    find_all_directories(parent_directory, directories)
    print(directories)
    print(find_deletion_size(directories, 30000000))

def calculate_total(parent_dicrectory):
    curr_dict = parent_dicrectory
    total = 0
    if curr_dict['score'] < 100000:
        total += curr_dict['score']
    for key in curr_dict:
        if key.isalpha() == True and key != 'score':
            total += calculate_total(curr_dict[key])
    return total

def find_all_directories(parent_directory, directories):
    curr_dict = parent_directory
    print(curr_dict['score'])
    for key in curr_dict:
        if key.isalpha() == True and key != 'score':
            directories.update({key: curr_dict[key]['score']})
            find_all_directories(curr_dict[key], directories)
        

def find_deletion_size(directories, target):
    keys = directories.keys()
    curr_min = directories['/']
    unused_space = 70000000 - curr_min
    target = target - unused_space
    print(target)
    for key in keys:
        if directories[key] > target:
            if directories[key] < curr_min:
                curr_min = directories[key]
    return curr_min

if __name__ == "__main__":
    main()




            
        