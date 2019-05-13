#!/usr/bin/env python3
import pyxel
from random_maze_generator import RandomMaze

SCREEN_WIDTH = 30
SCREEN_HEIGHT = 30
RIGHT, LEFT, UP, DOWN = (1,0), (-1,0), (0,-1), (0,1)
WHITE = 7
RED = 8
RUNNER_RADIUS = 0

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        pyxel.load('my_resource.pyxel')
        self.restart()
        pyxel.run(self.update, self.draw)

    def restart(self):
        self.maze = RandomMaze(SCREEN_HEIGHT)
        self.walls = self.maze.wall_coordinates()
        self.runner = self.maze.start
        self.end = self.maze.end

    def update(self):
        # check win
        if self.runner == self.end:
            pyxel.play(0, [0, 1, 2], loop=False)
            self.restart()
            return

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btnp(pyxel.KEY_G):
            self.restart()
            return
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self.move_if_possible(RIGHT)
        elif pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self.move_if_possible(LEFT)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.move_if_possible(UP)
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.move_if_possible(DOWN)

    def move_if_possible(self, direction):
        x, y = self.runner
        dx, dy = direction
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in self.walls:
            return
        if new_x < 0 or new_x >= SCREEN_WIDTH or new_y < 0 or new_y >= SCREEN_HEIGHT:
            return
        self.runner = (new_x, new_y)

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(*self.runner, RUNNER_RADIUS, RED)
        for (x, y) in self.walls:
            pyxel.rect(x, y, x, y, WHITE)


App()
