from Players import *

# флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

# игровая сцена:
back = (200, 255, 255)  # цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
