# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for July 21st class (while loops and booleans)

First a reminder on if statements. An if statement allows us to take different actions based on the value of a variable (in our case the user input). Python interprets any code that is *indented* beneath an if statement as happening if that statement is true. An example is:

```python
ans = raw_input("Do you want to play a game? ")
if ans == "yes":
   print("Great let's get started.")
elif ans == "no":
     print("OK maybe next time.")
else:
     print("Bad input!")
```

We can use this to create really in depth programs.


```python
ans = raw_input("Do you want to play a game? ")
if ans == "yes":
   print("Great let's get started.")
   ans = raw_input("There are three doors, one is red, one is blue and one is yellow, which do you open? (r,y,b) ")
   if ans == "r":
      print("Behind the red door is a red panda!")
   elif ans == "b":
      print("Behind the blue door is a dolphin!")
   elif ans == "y":
      print("Behind the yellow door is a giraffe!")
   else:
      print("Bad input!")
elif ans == "no":
     print("OK maybe next time.")
else:
     print("Bad input!")
```

We can keep adding if statements by indenting the text below the current if statement to keep the story going.

#### This week's new information

First we introduce a new variable type called a **bool**. It's simply a variable that stores one of two values: **True** or **False**, with the exact capitalization as shown here. An example:

```python
brushed_teeth = True
drank_juice = True
if brushed_teeth and drank_juice:
   print("That's disgusting")
elif drank_juice:
   print("Good vitamin C")
elif brushed_teeth:
   print("Good dental hygene")
else:
   print("You should brush your teeth and drink juice!")
```

Under the hood, our comparisons using ==,<=,>=,>,< that we covered last class get *evaluated* to become bool values of True or False.

```python
brushed_teeth = raw_input("Did you brush your teeth? ")
drank_juice = raw_input("Did you drink juice? ")
juice_taste_bad = brushed_teeth == "y" and drank_juice == "y"
```
The value of the variable juice_taste_bad is True if you drank juice and brushed your teeth and False otherwise


If you recall from last class, if the user gave wrong input they get kicked out of the game. This isn't very nice - what if they were close to the end? We want to let them re-type their input if they type the wrong thing. This is where the programming technique of loops can be useful. We will be covering **while loops**.

while loops repeat something while their condition is True. For example, this will print the numbers from 1 to 10.
```python
i = 1
while i <= 10:
      print(i)
      i = i + 1

```

We can also break out of the loop which is often useful in game-style programming, what will this example print?

```python
i = 1
while i <= 10:
      print(i)
      i = i + 1
      if i == 3:
      	 break
      print("stil counting...")
```

```
1
stil counting...
2
```

It only prints the numbers 1 and 2 because we put a break statement when i gets to 3. Also it only prints "still counting..." once because anything inside the while loop after the break statement won't happen. Literally the break statement leaves the loop at that exact point in the code.



#### Coding instructions

Using the green button, download the code to your computer. Extract the folder saying yes to all the prompts. Inside the extracted HSSP_Python-master folder, drag the lesson3 folder to the desktop.

Find your terminal. It should already be up as a black screen on your computer, if it's not you can search the computer to open it.

Now type into the terminal:

```
cd ~/Desktop/lesson3
```

Remember that computers are picky, so all the characters should be the exact case and spacing.
Now we can run the code from inside the folder, type into the terminal:

```
python text_adventure_game.py 
```

This is an empty template so you can start making your own text adventure game. We will use both if statements and while loops.

There are two ways to use while statements to make your code better which we talked about in the lesson

```python
ans = ""
while ans != "yes" and ans != "no":
   ans = raw_input("Do you want to play? (yes or no)")
   if ans == "yes":
      print("Great")
   elif ans == "no":
      print("to bad")
   else:
      print("bad input! please say yes or no")

```

```python
ans = “”
while True:
   ans = raw_input("Do you want to play? (yes or no)")
   if ans == "yes":
      print("Great")
      break
   elif ans == "no":
      print("to bad")
      break
   else:
      print("bad input! please say yes or no")
```

Now we can take a look at the code. Type once again go to the terminal

```
gvim text_adventure_game.py 
```

Try adding a while statement and an if statement to start your text adventure game. 