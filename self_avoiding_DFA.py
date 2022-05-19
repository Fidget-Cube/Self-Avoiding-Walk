# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson
import sys

# Each index is a unique starting column, stores the weight of each
startTable = [0, 0.5, 1, 1, 2, 2.5, 1, 2, 2.5, 1.5, 2, 2, 2.5, 0.5, 1, 1, 2, 2.5, 1, 2, 2.5, 1.5, 2, 2, 2.5, 0.5, 1, 1, 1, 1, 1.5, 2, 1.5, 2]
# Transition table for each starting column (there are 13 valid states)
startTransitions = [0, 1, 0, 4, 4, 12, 5, 5, 10, 2, 0, 8, 3, 3, 0, 9, 9, 12, 7, 7, 11, 2, 0, 6, 1, 2, 0, 0, 8, 6, 1, 5, 3, 7]
# Transition from startTransitions to columns other than the starting column, incomplete 
mainTransitions =  [[], [0,1,2,3,4,6,17,19,20,22,24,25,27], [49,50,51,52,53,55,57,59,61,63], [8,9,10,11,12,14,36,38,39,41,43,44,46], 
                    [5,18,26], [7,21,23,28], [54,58,64], [15,40,42,47], [56,60,62], [13,37,45], [35,65], [34,66], [16,29,30,31,32,33,48]]
# Stores the weight of each standard column (0-66)
columnTable       =  [0.5,1,1.5,2,2.5,2,3,3,0.5,1,1.5,2,2.5,2,3,3,2.5,1.5,2,2.5,3,3,1.5,2,2.5,3,3,2.5,3,2.5,3,2.5,2.5,3,2.5,2.5,1.5,2,
                      2.5,3,3,1.5,2,2.5,3,3,2.5,3,3,0.5,1,1.5,1.5,2,2,2,2,1.5,2,1.5,2,2.5,3,2.5,3,3,3]
# Transition table for each standard column (there are 13 valid states)
endTransitions = [0,1,0,2,0,0,3,0,0,3,0,2,0,0,1,0,0,4,4,4,12,4,5,5,5,10,5,8,8,0,3,9,4,12,7,5,9,9,9,12,9,7,7,7,11,7,6,6,1,0,2,0,0,1,0,3,0,6,6,8,8,5,5,7,7,10,11]


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
    length = 0
    validSet = [] # In progress
    newSet = [] # In progress

    def __init__(self, length):
        # Each index in validSet represents a DFA state.
        # There are 13 states (not counting the start state), each representing a possible set of paths between each column.
        # Each value of validSet is an array.
        # Each index of this array represents a weight.
        # Each value of this array represents the number of possible paths resulting in that weight.
        if self.length < 0:
            return "Invalid Length"
        else:
            self.length = length
            for i in range(13):
                self.validSet.append([0 for it in range((length * 2) + 1)]) # Max weight we care about = length of target walk
            for i in range(len(startTable)):
                if startTable[i] <= self.length:
                    self.validSet[startTransitions[i]][int(startTable[i] * 2)] += 1
    
    # Calculates the number of valid walks of length "length"
    def walk(self):
        if self.length == 0:
            return 3
        runningTotal = 0
        # Our oracle here is validSet[0], which is the final state of the DFA
        # Everything ending at validSet[0] with length "length" is a walk we want to count
        runningTotal += self.validSet[0][self.length * 2]
        # We continue this until there is no weight <= length * 2 in the final state.
        while True:
            self.updateSet()
            flag = False
            for i in self.validSet[0]:
                if i != 0:
                    flag = True
            if flag == False: 
                break
            runningTotal += self.validSet[0][self.length * 2]

        return runningTotal
    
    # Simulates the reading in of a new character, and updates validSet.
    def updateSet(self):
        self.nextSet = []
        for i in range(13):
            self.nextSet.append([0 for it in range((self.length * 2) + 1)])
        for i in range(len(self.validSet)):
            for j in range(len(self.validSet[i])):
                for k in range(len(mainTransitions[i])):
                    weight = columnTable[mainTransitions[i][k]] # The weight of the transition
                    if (j / 2) + weight <= self.length:           # We only care about counting weights up to the desired walk length
                        index = endTransitions[mainTransitions[i][k]] # The state index that the transition leads to
                        self.nextSet[index][int(j + (weight * 2))] += self.validSet[i][j]
        self.validSet = self.nextSet[:]



def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Format: python3 self_avoiding_DFA.py <length>")
    walker = gridwalk(int(args[0]))
    count = walker.walk()
    print(count)

if __name__ == "__main__":
    main()