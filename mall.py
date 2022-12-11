from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))


with open('input-9.txt') as f:
    lines = [row.strip() for row in f]



def main():
    pass

if __name__ == "__main__":
    main()
