# Game of Life
This project is an implementation of the famous Conway's Game of Life in Python using Pygame on a 10x10 grid. Each block represents a cell that will live or die according to the rules of life and depending on the inital position you as the player sets them in.

## Rules of Life
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

You can read more about the game and its intricacies [`here`](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Controls
Once you run the program, you can click on each cell in order to set it alive before starting the simulation. A grey cell is dead, and a white cell is alive. 

Once you are happy with your starting point. You can press the RETURN key in order to start and stop the simulation at your desired time. There is a delay of half a second on each iteration in order to allow you to see each change.

## Running the program
In order to run the program, simply run the following command:

```console
$ python3 main.py
```

## Dependencies

This project utilizes Python 3.9.7 which you can check by running:
```console
$ python3 --version
Python 3.9.7
```

Similarly, Pygame version 2.1.0 is utilized, which can be checked by running:

```console
$ pip3 show pygame
Name: pygame
Version: 2.1.0
Summary: Python Game Development
Home-page: https://www.pygame.org
Author: A community project.
Author-email: pygame@pygame.org
License: LGPL
Location: /Users/martinheberling/Library/Python/3.9/lib/python/site-packages
Requires: 
Required-by: 
```
