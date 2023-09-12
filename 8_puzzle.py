initial_state = [1, 2, 3, 5, 6, 0, 7, 8, 4]
goal_state = [1, 2, 3, 5, 8, 6, 0, 7, 4]

def calculate_misplaced_tiles(state):
    return sum(1 for i, j in zip(state, goal_state) if i != j)

def generate_neighbors(state):
    neighbors = []
    empty_tile_index = state.index(0)
    rows, cols = 3, 3
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for move in possible_moves:
        new_row = empty_tile_index // cols + move[0]
        new_col = empty_tile_index % cols + move[1]

        if 0 <= new_row < rows and 0 <= new_col < cols:
            new_state = state[:]
            new_index = new_row * cols + new_col
            new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
            neighbors.append(new_state)

    return neighbors

def hill_climbing_search(initial_state):
    current_state = initial_state
    current_cost = calculate_misplaced_tiles(current_state)

    while True:

        print("Current State:")
        for i in range(0, 9, 3):
            print(current_state[i:i+3])

        neighbors = generate_neighbors(current_state)
        if not neighbors:
            break

        best_neighbor = min(neighbors, key=calculate_misplaced_tiles)
        best_cost = calculate_misplaced_tiles(best_neighbor)

        if best_cost >= current_cost:
            break

        current_state = best_neighbor
        current_cost = best_cost

    return current_state

solution = hill_climbing_search(initial_state)

print("\nGoal State:")
for i in range(0, 9, 3):
    print(goal_state[i:i+3])