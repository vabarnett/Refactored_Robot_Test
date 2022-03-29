"""
A robot moves according to the following instructions:
 
F = move one unit forward
L = rotate 90 degrees anticlockwise
R = rotate 90 degree clockwise

with an input of instructions eg. 'LFRRFLLLF' calculate and return the minimum number of instructions
needed to return the robot to its starting point. The output should be an integer.
"""


#clean up instructions - produces a list with non-valid instructions removed
def cleanUp(directions):
    seperated = []
    for i in directions:
        if i in ["L","F","R"]:
            seperated.append(i)
    return seperated

def test_data_cleanup():
    assert cleanUp('LFxYZR') == ['L','F','R']
    assert cleanUp('RFL') == ['R', 'F', 'L']
    assert cleanUp('dhehrgrgr') == []
        
#calculate current direction

 
#calculate position on an x/y axis

#calculate moves to return to start