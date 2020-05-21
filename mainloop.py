import arcade
import settings

SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = SCREEN_WIDTH // 16 * 9
FIELD_WIDTH = SCREEN_WIDTH * 13 // 16
FIELD_HEIGHT = SCREEN_HEIGHT * 7 // 9


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_BROWN)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        arcade.draw_rectangle_filled(7 * SCREEN_WIDTH // 16, 5 * SCREEN_HEIGHT // 9, FIELD_WIDTH, FIELD_HEIGHT,
                                     arcade.color.AMAZON)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'Test')
    arcade.run()


if __name__ == "__main__":
    main()