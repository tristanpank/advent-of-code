class Stack:
    def __init__(self, *stack_inputs):
        self.stacks = [stack for stack in stack_inputs]

    def move_items(self, num_items, stack1, stack2):
        moving_items = self.stacks[stack1][-num_items:]
        for _ in range(num_items):
            self.stacks[stack1].pop()
            # item = self.stacks[stack1].pop()
            # self.stacks[stack2].append(item)
        self.stacks[stack2].extend(moving_items)

with open('input.txt') as f:
    file_content = [line.strip().split() for line in f.readlines()]
    # file_content = [num for num in filter(lambda x: x.isdigit(), file_content)]



item_stack_example = Stack(['Z', 'N'], ['M', 'C', 'D'], ['P'])
item_stack_input = Stack(
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    ['D', 'P', 'J'],
    ['D', 'C', 'N', 'W', 'V']
)

for row in file_content:
    nums = [int(num) for num in filter(lambda x: x.isnumeric(), row)]
    item_stack_input.move_items(nums[0], nums[1]-1, nums[2]-1)


for stack in item_stack_input.stacks:
    print(stack[-1], end="")
print()