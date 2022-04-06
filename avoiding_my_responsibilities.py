# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson

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
    # Each set contains a state mapped to a weight
    # The weight is the collective weight of every
    # transition that led to that particular state
    validSet = [] # In progress
    newSet = [] # In progress

    def __init__(self):
        self.validSet # Fill the first valid set with weights according to the starting table
    

def main():
    walker = gridwalk()

if __name__ == "__main__":
    main()