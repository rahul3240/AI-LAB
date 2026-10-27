import heapq

GOAL = (
    1,2,3,
    4,5,6,
    7,8,0
)

MOVES = {
    "UP":(-1,0),
    "DOWN":(1,0),
    "LEFT":(0,-1),
    "RIGHT":(0,1),
}

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        tile=state[i]

        if tile==0:
            continue
        current_row=i//3
        current_col=i%3

        goal_index=tile-1
        goal_row=goal_index//3
        goal_col=goal_index%3

        distance+=abs(current_row-goal_row)
        distance+=abs(current_col-goal_col)

    return distance

def display(state):
    for i in range(0,9,3):
        row=[]
        for j in range(i,i+3):
            if state[j]==0:
                row.append("_")
            else:
                row.append(str(state[j]))
        print(" ".join(row))
    print()

def is_solvable(state):
    numbers=[x for x in state if x !=0]
    inversions = 0

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
                inversions+=1
    return inversions%2==0


def get_successors(state):
    successors=[]
    blank_position=state.index(0)
    
    blank_row = blank_position // 3
    blank_col = blank_position % 3

    for action, (row_change, col_change) in MOVES.items():

        new_row = blank_row + row_change
        new_col = blank_col + col_change
        if 0 <= new_row < 3 and 0 <= new_col < 3:
        
            new_position = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank_position], new_state[new_position] = \
                new_state[new_position], new_state[blank_position]

            successors.append(
                (tuple(new_state), action)
            )
        
    return successors

def a_star(start):
    frontier = []

    g = 0
    h = manhattan_distance(start)
    f = g + h

    heapq.heappush(frontier, (f, g, start, []))

    explored = set()

    while frontier:

        f, g, state, path = heapq.heappop(frontier)

        if state == GOAL:
            return path, g

        if state in explored:
            continue

        explored.add(state)

        for new_state, action in get_successors(state):

            if new_state in explored:
                continue

            new_g = g + 1
            new_h = manhattan_distance(new_state)
            new_f = new_g + new_h

            new_path = path + [(action, new_state)]

            heapq.heappush(
                frontier,
                (new_f, new_g, new_state, new_path)
            )

    return None, -1


def main():

    print("8-PUZZLE USING A* SEARCH")
    print("Enter the puzzle (use _ for blank):")

    values = []

    for i in range(3):
        row = input().split()

        for value in row:
            if value == "_":
                values.append(0)
            else:
                values.append(int(value))

    start = tuple(values)

    print("\nInitial State:")
    display(start)

    if not is_solvable(start):
        print("No solution exists for this puzzle.")
        return

    solution, cost = a_star(start)

    if solution is None:
        print("No solution exists.")
        return

    current_state = start

    for move_number, (action, state) in enumerate(solution, start=1):

        print("Move", move_number, ":", action)
        display(state)

        current_state = state

    print("Goal State Reached")
    print("Solution Cost =", cost)


if __name__ == "__main__":
    main()