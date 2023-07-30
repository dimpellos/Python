'''
TODO:
1. The snake is coloured on the screen. Fix it.
2. Refactoring of the code. Functions, utils.py, test_file.py
'''


# import random
# import curses
#
# s = curses.initscr()
# curses.curs_set(0) # set cursor
# sh, sw = s.getmaxyx() #width and height
# w = curses.newwin(sh, sw, 0, 0) # new window
# w.keypad(True) # accepts keypad input
# w.timeout(100) # refresh every 100ms the screen
# #
# # Snake initial position
# snk_x = sw//4
# snk_y = sh//2
# snake = [
#     [snk_y, snk_x],
#     [snk_y, snk_x-1],
#     [snk_y, snk_x-2]
# ]
#
# food = [sh/2, sw/2] # Food initial position
# w.addch(int(food[0]), int(food[1]), curses.ACS_PI) # Add food to the screen
# #
# key = curses.KEY_RIGHT # initial movement direction of the snake
# #
# while True:
#     next_key = w.getch()
#     key = key if next_key == -1 else next_key
#
#     if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
#         curses.endwin() # restores terminal to operating mode
#         w.keypad(False)
#         curses.echo()
#         quit()
#
#     new_head = [snake[0][0], snake[0][1]]
# #
#     if key == curses.KEY_DOWN:
#         new_head[0] += 1
#     if key == curses.KEY_UP:
#         new_head[0] -= 1
#     if key == curses.KEY_LEFT:
#         new_head[1] -= 1
#     if key == curses.KEY_RIGHT:
#         new_head[1] += 1
#
#     snake.insert(0, new_head)
#
#     if snake[0] == food:
#         food = None
#         while food is None:
#             nf = [
#                 random.randint(1, sh-1),
#                 random.randint(1, sw-1)
#             ]
#             food = nf if nf not in snake else None
#         w.addch(food[0], food[1], curses.ACS_PI)
#     else:
#         tail = snake.pop()
#         w.addch(int(tail[0]), int(tail[1]), ' ')
#
#     w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


import random
import curses

s = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = s.getmaxyx()
w = curses.newwin(screen_height, screen_width, 0, 0)
w.keypad(1)
w.timeout(100)

snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [screen_height // 2, screen_width // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_DIAMOND)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        w.keypad(False)
        print("Snake length was " + str(len(snake)))
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = nf if nf not in snake[0:] else None
            try:
                w.addch(int(food[0]),int(food[1]), curses.ACS_DIAMOND)
            except:
                pass
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

    except:
        curses.endwin()
        w.keypad(False)
        print("Snake length was " + str(len(snake)))
        quit()
