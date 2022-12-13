
from collections import defaultdict
from ctypes import ArgumentError
import sys

# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))


class Walker:

    def __init__(self):
        with open('input-12.txt') as f:
            lines = [row.strip() for row in f]

        self.grid = multi_dict(2, str)
        self.visited_grid = multi_dict(2, int)
        self.solution = []

        """
        Read file and create a grid. Save the character in the cell (we will convert to elevation later)
        and also save a visited flag in a separate grid. Default is 0, 1 means visited.
        """
        row = 0
        for line in lines:
            col = 0
            letters = list(line)
            for l in letters:
                self.grid[row][col] = l
                self.visited_grid[row][col] = 0
                col += 1
            row += 1

        """
        Save the width and height of the grid
        """
        self.width = col
        self.height = row

    """
    Convert the character in the grid to an elevation. S is 0, E is 1000, and a-z is 1-26
    """
    def elevation(self, row, col):
        if self.inside_grid(row, col) == False:
            raise ArgumentError(f"row {row} or col {col} is out of bounds")

        l = self.grid[row][col]
        if (l == "S"):
            return 0
        elif (l == "E"):
            return 1000
        else:
            return ord(l)-ord("a")

    def get_starting_point(self):
        for x in self.grid:
            for y in self.grid[x]:
                if self.grid[x][y] == "S":
                    return x, y
        raise "No starting point found"


    def get_ending_point(self):
        for x in self.grid:
            for y in self.grid[x]:
                if self.grid[x][y] == "E":
                    return x, y
        raise "No ending point found"

    """
    Run the walker. This will start at the starting point and walk to the ending point.
    Begin by taking one step. take_step() is recursive
    """
    def run(self):
        row,col = self.get_starting_point()
        end_row,end_col = self.get_ending_point()
        visited_steps = [(row,col)] # current cell is visited
        self.take_step(self.grid, self.width, self.height, row, col, end_row, end_col, visited_steps)

    """
    Print the grid first and the elevation of each cell next
    """    
    def printGrid(self):
        
        print(f"Printing Grid")

        for row in self.grid:
            for col in self.grid[row]:
                print(self.grid[row][col], end='')
            print()

        # for row in self.grid:
        #     for col in self.grid[row]:
        #         print(f"{self.elevation(row,col)}", end='-')
        #     print()

        # for row in self.grid:
        #     for col in self.grid[row]:
        #         print(self.visited_grid[row][col], end='')
        #     print()

    def inside_grid(self, row, col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width

    def ok_elevation(self, row, col, to_row, to_col):
        return self.elevation(to_row,to_col) == 1000 or (self.elevation(to_row,to_col) in [self.elevation(row,col), self.elevation(row,col) + 1])


    """
    Look around the current cell and return a list of possible steps. 
    Only cells that are 
        * current_height or current_height + 1
        * not visited
        * not out of bounds
    ... are possible steps.
    """
    def possible_steps(self, row, col, visited_steps):
        #print(f"Enter: possible_steps({row},{col})")
        myelevation = self.elevation(row,col)
        #print(f"Current elevation is {myelevation}")
        
        poss = []
        # Can we go up? Check edge!
        if row > 0:
            #print(f"Checking up... {self.grid[row-1][col]} with elevation {self.elevation(row-1,col)}")
            if self.ok_elevation(row, col, row-1,col):
                #print("Elevation is OK!")
                if (row-1,col) not in visited_steps:
                    #print("We have not been there so lets append this row/col!")
                    visited_steps.append((row-1,col))
                    poss.append([row-1,col])

        # Can we go down? Check edge!
        if row < self.height-1:
            #print(f"Checking down... {self.grid[row+1][col]} with elevation {self.elevation(row+1,col)}")
            if self.ok_elevation(row, col, row+1,col):
                #print("Elevation is OK!")
                if (row+1,col) not in visited_steps:
                    #print("We have not been there so lets append this row/col!")
                    visited_steps.append((row+1,col))
                    poss.append([row+1,col])

        # Can we go left? Check edge!
        if col > 0:
            #print(f"Checking left... {self.grid[row][col-1]} with elevation {self.elevation(row,col-1)} ")
            if self.ok_elevation(row, col, row,col-1):
                #print("Elevation is OK!")
                if (row,col-1) not in visited_steps:
                    #print("We have not been there so lets append this row/col!")
                    visited_steps.append((row,col-1))
                    poss.append([row,col-1])

        # Can we go right? Check edge!
        if col < self.width-1:
            #print(f"Checking right... {self.grid[row][col+1]} with elevation {self.elevation(row,col+1)}")
            if self.ok_elevation(row, col, row,col+1):
                #print("Elevation is OK!")
                if (row,col+1) not in visited_steps:
                    #print("We have not been there so lets append this row/col!")
                    visited_steps.append((row,col+1))
                    poss.append([row,col+1])

        #print(f"Returning possible steps: {poss}")
        return poss, visited_steps

    #
    # Look around and create a new Walker for each possible step
    #
    def take_step(self, grid, width, height, row,col, end_x, end_y, visited_steps):

        #print("----------------------------------------------------------------------------")
        #print(f"We are at row:{row} col:{col} content: {self.grid[row][col]}")
        steps,visited_steps = self.possible_steps(row, col, visited_steps)
        #print(f"Possible steps are: {steps}")

        for step in steps:
            #print(f"** Stepping to: {step}")
            if grid[step[0]][step[1]] == "E":
                print(f"Found the end! {len(visited_steps)} {visited_steps}")
                self.solution.append(len(visited_steps))

            self.take_step(grid, width, height, step[0], step[1], end_x, end_y, visited_steps.copy())

        #print("returning from take_step")


if __name__ == "__main__":
    wlkr = Walker()
    wlkr.printGrid()
    wlkr.run()

    print(wlkr.solution, min(wlkr.solution))
