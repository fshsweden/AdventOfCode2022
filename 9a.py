from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

with open('test-input-9.txt') as f:
    lines = [row.strip() for row in f]

class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        print(f"Grid Width: {self.width} Height: {self.height}")

        self.h_position_row = self.height // 2
        self.h_position_col = self.width // 2
        self.t_position_row = self.height // 2
        self.t_position_col = self.width // 2

        self.grid = multi_dict(2, int)
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.grid[row][col] = '.'

        self.grid[self.t_position_row][self.t_position_col] = 'T'
        self.grid[self.h_position_row][self.h_position_col] = 'H'

    def is_adjacent_to_head(self):
        
        if (self.h_position_row == self.t_position_row) or (self.h_position_row == self.t_position_row-1) or (self.h_position_row == self.t_position_row+1):
            if  (self.h_position_col == self.t_position_col - 1) or (self.h_position_col == self.t_position_col + 1) or (self.h_position_col == self.t_position_col):
                return True

        if  (self.h_position_col == self.t_position_col) or (self.h_position_col == self.t_position_col-1) or (self.h_position_col == self.t_position_col+1):
            if (self.h_position_row == self.t_position_row - 1) or (self.h_position_row == self.t_position_row + 1) or (self.h_position_row == self.t_position_row):
                return True

        return False

    def move_head(self, direction, steps):
        for i in range(0, steps):
            if not self.grid[self.h_position_row][self.h_position_col] == 'T':
                self.grid[self.h_position_row][self.h_position_col]='.'

            self.grid[self.h_position_row][self.h_position_col] = '.'
            self.move_head_one_step(direction)
            self.grid[self.h_position_row][self.h_position_col] = 'H'
            self.move_tail(direction)

    def move_tail(self, direction):
        if self.is_adjacent_to_head():
            print("H and T are adjacent... not moving tail")
        else:
            # MOVE TAIL
            self.grid[self.t_position_row][self.t_position_col] = '#'
            self.move_tail_one_step(direction)

    def move_head_one_step(self, direction):
        if direction == 'U':
            self.h_position_row -= 1
        elif direction == 'D':
            self.h_position_row += 1
        elif direction == 'R':
            self.h_position_col += 1
        elif direction == 'L':
            self.h_position_col -= 1
        else:
            raise (f"Unknown direction: {direction}")

    def move_tail_one_step(self, direction):
        if direction == 'U':
            self.t_position_row -= 1
        elif direction == 'D':
            self.t_position_row += 1
        elif direction == 'R':
            self.t_position_col += 1
        elif direction == 'L':
            self.t_position_col -= 1
        else:
            raise (f"Unknown direction: {direction}")

    def get(self, row, col):
        return self.grid[row][col]

    def print(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                print(self.grid[row][col], end='')
            print()

    

grid = Grid(8,8)

print(grid.is_adjacent_to_head())
grid.print()

grid.move_head('R', 1)
print(grid.is_adjacent_to_head())
grid.print()

grid.move_head('R', 1)
print(grid.is_adjacent_to_head())
grid.print()

grid.move_head('R', 1)
print(grid.is_adjacent_to_head())
grid.print()

# grid.print()
# for line in lines:
#     direction = line.split(" ")[0]
#     steps = int(line.split(" ")[1])
#     grid.move_head(direction, steps)
# grid.print()

def main():
    pass

if __name__ == "__main__":
    main()
