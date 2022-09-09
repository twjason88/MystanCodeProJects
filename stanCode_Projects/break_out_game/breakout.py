"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: Jason Hsu
-------------------------
This program creates a breakout game for users to remove all bricks!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    lives = NUM_LIVES
    while True:
        vx = graphics.get_initial_ball_vx()
        vy = graphics.get_initial_ball_vy()
        graphics.ball.move(vx, vy)  # Update

        graphics.reset_ball_velocity()  # Check
        if graphics.ball.y >= graphics.window.height:  # Reset ball position when moves out of the window
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)//2,
                                y=(graphics.window.height-graphics.ball.height)//2)
            lives -= 1
            if lives == 0:
                break

        graphics.collusion()  # Check
        if graphics.num == 0:  # When all bricks are knocked down
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) // 2,
                                y=(graphics.window.height - graphics.ball.height) // 2)
            break

        pause(FRAME_RATE)  # Pause


if __name__ == '__main__':
    main()
