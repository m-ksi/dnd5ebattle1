import arcade
import settings
from grid import map_grid
from grid import path_grid
from grid import chars_grid

SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = SCREEN_WIDTH // 16 * 9
rect_width = SCREEN_WIDTH // 16
FIELD_WIDTH = 13.7 * rect_width  # SCREEN_WIDTH * 13 // 16
FIELD_HEIGHT = 7.4 * rect_width  # SCREEN_HEIGHT * 7 // 9
FIELD_CENTER_X = 7.15 * SCREEN_WIDTH // 16
FIELD_CENTER_Y = 5 * SCREEN_HEIGHT // 9
step = int(rect_width + (rect_width / 20))
bot_left_x = FIELD_CENTER_X - 6 * step
bot_left_y = FIELD_CENTER_Y - 3 * step


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_BROWN)

        self.grid_sprite_list = None
        self.chars_sprite_list = None
        self.draw_grid_sprites()
        self.draw_chars()

    def draw_chars(self):
        self.chars_sprite_list = arcade.SpriteList()
        for row in range(7):
            for column in range(13):
                if chars_grid[row][column] == 1:
                    char_sprite = arcade.Sprite('char.png', 8/3)
                    char_sprite.center_x = bot_left_x + column * step
                    char_sprite.center_y = bot_left_y + row * step
                    self.chars_sprite_list.append(char_sprite)

    def draw_grid_sprites(self):
        self.grid_sprite_list = arcade.SpriteList()
        for row in range(7):
            for column in range(13):
                if map_grid[row][column] == 1:
                    rect_sprite = arcade.Sprite('grass.jpg', 8/3)
                elif map_grid[row][column] == 2:
                    rect_sprite = arcade.Sprite('swamp.jpg', 8/3)
                else:
                    rect_sprite = arcade.Sprite('rocks.jpg', 8/3)
                rect_sprite.center_x = bot_left_x + column * step
                rect_sprite.center_y = bot_left_y + row * step
                self.grid_sprite_list.append(rect_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        arcade.draw_rectangle_filled(FIELD_CENTER_X, FIELD_CENTER_Y, FIELD_WIDTH, FIELD_HEIGHT, arcade.color.BLACK)
        self.grid_sprite_list.draw()
        self.chars_sprite_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if (bot_left_x - rect_width // 2) < x < (bot_left_x + 12 * step + rect_width // 2) and (
                bot_left_y - rect_width // 2) < y < (bot_left_y + 6 * step + rect_width // 2):
            grid_column = int((x - (bot_left_x - rect_width // 2)) // step)
            grid_row = int((y - (bot_left_y - rect_width // 2)) // step)
            print(int(bot_left_x + grid_column * step), int(bot_left_y + grid_row * step))


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test')
    arcade.run()


if __name__ == "__main__":
    main()
