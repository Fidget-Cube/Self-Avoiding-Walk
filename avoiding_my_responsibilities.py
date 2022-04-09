# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson

# Each index is a unique starting column, stores the weight of each
startTable = [0, 0.5, 1, 1, 2, 2.5, 1, 2, 2.5, 1.5, 2, 2, 2.5, 0.5, 1, 1, 2, 2.5, 1, 2, 2.5, 1.5, 2, 2, 2.5, 0.5, 1, 1, 1, 1, 1.5, 2, 1.5, 2]
# Transition table for each starting column (there are 27 states)
startTransitions = [0, 1, 0, 9, 9, 21, 10, 10, 20, 2, 0, 16, 3, 3, 0, 17, 17, 21, 12, 12, 23, 2, 0, 11, 1, 2, 0, 0, 16, 11, 1, 10, 3, 12]
# Transition from startTransitions to columns other than the starting column, incomplete 
mainTransitions =  [[], [0,1,2,3,4,5,6,17,19,20,22,24,25,27], [49,50,51,52,53,55,57,59,61,63], [8,9,10,11,12,14,36,38,39,41,43,44,46], 
                    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


# We define our coordinate system as a 3 by infinity grid,
# with starting point p at any point farthest left (0,-1) (0,0) (0,1)
# grid goes from (0,-1) to (inf,1)
# We will define a character of our language as a unique arrangement 
# of lines in a single column of the coordinate system. The set of 
# characters in the starting column is separate from the rest of the columns,
# and is dealt with separately.
# The first transition of our "DFA" involves reading in the start
# character and choosing a state based on the "output arrows".
# Every transition following that moves to a different one of these
# states.
# Every transition will also have a weight, depending on the number of
# arrows in the character involved in the transition.
class gridwalk:
    validSet = [] # In progress
    newSet = [] # In progress

    def __init__(self):
        # Each index in validSet represents a DFA state.
        # There are 27 states, each representing a possible set of paths between each column.
        # Each value of validSet is an array.
        # Each index of this array represents a weight.
        # Each value of this array represents the number of possible paths resulting in that weight.
        for i in range(27):
            self.validSet.append([0,0,0,0,0,0]) # Max starting weight = 2.5
        for i in range(len(startTable)):
            self.validSet[startTransitions[i]][int(startTable[i] * 2)] += 1
        print(self.validSet)
    

def main():
    walker = gridwalk()

if __name__ == "__main__":
    main()