#!/usr/bin/env python
print "You are standing in front of a black iron gate with rusty hinges and a large gold lock. Behind the gate stands an ominous castle, shrouded with clouds and with large gargoyles that cast creepy shadows onto the ground."
go_in = raw_input("Do you try to open the gate? (y or n) ")

if go_in is "y":
    print("You yank on the gate, but the large gold lock won't budge.")
    pick_lock = raw_input("Do you try to pick the lock? (y or n) ")
    # enter your if statement here to decide what happens if you try to pick the lock
    print("What happens? You decide...")    
elif go_in is "n":
    direction = raw_input("You decide to go home, but you've forgotten the way! Do you go left, right, or straight? (left,right,straight) ")
    if direction == "left":
        # enter your code here to continue the story
        print("What happens? You decide...")
    elif direction == "right":
        # enter your code here to continue the story
        print("What happens? You decide...")
    elif direction == "straight":
        # enter your code here to continue the story
        print("What happens? You decide...")
    else:
        print("Invalid input! You can't play :p")        
else:
    print("Invalid input! You can't play :p")

print("The End")
