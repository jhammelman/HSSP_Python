# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for July 27th class (intro to pygame)

First a reminder on bools. Bools are a variable type that stores one of two values: **True** or **False**, with the exact capitalization as shown here. An example:

```python
takes_class = True
loves_code = True
if takes_class and loves_code:
   print("Glad you're having fun")
elif takes_class:
   print("Hopefully you can learn to like code")
elif loves_code:
   print("You should take our class")
else:
   print("You should take our class and learn to love code!")
```

We also talked about **while loops**.

while loops repeat something while their condition is True. For example, this will print hello 10 times.
```python
i = 1
while i <= 10:
      print("hello!")
      i = i + 1

```

We can also break out of the loop which is often useful in game-style programming, what will this example print?

```python
i = 1
while i <= 10:
      print(i)
      i = i+1
      if i == 5:
      	 break
```

```
1
2
3
4
```

It only prints the numbers 1 through 4 because we put a break statement when i gets to 5. 

#### New material

Today we will be learning about pygame. Pygame is a library which you can use to write games in python. Python has a lot of libraries for different purposes. To get a library we have to install it. Once a library is installed, we can tell our code we'll be using that library:

```python
import pygame
```

We'll also be using the time library to spawn new events:

```python
import time
```
Using pygame isn't that different from our text adventure game. One difference is that we write our main code in a **game loop**, which uses **while loops** and **Bools**.

```python
import pygame

pygame.init()

while True:
  # We will write anything we want to happen in game code here
  pygame.display.update() 
```

We update the display at the end of our while loop, which tells pygame to redraw our screen with any updates inside our loop
In any graphical game, we have a screen, and objects on the screen. In pygame we define these:

```python
import pygame

pygame.init()

# Define the screen
width = 640
height = 460
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
main_clock = pygame.time.Clock()

while True:
  # We will write anything we want to happen in game code here
  pygame.display.update() 

```
#### Coding instructions

Using the green button, download the code to your computer. Extract the folder saying yes to all the prompts. Inside the extracted HSSP_Python-master folder, drag the lesson4 folder to the desktop.

Find your terminal. It should already be up as a black screen on your computer, if it's not you can search the computer to open it.

Now type into the terminal:

```
cd ~/Desktop/lesson4
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