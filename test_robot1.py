"""
A robot moves according to the following instructions:
 
F = move one unit forward
L = rotate 90 degrees anticlockwise
R = rotate 90 degree clockwise

with an input of instructions eg. 'LFRRFLLLF' calculate and return the minimum number of instructions
needed to return the robot to its starting point. The output should be an integer.
"""

#clean up instructions
def cleanUp(directions):
    return ['L','F','R']


#calculate current direction

def test_data_cleanup():
    assert cleanUp('LFxYZR') == ['L','F','R']
        


 
#calculate position on an x/y axis

#calculate moves to return to start