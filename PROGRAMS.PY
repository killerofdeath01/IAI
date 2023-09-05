PROBLEM-1
PAC-MAN
CODE-
from queue import PriorityQueue

def nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    # Define the directions for UP, DOWN, LEFT, and RIGHT
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # Create a visited array to keep track of visited cells
    visited = [[False] * c for _ in range(r)]
    
    # Create a priority queue (min-heap) for UCS
    pq = PriorityQueue()
    
    # Initialize the priority queue with the starting position and cost
    pq.put((0, pacman_r, pacman_c))
    
    # Initialize the parent dictionary to store the path
    parent = {}
    
    while not pq.empty():
        cost, curr_x, curr_y = pq.get()
        
        # Mark the current cell as visited
        visited[curr_x][curr_y] = True
        
        # If the current cell is the food, break the loop
        if curr_x == food_r and curr_y == food_c:
            break
        
        # Explore neighbors
        for d in range(4):
            next_x, next_y = curr_x + dx[d], curr_y + dy[d]
            
            # Check if the next cell is valid and not visited
            if 0 <= next_x < r and 0 <= next_y < c and not visited[next_x][next_y] and grid[next_x][next_y] != '%':
                # Calculate the cost to move to the next cell
                move_cost = 0 if grid[next_x][next_y] == '.' else 1
                total_cost = cost + move_cost
                
                # Push the next cell into the priority queue with its cost
                pq.put((total_cost, next_x, next_y))
                
                # Store the parent of the next cell
                parent[(next_x, next_y)] = (curr_x, curr_y)
    
    # Reconstruct the path from food to pacman
    path = []
    curr_x, curr_y = food_r, food_c
    while (curr_x, curr_y) != (pacman_r, pacman_c):
        path.append((curr_x, curr_y))
        curr_x, curr_y = parent[(curr_x, curr_y)]
    path.append((pacman_r, pacman_c))
    
    # Print the distance and path
    print(len(path) - 1)
    for x, y in reversed(path):
        print(x, y)

# Sample Input
pacman_r, pacman_c = map(int, input().split())
food_r, food_c = map(int, input().split())
r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]

# Call the function with the provided input
nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)

OUTPUT-

PROBLEM-2
N PRINCESS
CODE-
def displayPathtoPrincess(N, grid):
    # Find the positions of 'm' (bot) and 'p' (princess)
    bot_position = None
    princess_position = None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # Calculate the difference in positions to determine the moves needed
    delta_x = princess_position[0] - bot_position[0]
    delta_y = princess_position[1] - bot_position[1]

    # Generate and print the moves to rescue the princess
    moves = []
    if delta_x < 0:
        moves.extend(['UP'] * abs(delta_x))
    elif delta_x > 0:
        moves.extend(['DOWN'] * abs(delta_x))

    if delta_y < 0:
        moves.extend(['LEFT'] * abs(delta_y))
    elif delta_y > 0:
        moves.extend(['RIGHT'] * abs(delta_y))

    for move in moves:
        print(move)

# Read input
N = int(input())
grid = [list(input()) for _ in range(N)]

# Call the function to rescue Princess Peach
displayPathtoPrincess(N, grid)

OUTPUT-

PROBLEM-3
PROBABILITY 1
CODE-
#include <stdio.h>

int main() {
    int x; 
    

    int favorable_outcomes = 0;
    int total_outcomes = 0;

    for (int die1 = 1; die1 <= 6; die1++) {
        for (int die2 = 1; die2 <= 6; die2++) {
            if (die1 != die2 && die1 + die2 == 6){
                favorable_outcomes++;
            }
            total_outcomes++;
        }
    }

   
    int gcd = 1;
    for (int i = 1; i <= favorable_outcomes; i++) {
        if (favorable_outcomes % i == 0 && total_outcomes % i == 0) {
            gcd = i;
        }
    }
    favorable_outcomes /= gcd;
    total_outcomes /= gcd;

    printf("%d/%d\n", favorable_outcomes, total_outcomes);

    return 0;
}

OUTPUT-

PROBLEM-4
N-PUZZEL
CODE-
from queue import PriorityQueue

class PuzzleNode:
    def _init_(self, state, parent, move, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def _lt_(self, other):
        return self.cost < other.cost

def get_blank_position(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def is_goal_state(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != i * n + j + 1:
                return False
    return True

def get_possible_moves(state):
    moves = []
    i, j = get_blank_position(state)
    n = len(state)

    if i > 0:
        moves.append("UP")
    if i < n - 1:
        moves.append("DOWN")
    if j > 0:
        moves.append("LEFT")
    if j < n - 1:
        moves.append("RIGHT")

    return moves

def apply_move(state, move):
    i, j = get_blank_position(state)
    new_state = [list(row) for row in state]

    if move == "UP":
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif move == "DOWN":
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif move == "LEFT":
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif move == "RIGHT":
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

    return new_state

def solve_puzzle(initial_state):
    n = len(initial_state)
    initial_node = PuzzleNode(initial_state, None, None, 0)

    priority_queue = PriorityQueue()
    priority_queue.put(initial_node)

    visited_states = set()

    while not priority_queue.empty():
        current_node = priority_queue.get()
        current_state = current_node.state

        if is_goal_state(current_state):
            moves = []
            while current_node.parent:
                moves.append(current_node.move)
                current_node = current_node.parent
            moves.reverse()
            return moves

        visited_states.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            new_state = apply_move(current_state, move)
            if tuple(map(tuple, new_state)) not in visited_states:
                new_node = PuzzleNode(new_state, current_node, move, current_node.cost + 1)
                priority_queue.put(new_node)

    return None

# Read input
k = int(input())
initial_state = [list(map(int, input().split())) for _ in range(k)]

# Solve the puzzle
moves = solve_puzzle(initial_state)

# Print the solution
if moves:
    print(len(moves))
    for move in moves:
        print(move)
else:
    print("No solution found")

OUTPUT-

PROBLEM-5
PROBABILITY-2
CODE-
p_defective_plant1 = 0.1
p_defective_plant2 = 0.15
p_defective_plant3 = 0.2

# Total production from each plant
production_plant1 = 1000
production_plant2 = 800
production_plant3 = 1200

# Total production across all plants
total_production = production_plant1 + production_plant2 + production_plant3

# Probability that a randomly selected pipe is defective
p_defective = (production_plant1 * p_defective_plant1 + production_plant2 * p_defective_plant2 + production_plant3 * p_defective_plant3) / total_production

# Probability that a defective pipe came from plant 1 using Bayes' theorem
p_plant1_given_defective = (p_defective_plant1 * production_plant1) / (p_defective * total_production)

# Simplify the fraction to get the answer in the required format
def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Simplify the fraction
simplified_fraction = simplify_fraction(p_plant1_given_defective, 1)

# Print the answer in the required format
print(f"{simplified_fraction[0]}/{simplified_fraction[1]}")

OUTPUT-
