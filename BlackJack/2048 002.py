import random
import subprocess
import sys
import keyboard
import pygame
import math
import time

inf = float('inf')


def clear_screen():
    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls', shell=True)


class Node:
    def __init__(self, value, index, left=None, right=None, up=None, down=None):
        self.right = left
        self.left = right
        self.up = up
        self.down = down
        self.val = value
        self.index = index

    def show(self):
        print(self.val)


class Board:
    colors = {
        2: (238, 228, 218),  # White
        4: (237, 224, 200),  # Light Gray
        8: (242, 177, 121),  # Orange
        16: (245, 149, 99),  # Gold
        32: (246, 124, 96),  # Orange Red
        64: (246, 94, 59),  # Red
        128: (237, 207, 115),  # Pink
        256: (237, 204, 98),  # Light Purple
        512: (237, 200, 80),  # Purple
        1024: (237, 197, 63),  # Dark Purple
        2048: (237, 194, 45)  # Gold
    }

    def __init__(self, size=16):
        self.score = 0
        self.size = size
        self.WIDTH, self.HEIGHT = 600, 600
        self.ROWS, self.COLS = int(math.sqrt(self.size)), int(math.sqrt(self.size))
        self.CELL_SIZE = self.WIDTH // self.COLS
        self.GRID_COLOR = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.WHITE = (255, 255, 255)

        pygame.init()  # Initialize pygame
        self.squares = []  # Make squares an instance variable
        self.font = pygame.font.SysFont(None, 48)  # Use a standard system font with size 36
        self.one = [i - 1 for i in
                    range(int(math.sqrt(self.size)), self.size + int(math.sqrt(self.size)), int(math.sqrt(self.size)))]
        self.two = [i for i in range(0, self.size, int(math.sqrt(self.size)))]
        for i in range(self.size):
            self.squares.append(Node(float('inf'), i))
        for i in range(self.size):
            if i not in self.one:
                self.squares[i].right = self.squares[i + 1]
        for i in range(self.size):
            if i not in self.two:
                self.squares[i].left = self.squares[i - 1]
        for i in range(self.size - int(math.sqrt(self.size))):
            self.squares[i].down = self.squares[i + int(math.sqrt(self.size))]
        for i in range(int(math.sqrt(self.size)), self.size):
            self.squares[i].up = self.squares[i - int(math.sqrt(self.size))]
        self.new_square()
        self.draw_game()

        clear_screen()
        print(self.score)

    def showBoard(self):
        for node in self.squares:
            node.show()  # Using show method of Node to print the value

    def draw_grid(self):
        for x in range(0, self.WIDTH, self.CELL_SIZE):
            pygame.draw.line(self.screen, self.GRID_COLOR, (x, 0), (x, self.HEIGHT))
            for y in range(0, self.HEIGHT, self.CELL_SIZE):
                pygame.draw.line(self.screen, self.GRID_COLOR, (0, y), (self.WIDTH, y))

    def color_grid(self):
        for index, square in enumerate(self.squares):
            row = index // self.COLS
            col = index % self.COLS
            square_rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            if square.val != inf:
                pygame.draw.rect(self.screen, self.colors[square.val], square_rect)
                # Render the text
                if square.val == inf:
                    text_surface = self.font.render('0', True, (0, 0, 0))  # Render '2' in white color
                else:
                    text_surface = self.font.render(str(square.val), True, (0, 0, 0))  # Render '2' in white color
                text_rect = text_surface.get_rect(center=square_rect.center)  # Center the text within the cell
                self.screen.blit(text_surface, text_rect)  # Draw the text on the screen
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), square_rect)

        # Update the display outside the loop
        pygame.display.flip()

    def draw_game(self):
        # self.screen.fill((0, 0, 0))
        self.draw_grid()
        self.color_grid()

    def check_game_over(self):
        for tile in self.squares:
            if tile.val == inf:
                return False  # Game is not over: there's an empty tile.
            if (tile.left and tile.val == tile.left.val) or \
                    (tile.right and tile.val == tile.right.val) or \
                    (tile.up and tile.val == tile.up.val) or \
                    (tile.down and tile.val == tile.down.val):
                return False  # Game is not over: there are mergeable tiles.

        # If no empty or mergeable tiles are found, then the game is over.
        return True

    def __str__(self):
        board_str = ""
        for i in range(0, 16, 4):
            row = self.squares[i:i + 4]
            board_str += ' '.join(str(node) for node in row) + "\n"
        return board_str.strip()

    '''
    0  1  2  3
    4  5  6  7 
    8  9  10 11
    12 13 14 15
    '''

    def new_square(self):
        square = random.choice(range(16))
        if self.squares[square].val == inf:
            self.squares[square].val = random.choices([2, 4], weights=[9, 1], k=1)[0]
        else:
            self.new_square()

    def start_move(self, direction):
        a = []
        for i in range(int(math.sqrt(self.size)) - 2, -1, -1):
            for j in range(int(math.sqrt(self.size))):
                a.append(i + int(math.sqrt(self.size)) * j)

        b = []
        for i in range(1, int(math.sqrt(self.size))):
            for j in range(int(math.sqrt(self.size))):
                b.append(i + int(math.sqrt(self.size)) * j)

        c = []
        for i in range(self.size - 2 * int(math.sqrt(self.size)), -1, -int(math.sqrt(self.size))):
            for j in range(int(math.sqrt(self.size))):
                c.append(i + j)
        dir_dictionary = {

            'right': a,  # [2, 6, 10, 14, 1, 5, 9, 13, 0, 4, 8, 12],
            'left': b,  # [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15],
            'up': [i for i in range(int(math.sqrt(self.size)), self.size)],
            'down': c,  # [8, 9, 10, 11, 4, 5, 6, 7, 0, 1, 2, 3]
        }
        moved = False
        moved_ = 0
        for i in dir_dictionary[direction]:
            if self.move(self.squares[i], direction, moved_) == 1:
                moved_ = 1

        if moved_ == 1:
            self.new_square()

        self.draw_game()
        clear_screen()
        print(self.score)

    def move(self, node, direction, counter):
        next_node = getattr(node, direction)

        # Check if there is a neighboring node
        if node.val != inf:
            if next_node is None:
                return 0

            # If the neighboring node is empty, move the current node to it
            if next_node.val == inf:
                next_node.val = node.val
                node.val = inf
                # print(f"you can move {direction}")
                if getattr(next_node, direction):
                    self.move(next_node, direction, counter)
                    return 1
                else:
                    # print("You can't move")
                    counter += 1
                    return 1

            # If the neighboring node has the same value, merge them
            elif next_node.val == node.val:
                next_node.val *= 2
                self.score += (node.val * 2)
                node.val = inf
                # print(f"you can move {direction}")
                counter += 1
                return 1

        else:
            return 0


def game_over(board):
    clear_screen()
    print("Game Over")
    print(f"Score: {board.score}")


def main():
    board = Board(16)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.start_move('left')
                elif event.key == pygame.K_RIGHT:
                    board.start_move('right')
                elif event.key == pygame.K_UP:
                    board.start_move('up')
                elif event.key == pygame.K_DOWN:
                    board.start_move('down')
                elif event.key == pygame.K_q:
                    running = False
            for square in board.squares:
                if square.val == 2048:
                    print("2048!")
                    print(f"Score: {board.score}")
            if board.check_game_over() is True:
                game_over(board)
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


