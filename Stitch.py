import tkinter as tk
from tkinter import Canvas
import random, math

class Stitch(tk.Tk):
   #this is a setup function for tkinter canvas
   def __init__(self, vertical = 10, horizontal = 10):
      super().__init__()

      self.horizontal_line_length = vertical
      self.vertical_line_length = horizontal

      # Creates the canvas
      self.canvas = Canvas(background='white')
      self.canvas.pack(fill=tk.BOTH, expand=True)

      #running my functions
      self.createNumbers()
      self.createStitch()
      self.windowSize()

   def windowSize(self):
      #Setting the size of the window
      toplevelwindow = self.winfo_toplevel()
      toplevelwindow.wm_geometry(str(self.vertical_line_length * 10) + "x" + str(self.horizontal_line_length * 10))


   def createNumbers(self):
      # Set up the vertical and horizontal numbers.
      self.horizontal_numbers = []
      self.vertical_numbers = []

      #populates the preset horizontal and vertical number arrays with either a 1 or 0
      for horizontal in range(0, self.horizontal_line_length):
         self.horizontal_numbers.append(random.randrange(0,2))

      for vertical in range(0, self.vertical_line_length):
         self.vertical_numbers.append(random.randrange(0,2))


   def HorizontalLines(self, depth, start):
      for x in range(0, int(self.vertical_line_length/2)):
         points = [
            start,
            depth,
            start + 10,
            depth
         ]
         self.canvas.create_line(points, fill="black", width=2)
         start = start + 20

   def VerticalLines(self, depth, start):
      for x in range(0, int(self.horizontal_line_length/2)):
         points = [
            depth,
            start,
            depth,
            start + 10
         ]
         self.canvas.create_line(points, fill="black", width=2)
         start = start + 20

   def createStitch(self):
      # Checks if number is even or odd, if number is odd the Stitch will start with an offset of 10
      for index, value in enumerate(self.vertical_numbers):
         if value % 2 == 0:
            self.VerticalLines(index * 10, 0)
         else:
            self.VerticalLines(index * 10, 10)

      for index, value in enumerate(self.horizontal_numbers):
         if value % 2 == 0:
            self.HorizontalLines(index * 10, 0)
         else:
            self.HorizontalLines(index * 10, 10)


if __name__ == "__main__":
    sentence_clock = Stitch(40, 50)
    sentence_clock.mainloop()