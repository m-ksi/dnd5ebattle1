import math
import arcade
from pathfinder import find_path


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


def draw_chars(chars_grid, char_list, bot_left_x, bot_left_y, step):
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


def draw_available_moves(p, char, path_grid, chars_grid, a_list, bot_left_x, bot_left_y, step):
    char_column = 0
    char_row = 0
    a_grid = [[False for x in range(13)] for y in range(7)]
    for i in range(13):
        for j in range(7):
            if chars_grid[j][i] == p:
                char_row = j
                char_column = i

    for i in range(char_column - char.sp, char_column + char.sp + 1):
        for j in range(char_row - char.sp, char_row + char.sp + 1):
            if 0 <= i <= 12 and 0 <= j <= 6:
                if chars_grid[j][i] == 0 and path_grid[j][i] != 3:
                    path_dict = find_path(p, chars_grid, path_grid, (char_column, char_row), (i, j), char.sp_type)[1]
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


def draw_path(target_list, row, column, path_grid, bot_left_x, bot_left_y, step, chars_grid, p, char):
    c_row, c_column = find_char(p, chars_grid)
    path, tot_costs, grid = find_path(p, chars_grid, path_grid, (c_column, c_row), (column, row), char.sp_type)
    weights = grid.weights
    current = [column, row]
    nex = path[(current[0], current[1])]
    chars_grid[c_row][c_column] = 0
    chars_grid[row][column] = p
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


def find_char(p, chars_grid):
    char_row = -1
    char_column = -1
    for i in range(13):
        for j in range(7):
            if chars_grid[j][i] == p:
                char_row = j
                char_column = i
    return char_row, char_column


def get_sprite_index(char, sprites):
    i = 0
    for a in sprites:
        if char == a:
            return i
        else:
            i += 1
    return -1