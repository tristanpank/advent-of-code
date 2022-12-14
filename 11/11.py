import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

class Monkey:
    def __init__(self, info:list):
        self.num = int(info[0][-2])
        items = [item for item in info[1][16:].split()]
        items[0] = items[0][:-1]
        self.items = [int(item) if ',' not in item else int(item[:-1]) for item in items]
        self.operation_sign = info[2].split()[4]
        self.operation_num = info[2].split()[5]
        self.test_num = int(info[3].split()[3])
        self.true_monkey = int(info[4][-1])
        self.false_monkey = int(info[5][-1])

    def operation(self, index):
        if self.operation_num == "old":
            self.operation_num = self.items[index]
        self.items[index] = ops[self.operation_sign](self.items[index], int(self.operation_num)) // 3

    def test(self, index):
        if self.items[index] % self.test_num == 0:
            return self.true_monkey
        else:
            return self.false_monkey

def main():
    with open('example.txt') as f:
        content = [line.strip() for line in f.readlines()]

    # monkey_0 = Monkey(content[:6])
    # print(monkey_0.num)
    # print(monkey_0.items)
    # print(monkey_0.operation_sign)
    # print(monkey_0.operation_num)
    # print(monkey_0.test_num)
    # print(monkey_0.true_monkey)
    # print(monkey_0.false_monkey)
    # monkey_0.operation(0)
    # print(monkey_0.items)
    # print(monkey_0.test(0))

    monkey_list = create_monkey_list(content)
    monkey_dict = {}
    for i in range(len(monkey_list)):
        monkey_dict[i] = 0
    for i in range(20):
        print('Round: ', i)
        for monkey in monkey_list:
            print(monkey.num, monkey.items)
        round(monkey_list, monkey_dict)
        
    print(monkey_dict)
    for monkey in monkey_list:
        print(monkey.num, monkey.items)

def single_monkey(monkey:Monkey, monkey_list:list, monkey_dict:dict):
    for i in range(len(monkey.items)):
        monkey.operation(0)
        new_monkey = monkey.test(0)
        item = monkey.items.pop(0)
        monkey_list[new_monkey].items.append(item)
        monkey_dict[monkey.num] += 1

def round(monkey_list:list, monkey_dict):
    for monkey in monkey_list:
        single_monkey(monkey, monkey_list, monkey_dict)
    
def create_monkey_list(content:list):
    monkey_list = []
    for i in range(0, len(content), 7):
        monkey_info = content[i:i+7]
        # print(monkey_info)
        monkey = Monkey(monkey_info)
        monkey_list.append(monkey)
    return monkey_list

if __name__ == "__main__":
    main()