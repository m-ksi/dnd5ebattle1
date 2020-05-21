import arcade
import time
import settings

height = settings.SCREEN_HEIGHT
width = settings.SCREEN_WIDTH


class Game(arcade.Window):

    def __init__(self, width, height, title):
        # call window initializer
        super().__init__(width, height, title)

        self.player_list = None

        # player info
        self.player_sprite = None

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("character.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print('start')
            while (self.player_sprite.center_x != x) and (self.player_sprite.center_y != y):
                dx = x - self.player_sprite.center_x
                dy = y - self.player_sprite.center_y
                print('path', dx, dy)
                s = (dx ** 2 + dy ** 2) ** 0.5
                if (round((dx * 5) / s) > dx) and (round((dy * 5) / s) > dy):
                    self.player_sprite.center_x += round((dx * 5) / s)
                    self.player_sprite.center_y -= round((dy * 5) / s)
                else:
                    self.player_sprite.center_x = x
                    self.player_sprite.center_y = y
                print('player', self.player_sprite.center_x, self.player_sprite.center_y)



    # def update(self, delta_time):


def main():
    """ Main method"""
    window = Game(width, height, "Example")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
