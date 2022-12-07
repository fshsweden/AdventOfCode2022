"""
Pretty messy solution to AdventOfCode 2022 day 7 part 1

The solution is in two parts.
1)  Build a tree of directory() objects from a list of commands (cd and ls)
    The tree is built by interpreting the commands and adding directories and files
2)  Traverse the tree and collect the size of each directory

The quiz is to find the size of all directories that are smaller than 100000 bytes

There is room for optimisation since a dir X that is < 100000 bytes will also have all
subdirs < 100000 bytes.  This is not taken into account in the solution.

The quiz was a bit fuzzy on whether the root directory should be included in the result.
Also whether a parent dir < 100000 should be included in the result as well as the 
children in it. I do not know if this is a bug in the quiz or not.

"""
with open('test-input-7.txt') as f:
    lines = f.readlines()


curdir = "/"

class directory():

    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.children = []
        self.parent = parent

    def interpret_command(self, args):

        #print(f"WORKING WITH {self.name} {id(self)}")

        if args[0] == "cd":
            #print(f"cd to {args[1]}")
            if args[1] == "..":
                #print(f"Returning to {self.parent.name}")
                return self.parent
            else:
                if args[1][0] == '/':
                    #print(f"Absolute path {args[1]}")
                    return self  ## BUG
                else:
                    newdir = self.name + args[1] + "/"
                    #print(f"cd to path {newdir}")
                    tmp = self.add_dir(newdir)
                    return tmp

        elif args[0] == "ls":
            pass
        else:
            #print(f"Adding dir or file {args[0]} {args[1]}")
            self.add_dir_or_file(args[0],args[1])

        return self

    def add_dir_or_file(self, dir_or_size,name):
        if dir_or_size == "dir":
            # ignore
            pass
        else:
            #print(f"Adding dir or file {dir_or_size} {name}")
            self.add_file(dir_or_size, name)

    def add_dir(self, name):
        tmp = directory(name, self)
        #print(f"Adding directory {name} to children")
        self.children.append(tmp)
        return tmp

    def add_file(self, name, size):
        self.files.append((name, size))

    def print_with_tab(self, tab, what):
        for x in range(tab):
            print("    ",end='')
        print(what)

    def print(self, tab):

        self.print_with_tab(tab, f"- {self.name} (dir)")
        
        for c in self.children:
            # self.print_with_tab(tab, f" --- Diving into {c.name} ---")
            tab += 1
            c.print(tab)
            tab -= 1

        for f in self.files:
            # tuple with file name and size
            self.print_with_tab(tab, f"  - {f[1]} (file, size={f[0]})")

    def get_size(self, incl_subdirs=True):
        total = 0
        for f in self.files:
            #print(f"File: {f[0]} {f[1]}")
            total += int(f[0])
        #print("Total:", total)

        if incl_subdirs:
            for c in self.children:
                total += c.get_size()

        return total


    def get_dir_sizes(self):
        sizes = []
        for c in self.children:
            sizes.append((c.name, c.get_size()))
            sizes = sizes + c.get_dir_sizes()
        return sizes



root = d = directory("/")

for line in lines:
    args = line.strip().split(' ')
    if args[0] == '$':
        # this is a command
        d = d.interpret_command(args[1:])
    else:
        # this is a data line
        d.add_dir_or_file(args[0], args[1])        

# print("------------------------------------------")
# root.print(0)
#
#for dz in root.get_dir_sizes():
#   print(dz)

result = list(filter(lambda x: x[0] != "root" and x[1] <= 100000, root.get_dir_sizes()))
result = list(map(lambda x: x[1], result))
print(f"dirs with size < 100000: {result}")
print(f"sum of dirs with size < 100000: {sum(result)}")
print(f"total size: {root.get_size()}")
