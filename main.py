#!/usr/bin/env python3
from window import Window, Cell
from lines import Line, Point
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    result = maze.solve()
    if result == True:
        print("Maze was solved")
    else:
        print("Maze is not solvable")

    win.wait_for_close()

main()