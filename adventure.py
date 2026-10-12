print("=======================================================================================================")
print("                                     THE TEMPLE GAME                                                   ")
print("=======================================================================================================")

print("in this game you will be given some choices and lets see what your fate is ")
print()

start=input("please enter start whenever you are ready to start=").lower()

while start not in ["start"] :
    print("invalid respone")
    start=input("please enter start whenever you are ready to start=").lower()
print()

print("=======================================================================================================")
print("                                           STORY                                                       ")
print("=======================================================================================================")

print("you are a treasure hunter and you have been given a map to find the treasure in the temple.")
print("so you go to the temple and you are at the entrance of the temple and you have to make a choice.")
print("on left side there is the entrance to the temple and on right side there is a dark cave which you can enter.")
print()
print("you have to make a choice, you can either go left or right.")

choice=input("please enter left or right to make your choice=").lower()

while choice not in ["left","right"] :
    print("invalid respone")
    choice=input("please enter left or right to make your choice=").lower()

if choice=="left":

    print("you have entered the temple, there is a big yard and there is a door in front of you with a lock on it")
    print("you have to guess a pattern to unlock the door and enter the temple.")
    print("there are four shapes in the pattern, you have to click the shapes in the correct order to unlock the door.")
    print("the shapes are: square, circle, triangle.")
    print("there are three huts in the yard, each hut has a shape on these door, you have to go to the huts and find the position of the shape and click the shapes in the correct order to unlock the door.")
    print()
    print("which hut will you go in first")

    choice=input("please enter the shape which is on the hut you wish to go in first=")

    while choice not in ["square","circle","triangle"] :
        print("invalid respone")
        choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()

    if choice=="square" :
        print("you have entered the hut with the square shape on the door, you see a note on the table which has a riddle on it, you have to solve the riddle to find the position of the square shape in the pattern.")
        print("the note says")
        print()
        print("The Riddle of the Forgotten Guardian I am the number of shadows cast by a single flame when reflected between two mirrors facing one another.I stand between the beginning and the end of a trio, yet I am not the first nor the last.Remove one from me, and I become nothing more than a lonely beginning.What number am I?")
        print()
        print("now you have to go to other two huts")
        print("which hut you wish to go in : circle or triangle")
        
        choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        while choice not in ["circle","square","triangle"] :
            print("invalid respone")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        for choice in ["square"] :
            print("you are already in the room")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        if choice=="circle" :
            print("you have entered the hut with the circle shape on the door, you see a note on the table which has a riddle on it, you see a safe in front of you, you have to put a code in the safe to open it")
            print("you search the hut and you find a note which has a code on it, 3009")
            print("you go to the safe and put a code")

            code=int(input("please enter the code to open the safe="))

            while code not in [3009] :
                print("invalid code")
                code=int(input("please enter the code to open the safe="))
            print()
            
            if code==3009 :
                print("the safe opens and you find a note which says 1, the position of the circle perhaps?")
        
        else :
            print("you have entered the hut with the triangle shape on the door.")
            print("the door behind shuts and you see three enormous statues standing before you. Suddenly, all three statues begin to glow faintly in the darkness.")
            print("A deep, ancient voice echoes through the room:")
            print()
            print("I am the final guardian, yet I am not the end. I stand after two, but before four. I am the number carved upon the triangle's fate. Speak my name, and the hidden clue shall awaken.")
            print()
            print("You look closely at the statues. The middle statue slowly raises its arm and points towards a stone pedestal.")
            print("A small inscription appears on the pedestal:")
            print()
            
            num=int(input("Enter the number you seek"))
                
            while num not in [3] :
                print("the ancient voice echoes through the room again")
                print("you have entered the wrong number, think again and answer correctly")
                num=int(input("Enter the number you seek"))
            
            if num==3 :
                print("The pedestal glows, the ancient voice echoes through the room again")
                print("the number which you entered is the position of the triangle.")
                print("the door opens")
        
    elif choice=="circle" :
        print("you have entered the hut with the circle shape on the door, you see a note on the table which has a riddle on it, you see a safe in front of you, you have to put a code in the safe to open it")
        print("you search the hut and you find a note which has a code on it, 3009")
        print("you go to the safe and put a code")
    
        code=int(input("please enter the code to open the safe="))

        while code not in [3009] :
            print("invalid code")
            code=int(input("please enter the code to open the safe="))
        
        print()
        
        if code==3009 :
            print("the safe opens and you find a note which says 1, the position of the circle perhaps?")
        
        print()
        print("now you have to go to other two huts")
        print("which hut you wish to go in : square or triangle")
        
        choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        while choice not in ["circle","square","triangle"] :
            print("invalid respone")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        for choice in ["circle"] :
            print("you are already in the room")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        if choice=="square" :
            print("you have entered the hut with the square shape on the door, you see a note on the table which has a riddle on it, you have to solve the riddle to find the position of the square shape in the pattern.")
            print("the note says")
            print()
            print("The Riddle of the Forgotten Guardian I am the number of shadows cast by a single flame when reflected between two mirrors facing one another.I stand between the beginning and the end of a trio, yet I am not the first nor the last.Remove one from me, and I become nothing more than a lonely beginning.What number am I?")
            print()
        
        else :
            print("you have entered the hut with the triangle shape on the door.")
            print("the door behind shuts and you see three enormous statues standing before you. Suddenly, all three statues begin to glow faintly in the darkness.")
            print("A deep, ancient voice echoes through the room:")
            print()
            print("I am the final guardian, yet I am not the end. I stand after two, but before four. I am the number carved upon the triangle's fate. Speak my name, and the hidden clue shall awaken.")
            print()
            print("You look closely at the statues. The middle statue slowly raises its arm and points towards a stone pedestal.")
            print("A small inscription appears on the pedestal:")
            print()
            
            num=int(input("Enter the number you seek"))    
            
            while num not in [3] :
                print("the ancient voice echoes through the room again")
                print("you have entered the wrong number, think again and answer correctly")
                num=int(input("Enter the number you seek"))
            
            if num==3 :
                print("The pedestal glows, the ancient voice echoes through the room again")
                print("the number which you entered is the position of the triangle.")
                print("the door opens")
     
    else :
        print("you have entered the hut with the triangle shape on the door.")
        print("the door behind shuts and you see three enormous statues standing before you. Suddenly, all three statues begin to glow faintly in the darkness.")
        print("A deep, ancient voice echoes through the room:")
        print()
        print("I am the final guardian, yet I am not the end. I stand after two, but before four. I am the number carved upon the triangle's fate. Speak my name, and the hidden clue shall awaken.")
        print()
        print("You look closely at the statues. The middle statue slowly raises its arm and points towards a stone pedestal.")
        print("A small inscription appears on the pedestal:")
        print()

        num=int(input("Enter the number you seek"))
        
        while num not in [3] :
            print("the ancient voice echoes through the room again")
            print("you have entered the wrong number, think again and answer correctly")
            
            num=int(input("Enter the number you seek"))

        if num==3 :
            print("The pedestal glows, the ancient voice echoes through the room again")
            print("the number which you entered is the position of the triangle.")
            print("the door opens")
        
        print()
        print("now you have to go to other two huts")
        print("which hut you wish to go in : square or circle")
        
        choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        while choice not in ["circle","square","triangle"] :
            print("invalid respone")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        for choice in ["triangle"] :
            print("you are already in the room")
            choice=input("please enter square, circle or triangle to choose the hut you want to go in first=").lower()
        
        if choice=="square" :
            print("you have entered the hut with the square shape on the door, you see a note on the table which has a riddle on it, you have to solve the riddle to find the position of the square shape in the pattern.")
            print("the note says")
            print()
            print("The Riddle of the Forgotten Guardian I am the number of shadows cast by a single flame when reflected between two mirrors facing one another.I stand between the beginning and the end of a trio, yet I am not the first nor the last.Remove one from me, and I become nothing more than a lonely beginning.What number am I?")
            print()
        
        else :
            print("you have entered the hut with the circle shape on the door, you see a note on the table which has a riddle on it, you see a safe in front of you, you have to put a code in the safe to open it")
            print("you search the hut and you find a note which has a code on it, 3009")
            print("you go to the safe and put a code")
            
            code=int(input("please enter the code to open the safe="))
            
            while code not in [3009] :
                print("invalid code")
                code=int(input("please enter the code to open the safe="))
                print()
            if code==3009 :
                print("the safe opens and you find a note which says 1, the position of the circle perhaps?")
        
