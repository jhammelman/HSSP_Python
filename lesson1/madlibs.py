#!/usr/bin/env python

print "------Correctly working program-------"
# There is a bug in this program with the
# variable names!
noun1 = raw_input("Give me a noun: ")

adjective = raw_input("Give me an adjective: ")

noun2 = raw_input("Give me a noun: ")

sentence = "After hiding the painting in his " + noun1 + " for two years, he grew " + adjective + " and tried to sell it to a/an " + noun2 + " in Florence, but was caught."

print sentence

print "------Bug with variables-------"
# There is a bug in this program with the
# variable names!
noun = raw_input("Give me a noun: ")

adjective = raw_input("Give me an adjective: ")

noun = raw_input("Give me a noun: ")

sentence = "After hiding the painting in his " + noun + " for two years, he grew " + adjective + " and tried to sell it to a/an " + noun + " in Florence, but was caught."

print sentence

print "------Bug with variables-------"
# Another common error is to rename a variable that
# python is already using, by writing raw_input =
# we are overwriting the function that python has
# for input, so we can no longer use it in this program
raw_input = raw_input("Give me a noun: ")

adjective = raw_input("Give me an adjective: ")

noun = raw_input("Give me a noun: ")

sentence = "After hiding the painting in his " + raw_input + " for two years, he grew " + adjective + " and tried to sell it to a/an " + noun + " in Florence, but was caught."

print sentencex
