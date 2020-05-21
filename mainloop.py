import arcade
import math
import settings

height = settings.SCREEN_HEIGHT
width = settings.SCREEN_WIDTH


class Game(arcade.Window):

    def __init__(self, width, height, title):
        # call window initializer
        super().__init__(width, height, title)

        self.player_list = None
        self.target_list = None

        # player info
        self.player_sprite = None
        self.target_sprite = None

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("character.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.target_list = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        self.target_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and len(self.target_list) == 0:
            target = arcade.Sprite("target.png", 0.3)
            target.center_x = x
            target.center_y = y

            self.target_list.append(target)
            '''start_x = self.player_sprite.center_x
            start_y = self.player_sprite.center_y
            dest_x = x
            dest_y = y
            self.dest_x = x
            self.dest_y = y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            self.player_sprite.change_x = math.cos(angle) * 2
            self.player_sprite.change_y = math.sin(angle) * 2
            if (abs(self.player_sprite.center_x - dest_x) < 2) and \
                    (abs(self.player_sprite.center_y - dest_y) < 2):
                print('here!')
                self.player_sprite.change_x = 0
                self.player_sprite.change_y = 0
                return'''

    def on_update(self, delta_time):
        self.player_list.update()
        self.target_list.update()

        if self.target_list is not None:
            for target in self.target_list:
                start_x = self.player_sprite.center_x
                start_y = self.player_sprite.center_y
                dest_x = target.center_x
                dest_y = target.center_y
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)
                self.player_sprite.change_x = math.cos(angle) * 3
                self.player_sprite.change_y = math.sin(angle) * 3
                if (abs(self.player_sprite.center_x - dest_x) < 3) and \
                        (abs(self.player_sprite.center_y - dest_y) < 3):
                    self.player_sprite.change_x = 0
                    self.player_sprite.change_y = 0
                    target.remove_from_sprite_lists()


'''def mov(sprite, x, y):
    start_x = sprite.center_x
    start_y = sprite.center_y
    dest_x = x
    dest_y = y
    x_diff = dest_x - start_x
    y_diff = dest_y - start_y
    angle = math.atan2(y_diff, x_diff)
    while (abs(sprite.center_x - dest_x) >= 2) and \
            (abs(sprite.center_y - dest_y) >= 2):
        sprite.change_x = math.cos(angle) * 2
        sprite.change_y = math.sin(angle) * 2
    sprite.change_x = 0
    sprite.change_y = 0
    return'''


def main():
    """ Main method"""
    window = Game(width, height, "Example")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
