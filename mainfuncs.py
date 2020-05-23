import math
import arcade
from pathfinder import find_path
'''
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
                char_sprite.center_x = target.center_x
                char_sprite.center_y = target.center_y
                target.remove_from_sprite_lists()
'''


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


def get_cell_center(x, y, bot_left_x, bot_left_y, rect_width, step):
    grid_column = int((x - (bot_left_x - rect_width // 2)) // step)
    grid_row = int((y - (bot_left_y - rect_width // 2)) // step)
    return [int(bot_left_x + grid_column * step), int(bot_left_y + grid_row * step)]


def draw_buttons(button_sprite_list, bot_left_y, screen_width):
    action_button_sprite = arcade.Sprite('actionbtn.png', 8 / 3)
    bonus_button_sprite = arcade.Sprite('bonusbtn.png', 8 / 3)
    move_button_sprite = arcade.Sprite('movebtn.png', 8 / 3)
    turn_button_sprite = arcade.Sprite('next_turn.png', 8 / 3)
    center_y = int(bot_left_y // 2) * 4 // 5
    action_button_sprite.center_y = center_y
    bonus_button_sprite.center_y = center_y
    move_button_sprite.center_y = center_y
    turn_button_sprite.center_y = center_y
    action_button_sprite.center_x = screen_width // 5
    bonus_button_sprite.center_x = screen_width // 5 * 2
    move_button_sprite.center_x = screen_width // 5 * 3
    turn_button_sprite.center_x = screen_width // 5 * 4
    button_sprite_list.append(action_button_sprite)
    button_sprite_list.append(bonus_button_sprite)
    button_sprite_list.append(move_button_sprite)
    button_sprite_list.append(turn_button_sprite)
    return button_sprite_list


def draw_available_moves(char, path_grid, chars_grid, a_list, bot_left_x, bot_left_y, step):
    char_column = 0
    char_row = 0
    a_grid = [[False for x in range(13)] for y in range(7)]
    for i in range(13):
        for j in range(7):
            if chars_grid[j][i] == 1:
                char_row = j
                char_column = i

    for i in range(char_column - char.sp, char_column + char.sp):
        for j in range(char_row - char.sp, char_row + char.sp):
            if 0 <= i <= 12 and 0 <= j <= 6:
                if chars_grid[j][i] == 0 and path_grid[j][i] != 3:
                    path_dict = find_path(path_grid, (char_column, char_row), (i, j))[1]
                    if path_dict[i, j] <= char.sp:
                        a_grid[j][i] = True
                        if a_grid[j][i]:
                            a_sprite = arcade.Sprite('available_ter.png', 8 / 3)
                            a_sprite.center_x = bot_left_x + i * step
                            a_sprite.center_y = bot_left_y + j * step
                            a_list.append(a_sprite)
