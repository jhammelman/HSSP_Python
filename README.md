# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for August 11th class (adding game and screen characters)

Today we will talk about how to customize a game. First we will review from last class.

###Review

####Lists
First we'll talk about **lists**. This is a new type of variable that can hold multiple things (called elements). We can make an empty list using brackets:
```python
mylist = []
```

We can make a list that has elements, separated by commas:
```python
mylist = ["item1","item2"] #this list has two strings inside it
```

We can add things to our list:

```python
backpack = []
backpack.append("key")
print(backpack) #list has one object, "key"
```

We can check how many things are inside our list:
```python
print(len(backpack)) #is 1
backpack.append("antidote")
print(backpack) #list has two objects, a key and an antidote
print(len(backpack)) #len(backpack) is 2
```

We can check if something is in our list:
```python
if "key" in backpack:
   print("You open the door with your key")
   if "antidote" not in backpack:
      print("The minute the door creaks open, a snake bites you. Since you don't have antidote you die.")
```

Lists can have items from any variable type: ints, floats, bools, strings, or lists!
```python
myintlist = [1,2,3]
myfloatlist = [1.0,1.1,1.2]
myboollist = [True,True,False]
mystringlist = ["item1","item2"]
mylistlist = [[1,2,3],[4,5,6]]
```

We can get specific elements from a list, by **indexing**. In python the first element in the list **starts at zero**:
```python
backpack = ["sword","snack","dragon egg"]
print(backpack[0]) #will print the first element, sword
print(backpack[1]) #will print the second element, snack
print(backpack[2]) #will print the third element, dragon egg
```

One very useful feature is to create a set of numbers (maybe you want a list of the numbers 1 through 10, we can get this using the **range** command:
```python
numbers1to10 = range(1,11)
print(numbers1to10) # this is a list of the numbers 1 through 10
```

Notice to get numbers 1 thorough 10, we actually have to tell the range we want the numbers starting at 1 and stopping before 11.

####For loops
We are adding **for** loops to our toolbox, in addition to **while** loops and **if** statements.

for loops iterate over a list, with a specific synatax:

```python
backpack = ["sword","snack","dragon egg"]
for item in backpack:
    print(item) 
```
We write the keyword **for**, then a **variable** where we will store the elements the the keyword **in**, then our list that we want to iterate over.


###Coding instructions
Using the green button, download this code to your computer. Extract the folder saying yes to all the prompts. Inside the extracted HSSP_Python-master folder, drag the lesson6 folder to the desktop. 

Type into the terminal the line below, responding **yes** to any prompts:
```
sudo apt-get install python-pygame
```

In the terminal type the following commands: 

```
cd ~/Desktop/lesson6

```
Drag just game.py file from last week from your flashdrive to the lesson6 folder on your Desktop. Check that the code is running the same as from last week by typing into the terminal: 

```
python game.py
```

Now we are moving on to adding characters to the screen. Open your game code:

```
gvim game.py
```

We are going to customize our game, this involves two steps:
1. loading custom images and 2. **blitting** images onto characters.

For setp one, add the following code beneath the set of lines that the define the screen:

```python
# Define the screen
width = 640
height = 460
screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
main_clock = pygame.time.Clock()

# New code for this class
background_image = pygame.image.load("space.jpg").convert_alpha()
background_image = pygame.transform.scale(background_image,(width,height))
```
This loads the image "space.jpg" and makes it the same size as the screen you defined with width and height.

Now inside your game loop and below the line we screen.fill, we replacethe following below the line where we draw our screen:
```python
screen.fill((255,255,255)) #draw screen
```
with a new line:
```python
#New code to add
screen.blit(background_image,(0,0)) #add background on screen
```

Test this is working by saving the code, then typing in the terminal:

```
python game.py
```

Your game should now have a space background.
Now we do the same for the player, first load the player image, in the line below where we loaded the background image. 
```python
player_image = pygame.image.load("spaceship.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (60, 60))
```

Now in the game loop, replace the line
```python
pygame.draw.rect(screen, (0,0,0), player) #draw player
```
with
```python
screen.blit(player_image,player)
```

When you test the code, a space ship should show up where our player was:
```
python game.py
```

Now slightly trickier we do this for the falling objects, add below where we defined

```python
#load a image for falling objects
object_image = pygame.image.load("asteroid.png").convert_alpha()
object_image = pygame.transform.scale(object_image, (50, 50))
```

and replace the lines:

```python
obj = pygame.draw.circle((screen), (0, 0, 0),
				 (obj.x, obj.y),
				 20, 1)
```
with the line:

```python
screen.blit(object_image,(obj.x,obj.y))
```

Now the falling objects should be asteroids. After this, call one of us over and we can help you to add your own images!!!