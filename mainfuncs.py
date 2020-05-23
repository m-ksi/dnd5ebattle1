import math
import arcade


def find_path(t_list, char_sprite):
    if t_list is not None:
        for target in t_list:
            start_x = char_sprite.center_x
            start_y = char_sprite.center_y
            dest_x = target.center_x
            dest_y = target.center_y
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)
            char_sprite.change_x = math.cos(angle) * 5
            char_sprite.change_y = math.sin(angle) * 5
            if (abs(char_sprite.center_x - dest_x) < 5) and \
                    (abs(char_sprite.center_y - dest_y) < 5):
                char_sprite.change_x = 0
                char_sprite.change_y = 0
                target.remove_from_sprite_lists()


def draw_grid_sprites(grid_sprite_list, map_grid, bot_left_x, bot_left_y, step):
    for row in range(7):
        for column in range(13):
            if map_grid[row][column] == 1:
                rect_sprite = arcade.Sprite('grass.jpg', 8 / 3)
            elif map_grid[row][column] == 2:
                rect_sprite = arcade.Sprite('swamp.jpg', 8 / 3)
            else:
                rect_sprite = arcade.Sprite('rocks.jpg', 8 / 3)
            rect_sprite.center_x = bot_left_x + column * step
            rect_sprite.center_y = bot_left_y + row * step
            grid_sprite_list.append(rect_sprite)


def draw_chars(chars_grid, char_sprite, bot_left_x, bot_left_y, step):
    for row in range(7):
        for column in range(13):
            if chars_grid[row][column] == 1:
                char_sprite.center_x = bot_left_x + column * step
                char_sprite.center_y = bot_left_y + row * step
