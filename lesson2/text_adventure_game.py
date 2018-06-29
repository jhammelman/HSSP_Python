#!/usr/bin/env python
import time

print "You are standing in front of a black iron gate with rusty hinges and a large gold lock. Behind the gate stands an ominous castle, shrouded with clouds and with large gargoyles that cast creepy shadows onto the ground."
go_in = raw_input("Do you try to open the gate? (y or n) ")

if go_in == "y":
    print "You yank on the gate, but the large gold lock won't budge."
    pick_lock = raw_input("Do you try to pick the lock? (y or n) ")
    
if go_in == "n":
    print "You decide to go home."
    
