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

    def lookEastFrom(self, row, col):

        startRow=row
        startCol=col
        trees = 1
        highest = self.getTreeHeight(row,col)
        self.getTree(row,col).visible_from_west = True
        startCol += 1

        for col in range(startCol, self.width):
            #print(f"Looking at Tree {row}/{col}")
            if self.getTreeHeight(row,col) > highest:
                #print(f"Found a tree {row}/{col} that is higher than {highest}")
                self.getTree(row,col).visible_from_west = True
                trees += 1
                highest = self.getTreeHeight(row,col)
            
        #print(f"Found {trees} trees Looking east from {startRow}/{startCol}")
        return trees

    def lookSouthFrom(self, row, col):

        startRow=row
        startCol=col
        trees = 1
        highest = self.getTreeHeight(row,col)
        self.getTree(row,col).visible_from_north = True
        startRow += 1

        for row in range(startRow, self.height):
            #print(f"Looking at Tree {row}/{col}")
            if self.getTreeHeight(row,col) > highest:
                #print(f"Found a tree {row}/{col} that is higher than {highest}")
                self.getTree(row,col).visible_from_north = True
                trees += 1
                highest = self.getTreeHeight(row,col)
            
        #print(f"Found {trees} trees Looking east from {startRow}/{startCol}")
        return trees

    def lookWestFrom(self, row, col):

        startRow=row
        startCol=self.width-1
        trees = 1
        highest = self.getTreeHeight(row,col)
        self.getTree(row,col).visible_from_east = True
        startCol -= 1

        for col in range(startCol, 0, -1):
            #print(f"Looking at Tree {row}/{col}")

            if self.getTreeHeight(row,col) > highest:

                #print(f"Found a tree {row}/{col} that is higher than {highest}")

                self.getTree(row,col).visible_from_east = True
                trees += 1
                highest = self.getTreeHeight(row,col)
            
        #print(f"Found {trees} trees Looking west from {startRow}/{startCol}")
        return trees

    def lookNorthFrom(self, row, col):

        startRow=self.height-1
        startCol=col
        trees = 1
        highest = self.getTreeHeight(row,col)
        self.getTree(row,col).visible_from_south = True
        startRow -= 1

        for row in range(startRow, 0, -1):
            #print(f"Looking at Tree {row}/{col}")
            if self.getTreeHeight(row,col) > highest:
                #print(f"Found a tree {row}/{col} that is higher than {highest}")
                self.getTree(row,col).visible_from_north = True
                trees += 1
                highest = self.getTreeHeight(row,col)
            
        #print(f"Found {trees} trees Looking east from {startRow}/{startCol}")
        return trees

    def lookIntoWoodFromEdges(self):

        for row in range(0, self.height):
            self.lookEastFrom(row, 0)

        for row in range(0, self.height):
            self.lookWestFrom(row, self.width -1)

        for col in range(0, self.width):
            self.lookSouthFrom(0, col)

        for col in range(0, self.width):
            self.lookNorthFrom(self.height-1, col)

        visible_count = 0
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.getTree(j,i).isVisible():
                    # print(f"Tree {j}/{i} is visible")
                    visible_count += 1
        return visible_count

def main():
    woods = Woods()
    woods.load(lines)

    print(woods.lookIntoWoodFromEdges())

if __name__ == "__main__":
    main()
