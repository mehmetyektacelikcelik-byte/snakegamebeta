import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20
CELL_NUMBER = WINDOW_WIDTH // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 36)

class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(5, 10), pygame.Vector2(4, 10), pygame.Vector2(3, 10)]
        self.direction = pygame.Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def check_collision(self):
        # Check if snake hits the wall
        if not 0 <= self.body[0].x < CELL_NUMBER or not 0 <= self.body[0].y < CELL_NUMBER:
            return True
        # Check if snake hits itself
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

class Food:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = pygame.Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        # Check if snake eats the food
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.score += 1

        # Make sure food doesn't spawn on snake
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()

    def check_fail(self):
        # Check if snake hits the wall or itself
        if self.snake.check_collision():
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(0, CELL_NUMBER, 2):
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(1, CELL_NUMBER, 2):
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(self.score)
        score_surface = font.render(score_text, True, WHITE)
        score_x = int(WINDOW_WIDTH - 60)
        score_y = int(WINDOW_HEIGHT - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

def main():
    game = Game()

    # Custom event for screen update
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = pygame.Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = pygame.Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = pygame.Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = pygame.Vector2(-1, 0)

        screen.fill(BLACK)
        game.draw_elements()
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()