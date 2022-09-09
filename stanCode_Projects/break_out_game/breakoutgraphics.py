"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File: breakoutgraphics.py
Name: Jason Hsu
-------------------------
This program designs the background objects and functions needed to create a breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.num = BRICK_COLS * BRICK_ROWS  # Calculate the total number of bricks

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-paddle_offset-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)//2, y=(self.window.height-self.ball.height)//2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)  # Control the mouse's movement

        onmouseclicked(self.set_initial_ball_velocity)  # Control when to let the ball move

        # Draw bricks
        n = brick_rows // 5  # Assign the number of the rows of bricks that are grouped together with the same color
        self.color = 'red'  # The initial color
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = self.color
                self.brick.color = self.color
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing) + brick_offset)
                if (i+1) % n == 0:
                    if j == brick_cols - 1:  # Check when to change the color
                        self.change_brick_color()

    def change_brick_color(self):
        # Change bricks' color based on a particular manner
        if self.color == 'red':
            self.color = 'gold'
        elif self.color == 'gold':
            self.color = 'yellow'
        elif self.color == 'yellow':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'blue'
        elif self.color == 'blue':
            self.color = 'red'

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x <= 0:  # Set a left boundary to prevent paddle from moving out of the window
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= self.window.width:
            # Set a right boundary to prevent paddle from moving out of the window
            self.paddle.x = self.window.width - self.paddle.width

    def set_initial_ball_velocity(self, _):
        if self.__dx == 0 and self.__dy == 0:  # Create a boundary to let mouse clicking work
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() >= 0.5:
                self.__dx = -self.__dx

    def reset_ball_velocity(self):
        # Velocity changes when the ball colludes with window's boundaries
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.ball.y >= self.window.height:  # The condition when player loses and the ball's velocity returns to 0
            self.__dx = 0
            self.__dy = 0

    def get_initial_ball_vx(self):
        # Due to the private variables, we need to get attributes' values from coder site
        return self.__dx

    def get_initial_ball_vy(self):
        # Due to the private variables, we need to get attributes' values from coder site
        return self.__dy

    def collusion(self):
        #  The ball colludes with objects
        switch = False  # Set a switch to control when to break the for loop
        for i in range(self.ball.x, self.ball.x + self.ball.width+1, self.ball.width):
            if not switch:
                for j in range(self.ball.y, self.ball.y + self.ball.height+1, self.ball.height):
                    maybe_object = self.window.get_object_at(i, j)
                    if maybe_object is not None:
                        if maybe_object is self.paddle:
                            self.paddle_v_change()
                        else:  # When contacting with a brick
                            self.brick_v_change()
                            self.window.remove(maybe_object)
                            self.num -= 1
                        switch = True  # Close the switch
                        break
            else:
                break

    def paddle_v_change(self):
        # Velocity change when contacting with paddle
        if self.__dy > 0:  # Set a boundary to prevent the ball from bouncing when contacting with the paddle
            self.__dy = -self.__dy

    def brick_v_change(self):
        # Velocity change when contacting with bricks
        self.__dy = -self.__dy


