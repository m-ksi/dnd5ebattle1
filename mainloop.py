import arcade
import settings
from grid import map_grid
from grid import path_grid
from grid import chars_grid
from character import paladin
import mainfuncs
import creature
from bestiary import suc

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

turn_mode = [1, 0]  # 1 - best init turn; 1 - choose attack, 2 - choose bonus, 3 - choose movement, 4 - choose spell


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_BROWN)

        self.char = paladin
        self.suc = suc
        self.Char_list = creature.CreatureList([paladin, suc])

        self.current_char = self.Char_list.get_creature(1)
        print(self.current_char.name, ' turn!')
        self.current_index = mainfuncs.get_sprite_index(self.current_char.sprite, self.Char_list.sprites) + 1

        self.grid_sprite_list = None
        self.button_sprite_list = None

        self.chars_sprite_list = self.Char_list.sprites

        self.target_list = None
        self.availability_list = None

    def setup(self):

        self.availability_list = arcade.SpriteList()  # cells available to choose
        self.button_sprite_list = arcade.SpriteList()  # all buttons
        self.target_list = arcade.SpriteList()  # targets to follow
        self.grid_sprite_list = arcade.SpriteList()  # map
        mainfuncs.draw_grid_sprites(self.grid_sprite_list, map_grid, bot_left_x, bot_left_y, step)
        mainfuncs.draw_chars(chars_grid, self.Char_list, bot_left_x, bot_left_y, step)
        mainfuncs.draw_buttons(self.button_sprite_list, bot_left_y, SCREEN_WIDTH)

    def empty_a_list(self):
        self.availability_list = None
        self.availability_list = arcade.SpriteList()

    def next_turn(self):
        turn_mode[1] = 0
        turn_mode[0] += 1
        if turn_mode[0] > len(self.Char_list.Creature_list):
            turn_mode[0] = 1
        t = turn_mode[0]
        self.Char_list.next_turn()
        self.current_char = self.Char_list.get_creature(t)
        self.current_index = mainfuncs.get_sprite_index(self.current_char.sprite, self.Char_list.sprites) + 1
        print(self.current_char.name, ' turn!')

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
        if button == arcade.MOUSE_BUTTON_LEFT and self.current_char.sprite.change_x == 0 and self.current_char.sprite.\
                change_y == 0 and ((x - (SCREEN_WIDTH // 5 * 3)) ** 2 + (y - (int(bot_left_y // 2) * 4 // 5)) ** 2 <= (
                rect_width // 2) ** 2):  # movement mode
            self.empty_a_list()
            if turn_mode[1] != 3:
                turn_mode[1] = 3
                mainfuncs.draw_available_moves(self.current_index, self.current_char, path_grid, chars_grid, self.
                                               availability_list, bot_left_x, bot_left_y, step)
                print(self.current_char.name, "'s sp left = ", self.current_char.sp, sep='')
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and self.current_char.sprite.change_x == 0 and self.current_char.sprite.\
                change_y == 0 and ((x - (SCREEN_WIDTH // 5)) ** 2 + (y - (
                int(bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # action mode
            self.empty_a_list()
            if turn_mode[1] != 1:
                turn_mode[1] = 1
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and self.current_char.sprite.change_x == 0 and self.current_char.sprite.\
                change_y == 0 and ((x - (SCREEN_WIDTH // 5 * 2)) ** 2 + (y - (
                int(bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # bonus mode
            self.empty_a_list()
            if turn_mode[1] != 2:
                turn_mode[1] = 2
            else:
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and turn_mode[1] == 3 and self.current_char.sp > 0:
            r = mainfuncs.get_clicked_available_ter(x, y, bot_left_x, bot_left_y, rect_width, step, self.availability_list)
            if r != -1:  # move
                mainfuncs.draw_path(self.target_list, r[0], r[1], path_grid, bot_left_x, bot_left_y, step, chars_grid,
                                    self.current_index, self.current_char)
                self.empty_a_list()
                turn_mode[1] = 0
        elif button == arcade.MOUSE_BUTTON_LEFT and self.current_char.sprite.change_x == 0 and self.current_char.sprite.\
                change_y == 0 and ((x - (SCREEN_WIDTH // 5 * 4)) ** 2 + (y - (
                int(bot_left_y // 2) * 4 // 5)) ** 2 <= (rect_width // 2) ** 2):  # next turn
            self.empty_a_list()
            self.next_turn()

    def on_update(self, delta_time: float):
        self.chars_sprite_list.update()
        self.grid_sprite_list.update()
        self.target_list.update()
        self.button_sprite_list.update()
        self.availability_list.update()

        mainfuncs.follow_target(self.target_list, self.current_char.sprite)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
