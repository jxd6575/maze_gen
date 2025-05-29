from tkinter import Tk, BOTH, Canvas
from lines import Line, Point

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="White", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False


    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, y1, x2, y2):

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win == None:
            return
        if self.has_left_wall == True:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(l, "black")
        if self.has_right_wall == True:
            l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "black")
        if self.has_top_wall == True:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(l, "black")
        if self.has_bottom_wall == True:
            l = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "black")
        if self.has_left_wall == False:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(l, "white")
        if self.has_right_wall == False:
            l = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "white")
        if self.has_top_wall == False:
            l = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(l, "white")
        if self.has_bottom_wall == False:
            l = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(l, "white")
    
    def draw_move(self, to_cell, undo=False):

        half_length = abs(self.__x2 - self.__x1) // 2
        center_self_x = half_length + self.__x1
        center_self_y = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        center_to_cell_x = half_length2 + to_cell.__x1
        center_to_cell_y = half_length2 + to_cell.__y1
        if self.__win == None:
            return
        fill_color = "red"
        if undo:
            fill_color = "gray"
        line = Line(Point(center_self_x, center_self_y), Point(center_to_cell_x, center_to_cell_y))
        self.__win.draw_line(line, fill_color)
        

