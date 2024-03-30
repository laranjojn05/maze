class MazeGame:
    def __init__(self, maze):
        self.maze = maze

    def print_maze(self):
        for row in self.maze:
            print("".join(row))

    def move(self, direction):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'P':
                    if direction == 'up':
                        if self.maze[i - 1][j] != '#':
                            self.maze[i][j], self.maze[i - 1][j] = self.maze[i - 1][j], self.maze[i][j]
                    elif direction == 'down':
                        if self.maze[i + 1][j] != '#':
                            self.maze[i][j], self.maze[i + 1][j] = self.maze[i + 1][j], self.maze[i][j]
                    elif direction == 'left':
                        if self.maze[i][j - 1] != '#':
                            self.maze[i][j], self.maze[i][j - 1] = self.maze[i][j - 1], self.maze[i][j]
                    elif direction == 'right':
                        if self.maze[i][j + 1] != '#':
                            self.maze[i][j], self.maze[i][j + 1] = self.maze[i][j + 1], self.maze[i][j]
                    return

maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", "P", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]

game = MazeGame(maze)

while True:
    game.print_maze()
    move = input("Enter your move (up/down/left/right): ").lower()
    if move in ['up', 'down', 'left', 'right']:
        game.move(move)
    else:
        print("Invalid move! Please enter up, down, left, or right.")