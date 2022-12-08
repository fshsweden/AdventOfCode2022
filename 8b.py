from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))


with open('input-8.txt') as f:
    lines = [row.strip() for row in f]


class Tree:
    def __init__(self, row, col, height) -> None:
        self.row = row
        self.col = col
        self.height = height

        self.visible_from_west = None
        self.visible_from_east = None
        self.visible_from_north = None
        self.visible_from_south = None

    # is this tree visible from any direction?
    def isVisible(self):
        return self.visible_from_west or self.visible_from_east or self.visible_from_north or self.visible_from_south

    def __str__(self) -> str:
        return f"Tree at {self.row}/{self.col}"

    def __repr__(self) -> str:
        return f"Tree at {self.row}/{self.col}"


test = multi_dict(2, Tree)
test[1][1] = Tree(8, 9,10)


class Woods:
    def __init__(self) -> None:
        self.trees = multi_dict(2, Tree)

    def load(self, lines):
        self.width = len(lines[0])
        self.height = len(lines)
        print(f"Width: {self.width} Height: {self.height}")

        for row in range(0, self.height):
            for col in range(0, self.width):
                self.trees[row][col] = Tree(row, col, int(lines[row][col]))

    def getTree(self, row, col) -> Tree:
        return self.trees[row][col]

    def getTreeHeight(self, row, col) -> int:
        return self.trees[row][col].height

    def print(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                print(self.getTree(row, col), end='')
            print()

    def count_trees_for_slope(self, slope):
        return self.count_trees(slope[0], slope[1])

    def count_trees_for_slopes(self, slopes):
        trees = 1
        for slope in slopes:
            trees *= self.count_trees_for_slope(slope)
        return trees

    def findVisibleTreesToTheNorth(self, startRow, startCol):
        
        if startRow == 0:
            return 0
        trees = 0
        ourheight=self.getTreeHeight(startRow,startCol)
        print(f"Looking North for trees from {startRow}/{startCol} with height {ourheight}")
        for row in range(startRow-1, -1, -1):
            print(f"Checking {row}/{startCol} with height {self.getTreeHeight(row,startCol)}")
            trees += 1
            if self.getTreeHeight(row,startCol) >= ourheight:
                break
        return trees

    def findVisibleTreesToTheSouth(self, startRow, startCol):

        if startRow == self.height-1:
            return 0
        trees = 0
        ourheight=self.getTreeHeight(startRow,startCol)

        print(f"Looking South for trees from {startRow}/{startCol} with height {ourheight}")
        for row in range(startRow+1, self.height):
            print(f"Checking {row}/{startCol} with height {self.getTreeHeight(row,startCol)}")
            trees += 1
            if self.getTreeHeight(row,startCol) >= ourheight:
                break
            
        return trees

    def findVisibleTreesToTheEast(self, startRow, startCol):
        
        if startCol == self.width-1:
            return 0
        trees = 0
        ourheight=self.getTreeHeight(startRow,startCol)
        for col in range(startCol+1, self.width):
            trees += 1
            if self.getTreeHeight(startRow,col) >= ourheight:
                break
        return trees

    def findVisibleTreesToTheWest(self, startRow, startCol):
        
        if startCol == 0:
            return 0
        trees = 0
        ourheight=self.getTreeHeight(startRow,startCol)
        for col in range(startCol-1, -1, -1):
            trees += 1
            if self.getTreeHeight(startRow,col) >= ourheight:
                break
        return trees

    def calcScore(self, row, col):
        north = self.findVisibleTreesToTheNorth(row, col)
        print(f"Found {north} trees from {row}/{col} to the north")
        east = self.findVisibleTreesToTheEast(row, col)
        print(f"Found {east} trees from {row}/{col} to the east")
        south = self.findVisibleTreesToTheSouth(row, col)
        print(f"Found {south} trees from {row}/{col} to the south")
        west = self.findVisibleTreesToTheWest(row, col)
        print(f"Found {west} trees from {row}/{col} to the west")
        score = north*east*west*south
        return score


    def lookAround(self):
        
        maxscore = 0
        for row in range(0, self.height):
            for col in range(0, self.width):

                score = self.calcScore(row, col)
                if score > maxscore:
                    maxscore = score
                    print(f"New max score is tree {row,col} {maxscore}")
        
        print(f"Max score is {maxscore} ")

def main():
    woods = Woods()
    woods.load(lines)

    woods.lookAround()

    #print(woods.calcScore(1,2))
    #print(woods.calcScore(3,2))


if __name__ == "__main__":
    main()
