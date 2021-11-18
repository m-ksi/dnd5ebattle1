import math
import arcade
from pathfinder import find_path
# from actions import


def follow_target(t_list, char_sprite):
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


def draw_chars(char_list, bot_left_x, bot_left_y, step):
    """ old ver with chars_grid
    for i in range(len(char_list.init_list)):
        char = char_list.get_creature(i + 1)
        for row in range(7):
            for column in range(13):
                if char.name == "Leroy" and chars_grid[row][column] == 1:
                    char.sprite.center_x = bot_left_x + column * step
                    char.sprite.center_y = bot_left_y + row * step
                elif char.name == "Lilith" and chars_grid[row][column] == 2:
                    char.sprite.center_x = bot_left_x + column * step
                    char.sprite.center_y = bot_left_y + row * step
                elif char.name == "Lenny" and chars_grid[row][column] == 3:
                    char.sprite.center_x = bot_left_x + column * step
                    char.sprite.center_y = bot_left_y + row * step
    """
    for char in char_list.Creature_list:
        if char.position[0] is not None:
            char.sprite.center_x = bot_left_x + char.position[1] * step
            char.sprite.center_y = bot_left_y + char.position[0] * step


def get_cell_center(x, y, bot_left_x, bot_left_y, rect_width, step):
    grid_column = int((x - (bot_left_x - rect_width // 2)) // step)
    grid_row = int((y - (bot_left_y - rect_width // 2)) // step)
    return [int(bot_left_x + grid_column * step), int(bot_left_y + grid_row * step)]


def get_cell_center_by_r_c(row, column, bot_left_x, bot_left_y, step):
    return [int(bot_left_x + column * step), int(bot_left_y + row * step)]


def get_cell_r_c(x, y, bot_left_x, bot_left_y, rect_width, step):
    grid_column = int((x - (bot_left_x - rect_width // 2)) // step)
    grid_row = int((y - (bot_left_y - rect_width // 2)) // step)
    return [grid_row, grid_column]


def draw_buttons(button_sprite_list, bot_left_y, screen_width):
    # action_button_sprite = arcade.Sprite('actionbtn.png', 8 / 3)
    # bonus_button_sprite = arcade.Sprite('bonusbtn.png', 8 / 3)
    move_button_sprite = arcade.Sprite('movebtn.png', 8 / 3)
    turn_button_sprite = arcade.Sprite('next_turn.png', 8 / 3)
    center_y = int(bot_left_y // 2) * 4 // 5
    move_button_sprite.center_y = center_y
    turn_button_sprite.center_y = center_y
    move_button_sprite.center_x = screen_width // 5 * 3
    turn_button_sprite.center_x = screen_width // 5 * 4
    button_sprite_list.append(move_button_sprite)
    button_sprite_list.append(turn_button_sprite)

    action_selector_l = arcade.Sprite('a_button_left.jpg', 8 / 3)
    action_selector_c = arcade.Sprite('a_selector.jpg', 8 / 3)
    action_selector_r = arcade.Sprite('a_button.jpg', 8 / 3)
    action_selector_l.center_y = action_selector_c.center_y = action_selector_r.center_y = center_y
    action_selector_c.center_x = screen_width // 5
    action_selector_r.center_x = screen_width // 5 + 70
    action_selector_l.center_x = screen_width // 5 - 70
    button_sprite_list.append(action_selector_c)
    button_sprite_list.append(action_selector_l)
    button_sprite_list.append(action_selector_r)

    bonus_selector_l = arcade.Sprite('a_button_left.jpg', 8 / 3)
    bonus_selector_c = arcade.Sprite('a_selector.jpg', 8 / 3)
    bonus_selector_r = arcade.Sprite('a_button.jpg', 8 / 3)
    bonus_selector_l.center_y = bonus_selector_c.center_y = bonus_selector_r.center_y = center_y
    bonus_selector_c.center_x = screen_width // 5 * 2
    bonus_selector_r.center_x = screen_width // 5 * 2 + 70
    bonus_selector_l.center_x = screen_width // 5 * 2 - 70
    button_sprite_list.append(bonus_selector_c)
    button_sprite_list.append(bonus_selector_l)
    button_sprite_list.append(bonus_selector_r)


def draw_available_moves(chars_list, char, path_grid, a_list, bot_left_x, bot_left_y, step):
    a_grid = [[False for x in range(13)] for y in range(7)]
    char_row = char.position[0]
    char_column = char.position[1]
    """for i in range(13):
        for j in range(7):
            if chars_grid[j][i] == p:
                char_row = j
                char_column = i"""

    for i in range(char_column - char.sp, char_column + char.sp + 1):
        for j in range(char_row - char.sp, char_row + char.sp + 1):
            if 0 <= i <= 12 and 0 <= j <= 6:
                if path_grid[j][i] != 3 and [j, i] not in chars_list.positions:
                    path_dict = find_path(chars_list, path_grid, (char_column, char_row), (i, j), char.sp_type)[1]
                    if path_dict[i, j] <= char.sp:
                        a_grid[j][i] = True
                        if a_grid[j][i]:
                            a_sprite = arcade.Sprite('available_ter.png', 8 / 3)
                            a_sprite.center_x = bot_left_x + i * step
                            a_sprite.center_y = bot_left_y + j * step
                            a_list.append(a_sprite)


def get_clicked_available_ter(x, y, bot_left_x, bot_left_y, rect_width, step, availability_list):
    for ter in availability_list:
        cen_x, cen_y = get_cell_center(x, y, bot_left_x, bot_left_y, rect_width, step)
        if cen_x == ter.center_x and cen_y == ter.center_y:
            r = rect_width // 2
            if cen_x - r <= x <= cen_x + r and cen_y - r <= y <= cen_y + r:
                return get_cell_r_c(x, y, bot_left_x, bot_left_y, rect_width, step)
    return -1


def draw_path(target_list, row, column, path_grid, bot_left_x, bot_left_y, step, chars_list, char):
    c_row, c_column = char.position
    path, tot_costs, grid = find_path(chars_list, path_grid, (c_column, c_row), (column, row), char.sp_type)
    weights = grid.weights
    current = [column, row]
    nex = path[(current[0], current[1])]
    char.position = [row, column]
    chars_list.update_positions()
    total_weight = 0
    while path[(current[0], current[1])] is not None:
        total_weight += weights[(current[0], current[1]), (nex[0], nex[1])]
        # print(weights[(current[0], current[1]), (nex[0], nex[1])])
        center = get_cell_center_by_r_c(current[1], current[0], bot_left_x, bot_left_y, step)
        target = arcade.Sprite("target.png", 0.5)
        target.center_x = center[0]
        target.center_y = center[1]
        target_list.append(target)
        current = path[(current[0], current[1])]
        nex = path[(nex[0], nex[1])]
    char.sp -= total_weight


""" old stuff
def find_char(p, chars_grid):
    char_row = -1
    char_column = -1
    for i in range(13):
        for j in range(7):
            if chars_grid[j][i] == p:
                char_row = j
                char_column = i
    return char_row, char_column"""


def find_char(chars_list, row, column):
    for c in chars_list:
        if c.position == [row, column]:
            return c


def get_sprite_index(char, sprites):
    i = 0
    for a in sprites:
        if char == a:
            return i
        else:
            i += 1
    return -1


def load_actions(char, button_sprite, chosen_action, screen_width, bot_left_y):
    chosen_action = 0
    button_sprite = arcade.Sprite(char.actions.action_list[0].icon, 8/3)
    button_sprite.center_x = screen_width // 5
    button_sprite.center_y = int(bot_left_y // 2) * 4 // 5
    return button_sprite


def next_action(char, button_sprite, chosen_action, screen_width, bot_left_y):
    chosen_action += 1
    if chosen_action >= len(char.actions.action_list):
        chosen_action = 0
    button_sprite = arcade.Sprite(char.actions.action_list[chosen_action].icon, 8/3)
    button_sprite.center_x = screen_width // 5
    button_sprite.center_y = int(bot_left_y // 2) * 4 // 5
    return button_sprite, chosen_action


def previous_action(char, button_sprite, chosen_action, screen_width, bot_left_y):
    chosen_action -= 1
    if chosen_action < 0:
        chosen_action = len(char.actions.action_list) - 1
    button_sprite = arcade.Sprite(char.actions.action_list[chosen_action].icon, 8/3)
    button_sprite.center_x = screen_width // 5
    button_sprite.center_y = int(bot_left_y // 2) * 4 // 5
    return button_sprite, chosen_action


def draw_available_actions(chars_list, char, action_i, a_list, bot_left_x, bot_left_y, step):
    available_squares = []
    action = char.actions.action_list[action_i]
    reach = action.reach
    ren = False
    if reach == 0:
        available_squares.append(char.position)
    else:
        for row in range((char.position[0] - reach), (char.position[0] + reach + 1)):
            for column in range((char.position[1] - reach), (char.position[1] + reach + 1)):
                if [row, column] in chars_list.positions:
                    available_squares.append([row, column])
        odd = char.position
        available_squares.remove(odd)
        for square in available_squares:
            a_sprite = arcade.Sprite('available_ter.png', 8 / 3)
            a_sprite.center_x = bot_left_x + square[1] * step
            a_sprite.center_y = bot_left_y + square[0] * step
            a_list.append(a_sprite)
            ren = True
    return ren
