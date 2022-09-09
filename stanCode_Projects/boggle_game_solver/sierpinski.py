"""
File: sierpinski.py
Name: Jason Hsu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draws a Sierpinski Triangle in a determined order.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	This function draws a Sierpinski Triangle.
	:param order: int, the integer decides the order of a triangle
	:param length: int, the length of a Sierpinski Triangle
	:param upper_left_x: int, the horizontal coordination of a Sierpinski Triangle
	:param upper_left_y: int, the vertical coordination of a Sierpinski Triangle
	:return: None
	"""
	if order == 1:  # Base Case!
		pass
	else:
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x+length//2, upper_left_y)
		window.add(line1)
		line2 = GLine(upper_left_x+length//2, upper_left_y, upper_left_x+length//2-(length//2)*0.5,
					  upper_left_y+(length//2)*0.866)
		window.add(line2)
		line3 = GLine(upper_left_x+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866, upper_left_x, upper_left_y)
		window.add(line3)
		line4 = GLine(upper_left_x+length//2, upper_left_y, upper_left_x+length//2+length//2, upper_left_y)
		window.add(line4)
		line5 = GLine(upper_left_x+length//2+length//2, upper_left_y,
					  upper_left_x+length//2+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866)
		window.add(line5)
		line6 = GLine(upper_left_x+length//2+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866, upper_left_x+length//2, upper_left_y)
		window.add(line6)
		line7 = GLine(upper_left_x+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866,
					  upper_left_x+length//2+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866)
		window.add(line7)
		line8 = GLine(upper_left_x+length//2+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866,
					  upper_left_x+length//2+length//2-(length//2)*0.5-(length//2)*0.5, upper_left_y+(length//2)*0.866+(length//2)*0.866)
		window.add(line8)
		line9 = GLine(upper_left_x+length//2+length//2-(length//2)*0.5-(length//2)*0.5, upper_left_y+(length//2)*0.866+(length//2)*0.866,
					  upper_left_x+length//2-(length//2)*0.5, upper_left_y+(length//2)*0.866)
		window.add(line9)
		pause(200)
		sierpinski_triangle(order-1, length//2, upper_left_x, upper_left_y)  # The triangle of the upper left one.
		sierpinski_triangle(order-1, length//2, upper_left_x+length//2, upper_left_y)
		# The triangle of the upper right one.
		sierpinski_triangle(order-1, length//2, upper_left_x+(length//2)*0.5, upper_left_y+(length//2)*0.866)
		# The triangle of the bottom one.


if __name__ == '__main__':
	main()