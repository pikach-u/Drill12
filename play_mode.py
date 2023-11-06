import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy

    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    # 축구공 뿌리기
    global balls
    balls = [Ball(random.randint(100,1600),60,0.0) for _ in range(30)]
    game_world.add_objects(balls, 1)   #list를 더하는 함수

    # 좀비 5마리 추가
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    #충돌 상황 등록
    game_world.add_collision_pair('boy:ball', boy, None)
    game_world.add_collision_pair('boy:zombie', boy, None)


    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('ball:zombie',ball, None)


    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie)
        game_world.add_collision_pair('ball:zombie', None, zombie)




def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collision()
    # fill here
    # for ball in balls.copy():   #balls의 copy에서 처리하면서 원본 balls에서 ball을 삭제
    #     if game_world.collide(boy, ball):
    #         print("Collision Boy:Ball")
    #         #충돌처리
    #         #볼을 없앤다
    #         balls.remove(ball)
    #         game_world.remove_object(ball)  #이것만 해주면 안됨 볼 자체를 없애주어야 함
    #         #소년은 볼 카운트 증가
    #         boy.ball_count += 1

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

