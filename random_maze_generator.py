import random

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class RandomMaze:
    """
    start : coordinate (x, y) must be on the border
    end : coordinate (x, y) must be on the border
    board: a 2D board, for simplicity of the problem, lets assure it is a nxn square
    """
    def __init__(self, n):
        self.board = [[" "] * n for _ in range(n)]
        self.walls = set()
        self.n = n
        self.start = self.random_on_border()
        self.end = self.random_on_border()
        while self.start == self.end:
            end = self.random_on_border()
        self.random_maze()

    def random_maze(self):
        board, walls, start, end = self.board, self.walls, self.start, self.end
        if not board or not board[0]:
            return
        n = len(board)
        self.draw_border()

        while walls:
            x, y, dir = walls.pop()
            dx, dy = DIRECTIONS[dir]
            for delta in range(1, n):
                nx, ny = x + dx * delta, y + dy * delta
                if not self.valid_to_wall(nx, ny, dir):
                    break
            if delta == 1:
                continue
            randdelta = random.choice(range(1, delta))
            for delta in range(1, randdelta + 1):
                nx, ny = x + dx * delta, y + dy * delta
                board[nx][ny] = "*"
                walls.add((nx, ny, (dir + 3) % 4))
                walls.add((nx, ny, (dir + 1) % 4))

    def valid_to_wall(self, x, y, dir):
        board = self.board
        dx, dy = DIRECTIONS[dir]
        x1, y1 = x + dx, y + dy
        dx, dy = DIRECTIONS[(dir + 1) % 4]
        x2, y2 = x + dx, y + dy
        x3, y3 = x1 + dx, y1 + dy
        x4, y4 = x - dx, y - dy
        x5, y5 = x1 - dx, y1 - dy
        return (
            self.is_empty(x, y)
            and self.is_empty(x1, y1)
            and self.is_empty(x2, y2)
            and self.is_empty(x3, y3)
            and self.is_empty(x4, y4)
            and self.is_empty(x5, y5)
        )

    def is_empty(self, x, y):
        board = self.board
        h, w = len(board), len(board[0])
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        if board[x][y] == "*":
            return False
        return True

    def draw_border(self):
        board, walls, start, end = self.board, self.walls, self.start, self.end
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if (i, j) == start or (i, j) == end:
                    continue
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    board[i][j] = "*"
                    if i == 0:
                        walls.add((i, j, 0))
                    elif j == w - 1:
                        walls.add((i, j, 1))
                    elif i == h - 1:
                        walls.add((i, j, 2))
                    else:
                        walls.add((i, j, 3))

    def output(self):
        for row in self.board:
            print(" ".join(row))

    def random_on_border(self):
        n = self.n
        side = n - 1
        idx = random.choice(range(side * 4))
        while idx % side == 0:
            idx = random.choice(range(side * 4))
        # top
        if idx // side == 0:
            j = idx % side
            return (0, j)
        if idx // side == 1:
            i = idx % side
            return (i, side)
        if idx // side == 2:
            j = side - idx % side
            return (side, j)
        if idx // side == 3:
            i = side - idx % side
            return (i, 0)

    def wall_coordinates(self):
        board = self.board
        coordinates = set()
        for i, row in enumerate(board):
            for j, brick in enumerate(row):
                if brick == "*":
                    coordinates.add((i,j))
        return coordinates


# maze = RandomMaze(40)
# maze.output()

"""
* * * * * * * * * * * * * * * * * * * * * * * * * * * *   * * * * * * * * * * *
*   *                           *                         *   *   *           *
*       *     *     *     *         *     *     *     *               *   * * *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *       *
*             *                   *   *   *       *   *   *     *     *   * * *
*   * * * * * * * * * * *   * *   *           *       *   *     * *   *       *
*     *       *     *   *     *   * *   *   * *   * * *   *   * *         * * *
* *   *   * * * *           * *         *     *   *   *   *     * * *   * *   *
*         *   *     *   *     * * * *   *   * *       *         *         *   *
* *   *       * * * * * * *   *         *     *   *   * * *   * *   *         *
      *   * * *           *   *   *     * * * * * * * *         * * *   * * * *
* *   *       * * *   *       *   * *     *           * *   *   *         *   *
*     *   * * *       * * * * * * *             *           *   * *       *   *
* *   *       *   *     *         *   * * * * * * * * * * * * * *       * *   *
*     * * *   * * *     *   * * * *                 *           * *       *   *
* *   *       *   *   * *   *     * * * * *   *         * *   * *             *
*     *   * * *   *     *         *     *     * *   *   *       *   *   *     *
*     *   *   *   *     *   * * * * *       * *     * * *   *   * * * * * *   *
* * * *           * *   *   *     *     *     *         *   * * *     *   *   *
*         *   * * *     *   *   * * * * * * * * * *   * *   *   * *           *
*   *   * *       * *   *         *               *     *       *     * * * * *
* * *     * *           * *   * * *     * *     * *     *       * *   *   *   *
*       * *     * * *   *         * *     * *     *   * * *   * *             *
* *       * *       * * * * *   * *     * *       *       *     * * *     * * *
*         *     *       *         *       *   *   * *     *   * *             *
*     *   * *   *   * * *   * * * * *   * *   *   *     * *     * * * * * *   *
*   * *   *     *       *         *       * * *   *       *     *         *   *
*     *   * * * * * *         *   * * *   *       *   *   *   * * * * *       *
* *   *   *               * * *   *       *   *       *   *     *     * *   * *
*     *   *   *     *         * * * *     * * * * * * * * * *   * *     *     *
* * * * * * * * * * * *   *   *   *                       *     *       *     *
*           *   *   *     *       * *   * * * * *     *   *     * * *   *   * *
*   *   *               * * *     *     *   *   *   * *   * *   *             *
* * * * * * * *         *   *   * *   * *             *   *     *   *       * *
*         *           * *         *     * *   * *     *   *   * * * *   *     *
* * * *       *         *   * *   * * * *       * * * *   *     *       *   * *
*         *   * *   *   *     *   *           * *     *   *     *   *   *     *
* * * * * * * *     * * * * * *   *   * * *         * *   * *   *   * * * * * *
*                             *   *     *     *       *   *                   *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
