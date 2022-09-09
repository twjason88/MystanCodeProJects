"""
File: babygraphics.py
Name: Jason Hsu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

# Constant
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    spacing = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * spacing
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)  # The upper fixed line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)  # The lower fixed line
    for i in range(len(YEARS)):
        x_initial = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_initial, 0, x_initial, CANVAS_HEIGHT, width=LINE_WIDTH)  # The vertical lines
        canvas.create_text(x_initial + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)  # The year texts


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    n = 1  # The number of name drawn on the canvas
    for lookup_name in lookup_names:
        if n % len(COLORS) != 0:  # Select color based on the number of the name input
            color = COLORS[(n % len(COLORS)) - 1]
        else:
            color = COLORS[len(COLORS) - 1]
        n += 1
        x_initial = GRAPH_MARGIN_SIZE
        y_initial = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        for i in range(len(YEARS)):
            if i == 0:  # Set the first x, y values
                if str(YEARS[i]) in name_data[lookup_name]:
                    x_initial = GRAPH_MARGIN_SIZE
                    y_initial = GRAPH_MARGIN_SIZE + (int(name_data[lookup_name][str(YEARS[i])]) - 1) * ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)/1000)
                    canvas.create_text(x_initial + TEXT_DX, y_initial,
                                       text=f'{lookup_name} {name_data[lookup_name][str(YEARS[i])]}', anchor=tkinter.SW,
                                       fill=color)
                else:
                    x_initial = GRAPH_MARGIN_SIZE
                    y_initial = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x_initial + TEXT_DX, y_initial,
                                       text=f'{lookup_name} *', anchor=tkinter.SW, fill=color)
            else:
                if str(YEARS[i]) in name_data[lookup_name]:
                    x_end = get_x_coordinate(CANVAS_WIDTH, i)
                    y_end = GRAPH_MARGIN_SIZE + (int(name_data[lookup_name][str(YEARS[i])]) - 1) * ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)/1000)
                    canvas.create_text(x_end + TEXT_DX, y_end,
                                       text=f'{lookup_name} {name_data[lookup_name][str(YEARS[i])]}', anchor=tkinter.SW,
                                       fill=color)
                else:
                    x_end = get_x_coordinate(CANVAS_WIDTH, i)
                    y_end = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x_end + TEXT_DX, y_end,
                                       text=f'{lookup_name} *', anchor=tkinter.SW, fill=color)
                canvas.create_line(x_initial, y_initial, x_end, y_end, width=LINE_WIDTH, fill=color)
                x_initial = x_end
                y_initial = y_end


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
