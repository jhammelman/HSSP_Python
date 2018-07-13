# HSSP Introductory Python Programming through Games

This is a repository that holds the code for the Summer 2018 intro to python programming for MIT's HSSP program.

This code was developed for [Python](https://www.python.org/downloads/) (version 2.7).

Running the game templates and game example relies on the [Pygame](https://www.pygame.org/wiki/GettingStarted) library (version 1.9.3) which can be downloaded [here](https://www.pygame.org/download.shtml).

If you are looking to program without having to install Python on your computer, we recommend using the [www.learnpython.org](https://www.learnpython.org/) which is an interactive tutorial that covers many of the same topics as we will in the course.


## Instructions for July 14th class (If/Else statements)

Using the green button, download the code to your computer. Extract the folder saying yes to all the prompts. Inside the extracted HSSP_Python-master folder, drag the lesson 2 folder to the desktop.

Find your terminal. It should already be up as a black screen on your computer, if it's not use the search feature to open it.

Now type into the terminal:

```
cd ~/Desktop/lesson2
```

Remember that computers are picky, so all the characters should be the exact case and spacing.
Now we can run the code from inside the folder, type into the terminal:

```
python text_adventure_game.py 
```

Enter commands at the appropriate prompts. What happens if you don't follow the instructions? Try typing "yes" instead of "y".

Now we can take a look at the code. Type once again into the terminal

```
gvim text_adventure_game.py 
```

Now we can see there is an if statement based on the variable go_in which stores the users' response to opening the gate. What are the potential user responses? How does the computer respond? There is also an if statement if the user responds with a "y" to opening the gate.

