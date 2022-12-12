
def main():
    with open('input.txt') as f:
        moves = [line.strip() for line in f.readlines()]

    print(moves)

    positions = set()

    # position = (x, y)
    head = (0, 0)
    tail = (0, 0)
    positions.add(tail)
    for move in moves:
        for _ in range(int(move[2:])):
            direction = move[0]
            
            if direction == "R":
                head = (head[0]+1, head[1])
            elif direction == "L":
                head = (head[0]-1, head[1])
            elif direction == "U":
                head = (head[0], head[1]+1)
            elif direction == "D":
                head = (head[0], head[1]-1)
            tail = move_tail(head, tail)
            positions.add(tail)
            print(head)
            print(tail)

    print(positions)
    print(len(positions))

def move_tail(head, tail):
    tail_x = tail[0]
    tail_y = tail[1]
    head_x = head[0]
    head_y = head[1]
    if tail == head:
        return tail
    if abs(tail_x - head_x) + abs(tail_y - head_y) < 2:
        return tail
    elif tail[0] == head[0]:
        if head[1] > tail[1]:
            tail_y += 1
        else:
            tail_y -= 1
        return  (tail_x, tail_y)
    elif tail[1] == head[1]:
        if head[0] > tail[0]:
            tail_x += 1
        else:
            tail_x -= 1
        return (tail_x, tail_y)
    else:
        if abs(tail_x - head_x) + abs(tail_y - head_y) <= 2:
            return tail
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1
        return (tail_x, tail_y)

if __name__ == "__main__":
    main()