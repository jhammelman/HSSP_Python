# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for August 4th class (for loops and lists)

Today we will talk about  **lists** and **for** loops in python.

###Lists
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
mylist = []
mylist.append("item")
print(mylist) #list has one object, "item"
```

We can check how many things are inside our list:
```python
mylist = []
mylist.append("item1")
print(len(mylist)) #len(mylist) is 1
mylist.append("item2")
print(mylist) #list has two object, an item1 and item2
print(len(mylist)) #len(mylist) is 2
```

We can check if something is in our list:
```python
mylist = []
mylist.append("item1")
if "item1" in mylist:
   print("List contains item1")
if "item2" in mylist:
   print("List contains item2")
```
Only "List contains item1" will be printed because we didn't add item2 to our lists.

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
mylist = ["milk","juice","eggs"]
print(mylist[0]) #will print the first element, milk
print(mylist[1]) #will print the second element, juice
print(mylist[2]) #will print the third element, eggs
```

One very useful feature is to create a set of numbers (maybe you want a list of the numbers 1 through 10, we can get this using the **range** command:
```python
numbers1to10 = range(1,11)
print(numbers1to10) # this is a list of the numbers 1 through 10
```

Notice to get numbers 1 thorough 10, we actually have to tell the range we want the numbers starting at 1 and stopping before 11.

###For loops
We are adding **for** loops to our toolbox, in addition to **while** loops and **if** statements.

for loops iterate over a list, with a specific synatax:

```python
mylist = ["milk","juice","eggs"]
for item in mylist:
    print(item) 
```
We write the keyword **for**, then a **variable** where we will store the elements the the keyword **in**, then our list that we want to iterate over.


#### Coding instructions

Drag your lesson4 folder from your flashdrive to the desktop.

In the terminal type: 

```
cd ~/Desktop/lesson4

python game.py
```

You should see the code to control a player moving. This is a basic game loop, with a player that you can control with the left and right arrow keys. If this doesn't work, it may be that pygame isn't installed:

Type into the terminal:
```
sudo apt-get install python-pygame
```
and respond yes to any prompts.

But now try moving to the left. Eventually our character moves off the screen. How can we fix this? We attempted this last week.

Before moving on to this week's task, make sure your player can't move to the left or the right all the way off the screen. Open the code with:

```
gvim game.py
```

Remember our player's position can be checked with:

```python
player.left
player.right
player.top
player.botton
```

Ok now we will add falling objects to create an avoider-style game. Open your game.py code:
```
gvim game.py
```


After the line:

```python
# Define the player x,y,width,height
player = pygame.Rect(300,400,60,60)

```

Add a new line:

```python
all_objects = [] #empty objects list

```

Now directly below that line will add an object to the list:

```python
pos_x = 100 #x screen position
pos_y = -10 #y screen position make the circle off screen
obj = pygame.draw.circle((screen),(0,0,0),(pos_x,pos_y),20,0)
all_objects.append(obj) 
```

Now we actually have to draw these objects in our **game loop**, after the line:
```python
    pygame.draw.rect(screen, (0,0,0), player) #draw player
```
add the new lines:
```python
    for obj in all_objects:
    	obj.y += 3 # object is falling
	if obj.y >= height: #check if object off the screen
            obj.y = -10
        obj = pygame.draw.circle((screen), (0, 0, 0),
				 (obj.x, obj.y),
				 20,1)
```

If you run the code, you should see a circle fall from the top of the screen. On your own,
try adding a few more circles by appending them to the all_objects. Try varying the x and
y positions.

Now nothing happens currently if your player touches the circle. To make the player die if he hits a circle, we can add to our object for loop, under the line:
```python
     for obj in all_objects:
```
add:
```python
    #Test collisions with the bubbles
    if obj.colliderect(player):
       all_objects.remove(obj)
       pygame.quit()
       sys.exit()

```

You've made your first game! 