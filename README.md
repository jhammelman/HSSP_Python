# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for July 28th class (intro to pygame)

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

If we want to access commands and variables from that library we put pygame in front, for example:

```python
import pygame
pygame.display.set_mode((400,200))
```

This will set up a screen for our game.

We can also import specific parts of the pygame library, for example:

```python
from pygame.locals import *
```

Imports anything from pygame.locals which we will use to import testing key commands.

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

# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)

while True:
   # We will write anything we want to happen in game code here
   screen.fill((255,255,255)) #draw screen
   pygame.draw.rect(screen, (0,0,0), player) #draw player
   #Ensure constant frames/s
   main_clock.tick(50)

   pygame.display.update() 

```

You'll also notice we have some additional features. The **main_clock** variable is used to determine our frames/s for display.

Now pygame also has the ability to get commands from the keyboard:

```python
import pygame
import sys
from pygame.locals import *

pygame.init()

# Define the screen
width = 640
height = 460
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
main_clock = pygame.time.Clock()

# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)

player_speed=3
while True:
   # We will write anything we want to happen in game code here

   # Commands from keyboard
   for event in pygame.event.get():
       if event.type == QUIT:
       	  pygame.quit()
	  sys.exit()
       #check for pressing down on a key
       if event.type == KEYDOWN:
       	  if event.key == K_LEFT:
	     player.x -= player_speed
	  if event.key == K_RIGHT:
	     player.x += player_speed
   screen.fill((255,255,255)) #draw screen
   pygame.draw.rect(screen, (0,0,0), player) #draw player
   #Ensure constant frames/s
   main_clock.tick(50)

   pygame.display.update() 

```

#### Coding instructions

First we have to install pygame.

Find your terminal. It should already be up as a black screen on your computer, if it's not you can search the computer to open it.

Now type into the terminal:

```
sudo apt-get install python-pygame
```

Remember that computers are picky, so all the characters should be the exact case and spacing.
Now our first goal is to build a simple player controlled by arrow keys.

In the terminal type: 

```
cd ~/Desktop

gvim my_game.py
```

Start by writing this code to control a player moving. Reference earlier sections to understand how the code works:

```python
import pygame
import sys
from pygame.locals import *

pygame.init()

# Define the screen
width = 640
height = 460
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
main_clock = pygame.time.Clock()

# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)

player_speed=20
while True:
   # We will write anything we want to happen in game code here

   # Commands from keyboard
   for event in pygame.event.get():
       if event.type == QUIT:
       	  pygame.quit()
	  sys.exit()
       #check for pressing down on a key
       if event.type == KEYDOWN:
       	  if event.key == K_LEFT:
	     player.x -= player_speed
	  if event.key == K_RIGHT:
	     player.x += player_speed
   screen.fill((255,255,255)) #draw screen
   pygame.draw.rect(screen, (0,0,0), player) #draw player
   #Ensure constant frames/s
   main_clock.tick(50)

   pygame.display.update() 

```

One thing you will notice is if you hold down on the key, the player doesn't move. There is a way to fix this:

add the line to the beginning of your code before your game loop but after the imports and pygame.init()

```python
pygame.key.set_repeat(100,50)
```

Now when keys are held down they will generate multiple pygame.KEYDOWN events so we will move.

But now try moving to the left. Eventually our character moves off the screen. How can we fix this? Brainstorm with a neighbor.

Try modifying the code so that our character can't move off the screen.



