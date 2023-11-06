from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()


#좀비가 공에 1번 맞으면 반으로 줄어들고 두번 맞으면 사라짐.
#소년과 충돌하면 바로 게임프레임워크 quit. 사이즈가 작아지면 바운딩박스도 감소