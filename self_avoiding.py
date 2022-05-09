# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson
import sys

# We define our coordinate system as a 3 by infinity grid,
# with starting point p at any point farthest left (0,-1) (0,0) (0,1)
# grid goes from (0,-1) to (inf,1)
class gridwalk:
    validSet = [] # Number of valid walks already determined for n
    newSet = [] # Number of valid walks being determined for n+1

    def __init__(self):
        self.validSet += [[(0,-1)],[(0,0)],[(0,1)]] # Start by filling the valid set with all walks of length 0
    
    # Count the number of self-avoiding walks of length n possible given the coordinate system
    def count(self, n):
        for i in range(n):
            for walk in self.validSet:
                tests = [
                    walk + [(walk[-1][0] + 1,walk[-1][1])],
                    walk + [(walk[-1][0] - 1,walk[-1][1])],
                    walk + [(walk[-1][0],walk[-1][1] + 1)],
                    walk + [(walk[-1][0],walk[-1][1] - 1)]
                ]
                for test in tests:
                    if self.checkWalk(test):
                        self.newSet.append(test)
            self.validSet = self.newSet[:]
            self.newSet = []
        return len(self.validSet)
    
    # Check a walk to see if it is within the coordinate range and self-avoiding
    def checkWalk(self, walk):
        if walk[-1][1] > 1 or walk[-1][1] < -1 or walk[-1][0] < 0:
            return False
        if walk[-1] in walk[:-1]:
            return False
        return True

def main():
    args = sys.argv[1:]
    walker = gridwalk()
    result = walker.count(int(args[0]))
    print(result)

if __name__ == "__main__":
    main()