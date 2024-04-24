
import random

def generate_maze(rows, cols):
    maze = [['#'] * (2 * cols + 1) for _ in range(2 * rows + 1)]
    start_row, start_col = random.randrange(1, rows + 1) * 2 - 1, random.randrange(1, cols + 1) * 2 - 1
    maze[start_row][start_col] = ' '
    stack = [(start_row, start_col)]

    while stack:
        current_row, current_col = stack[-1]

        neighbors = []
        if current_row >= 3 and maze[current_row - 2][current_col] == '#':
            neighbors.append((current_row - 2, current_col))
        if current_row <= 2 * rows - 3 and maze[current_row + 2][current_col] == '#':
            neighbors.append((current_row + 2, current_col))
        if current_col >= 3 and maze[current_row][current_col - 2] == '#':
            neighbors.append((current_row, current_col - 2))
        if current_col <= 2 * cols - 3 and maze[current_row][current_col + 2] == '#':
            neighbors.append((current_row, current_col + 2))

        if neighbors:
            next_row, next_col = random.choice(neighbors)
            maze[(current_row + next_row) // 2][(current_col + next_col) // 2] = ' '
            maze[next_row][next_col] = ' '
            stack.append((next_row, next_col))
        else:
            stack.pop()

    return '\n'.join(''.join(row) for row in maze)

def main():
    rows = 10
    cols = 10
    maze = generate_maze(rows, cols)
    print(maze)

if __name__ == "__main__":
    main()
