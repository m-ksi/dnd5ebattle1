import arcade


class Button:

    def __init__(self,
                 center_x, center_y,
                 image, height, width=None):
        self.center_x = center_x
        self.center_y = center_y
        self.image = image
        self.height = height
        self.width = width
        self.sprite = None

    def draw(self):
        self.sprite = arcade.Sprite(self.image, 8 / 3)
        self.sprite.center_x = self.center_x
        self.sprite.center_y = self.center_y
        self.sprite.draw()


def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        if button.width is None:  # circled button
            pass
        else:  # rectangle buttons
            pass
