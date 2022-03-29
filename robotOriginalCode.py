""" This is the original solution to the problem written under time pressure with the instructions to write 
'quick and dirty' but working code. Being written within a hosted environment it was subject to tests online, 
but I tested it manually in my code editor as I went.  """


def solution(directions):
    seperated = []#list of seperated instructions, minus incorrect chars
    direction = 0 #counts numbers of turns +1 for clockwise, -1 for anti clockwise
    new_dir = "n" # letter to represent compass direction at present
    compass = ["n","e","s","w"] # possible directions of the compass
    #current coordinates of robot
    x = 0
    y = 0
    instructions = 0 #count of number of instructions required to return to original position
    
    #creates seperated list of instructions
    for i in directions:
        if i in ["L","F","R"]:
            seperated.append(i)
            
    #sets direction    
    for elem in seperated:
        if elem == "R":
            direction += 1
            new = direction % 4       
            new_dir = (compass[new])
            
        elif elem == "L":
            direction -= 1
            new = direction %4       
            new_dir = (compass[new])
            
        #increases x and y to find current position
        elif elem == "F":
            if new_dir == "e":
                x += 1
            elif new_dir == "s":
                y -= 1  
            elif new_dir == "w":
                x -= 1
            elif new_dir == "n":
                y += 1
    
    #calculates number of turn instructions and move instructions depending on current direction and distance            
    if (x!=0) and (y!=0): #for numbers not on axis
        if (x > 0) and (y > 0):#top right quadrant
            if (new_dir == "n") or (new_dir == "e"):
                instructions += 2
                instructions += abs(x)
                instructions += abs(y)
            elif (new_dir == "s") or (new_dir == "w"):
                instructions += 1
                instructions += abs(x)
                instructions += abs(y)
        elif (x < 0) and (y < 0):#bottom left quadrant
            if (new_dir == "w") or (new_dir == "s"):
                instructions += 2
                instructions += abs(x)
                instructions += abs(y)
            elif (new_dir == "e") or (new_dir == "n"):
                instructions += 1
                instructions += abs(x)
                instructions += abs(y)
        elif (x > 0) and (y < 0):#bottom right quadrant
            if (new_dir == "e") or (new_dir == "s"):
                instructions += 2
                instructions += abs(x)
                instructions += abs(y)
            elif (new_dir == "w") or (new_dir == "n"):
                instructions += 1
                instructions += abs(x)
                instructions += abs(y)
        elif (x < 0) and (y > 0):#top left quadrant
            if (new_dir == "w") or (new_dir == "n"):
                instructions += 2
                instructions += abs(x)
                instructions += abs(y)
            elif (new_dir == "e") or (new_dir == "s"):
                instructions += 1
                instructions += abs(x)
                instructions += abs(y)
    elif (x==0) and (y==0):#if robot is already in starting position
        instructions = 0
    elif (x==0) and (y!=0):#if on y axis
        if y>0:
            if (new_dir=="n"):
                instructions += 2
                instructions += abs(y)
            elif (new_dir=="e") or (new_dir=="w"):
                instructions += 1
                instructions += abs(y)
            elif (new_dir=="s"):
                instructions += abs(y)
        elif y<0:
            if (new_dir=="s"):
                instructions += 2
                instructions += abs(y)
            elif (new_dir=="e") or (new_dir=="w"):
                instructions += 1
                instructions += abs(y)
            elif (new_dir=="n"):
                instructions += abs(y)
    elif (y==0) and (x!=0):#if on x axis
        if x>0:
            if (new_dir=="e"):
                instructions += 2
                instructions += abs(y)
            elif (new_dir=="n") or (new_dir=="s"):
                instructions += 1
                instructions += abs(y)
            elif (new_dir=="w"):
                instructions += abs(y)
        elif x<0:
            if (new_dir=="w"):
                instructions += 2
                instructions += abs(y)
            elif (new_dir=="n") or (new_dir=="s"):
                instructions += 1
                instructions += abs(y)
            elif (new_dir=="e"):
                instructions += abs(y)
        
    print(x,y,new_dir,instructions)

solution("RF")

        
    
    
    
    

