import arcade
import settings
from grid import map_grid
from grid import path_grid
from grid import chars_grid
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
turn_mode = [1, 0]  # 1 - your turn; 1 - choose attack, 2 - choose bonus, 3 - choose movement, 4 - choose spell


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
        self.availability_list = None

    def setup(self):
        self.char_sprite = arcade.Sprite(self.char.sprite, 8 / 3)
        self.chars_sprite_list = arcade.SpriteList()
        self.chars_sprite_list.append(self.char_sprite)

        self.availability_list = arcade.SpriteList()  # cells available to choose
        self.button_sprite_list = arcade.SpriteList()  # all buttons
        self.target_list = arcade.SpriteList()  # targets to follow
        self.grid_sprite_list = arcade.SpriteList()  # map
        mainfuncs.draw_grid_sprites(self.grid_sprite_list, map_grid, bot_left_x, bot_left_y, step)
        mainfuncs.draw_chars(chars_grid, self.char_sprite, bot_left_x, bot_left_y, step)
        mainfuncs.draw_buttons(self.button_sprite_list, bot_left_y, SCREEN_WIDTH)

    def empty_a_list(self):
        self.availability_list = None
        self.availability_list = arcade.SpriteList()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        arcade.draw_rectangle_filled(FIELD_CENTER_X, FIELD_CENTER_Y, FIELD_WIDTH, FIELD_HEIGHT, arcade.color.BLACK)
        self.button_sprite_list.draw()
        self.grid_sprite_list.draw()
        self.target_list.draw()
        self.chars_sprite_list.draw()
        self.availability_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        '''if button == arcade.MOUSE_BUTTON_LEFT and len(self.target_list) == 0 and (bot_left_x - rect_width // 2) < x < (
                bot_left_x + 12 * step + rect_width // 2) and (bot_left_y - rect_width // 2) < y < (bot_left_y + 6 *
                                                                                                    step + rect_width
                                                                                                    // 2):
            cell_center = mainfuncs.get_cell_center(x, y, bot_left_x, bot_left_y, rect_width, step)
            target = arcade.Sprite("target.png", 0.5)
            target.center_x = cell_center[0]
            target.center_y = cell_center[1]
            self.target_list.append(target)'''
        if button == arcade.MOUSE_BUTTON_LEFT and turn_mode[0] == 1 and ((x - (SCREEN_WIDTH // 5 * 3)) ** 2 + (y - (int(
                bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # movement mode
            self.empty_a_list()
            if turn_mode[1] != 3:
                turn_mode[1] = 3
                mainfuncs.draw_available_moves(char, path_grid, chars_grid, self.availability_list, bot_left_x,
                                               bot_left_y, step)
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and turn_mode[0] == 1 and ((x - (SCREEN_WIDTH // 5)) ** 2 + (y - (
                int(bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # attack mode
            self.empty_a_list()
            if turn_mode[1] != 1:
                turn_mode[1] = 1
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and turn_mode[0] == 1 and ((x - (SCREEN_WIDTH // 5 * 2)) ** 2 + (y - (
                int(bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # bonus mode
            self.empty_a_list()
            if turn_mode[1] != 2:
                turn_mode[1] = 2
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and turn_mode[0] == 1 and turn_mode[1] == 3 and char.sp > 0:
            r = mainfuncs.get_clicked_available_ter(x, y, bot_left_x, bot_left_y, rect_width, step, self.availability_list)
            if r != -1:
                mainfuncs.draw_path(self.target_list, r[0], r[1], path_grid, bot_left_x, bot_left_y, step, chars_grid)
                self.empty_a_list()
                turn_mode[1] = 0

    def on_update(self, delta_time: float):
        if turn_mode[1] == 1:
            pass
        elif turn_mode[1] == 2:
            pass
        elif turn_mode[1] == 3:
            pass
        elif turn_mode[1] == 0:
            pass
        self.chars_sprite_list.update()
        self.grid_sprite_list.update()
        self.target_list.update()
        self.button_sprite_list.update()
        self.availability_list.update()

        if turn_mode[0] == 1:
            mainfuncs.follow_target(self.target_list, self.char_sprite)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
