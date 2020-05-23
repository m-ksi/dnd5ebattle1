import arcade
import settings
from grid import map_grid
from grid import path_grid
from grid import chars_grid
import math
from character import char
import mainfuncs
# import bestiary

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

        self.char = char
        self.grid_sprite_list = None
        self.button_sprite_list = None
        self.char_sprite = None
        self.chars_sprite_list = None
        self.target_list = None

    def setup(self):
        self.char_sprite = arcade.Sprite(self.char.sprite, 8 / 3)
        self.chars_sprite_list = arcade.SpriteList()
        self.chars_sprite_list.append(self.char_sprite)

        self.target_list = arcade.SpriteList()
        self.grid_sprite_list = arcade.SpriteList()
        mainfuncs.draw_grid_sprites(self.grid_sprite_list, map_grid, bot_left_x, bot_left_y, step)
        mainfuncs.draw_chars(chars_grid, self.char_sprite, bot_left_x, bot_left_y, step)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        arcade.draw_rectangle_filled(FIELD_CENTER_X, FIELD_CENTER_Y, FIELD_WIDTH, FIELD_HEIGHT, arcade.color.BLACK)
        self.grid_sprite_list.draw()
        self.target_list.draw()
        self.chars_sprite_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT and len(self.target_list) == 0 and (bot_left_x - rect_width // 2) < x < (
                bot_left_x + 12 * step + rect_width // 2) and (bot_left_y - rect_width // 2) < y < (bot_left_y + 6 *
                                                                                                    step + rect_width
                                                                                                    // 2):
            grid_column = int((x - (bot_left_x - rect_width // 2)) // step)
            grid_row = int((y - (bot_left_y - rect_width // 2)) // step)

            target = arcade.Sprite("target.png", 0.5)
            target.center_x = int(bot_left_x + grid_column * step)
            target.center_y = int(bot_left_y + grid_row * step)
            self.target_list.append(target)

    def on_update(self, delta_time: float):
        self.chars_sprite_list.update()
        self.grid_sprite_list.update()
        self.target_list.update()

        mainfuncs.find_path(self.target_list, self.char_sprite)


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
