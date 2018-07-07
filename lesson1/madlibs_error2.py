print("------Bug 2-------")
# Another common error is to rename a variable that
# python is already using, by writing raw_input =
# we are overwriting the function that python has
# for input, so we can no longer use it in this program
raw_input = raw_input("Give me a noun: ")

adjective = raw_input("Give me an adjective: ")

noun = raw_input("Give me a noun: ")

sentence = "After hiding the painting in his " + raw_input + " for two years, he grew " + adjective + " and tried to sell it to a/an " + noun + " in Florence, but was caught."

print(sentence)
