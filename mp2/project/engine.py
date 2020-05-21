import pyglet
import cv2
from importlib import import_module
from sys import path
from config import config
from os import mkdir
import datetime
import time
import playsound

def draw_text(frame, text, x, y, color=(255,255,255), thickness=5, size=4):
        if x is not None and y is not None:
            cv2.putText(frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_DUPLEX, size, color, thickness)

def get_images():

    tmpdir = 'tmp'

    try:
        mkdir(tmpdir)
    except FileExistsError:
        pass

    cam = cv2.VideoCapture(config['source'])

    img_counter = 0

    init_time = time.time()
    test_timeout = init_time + config['timer']
    final_timeout = init_time + config['timer']
    counter_timeout_text = init_time + 1
    counter_timeout = init_time + 1
    counter = config['timer']

    tick = 'resources/sounds/tick.wav'
    shutter = 'resources/sounds/shutter.wav'
    
    while img_counter < 4:
        ret, frame = cam.read()

        x = int(frame.shape[0] * (3/4))
        y = int(frame.shape[0] / 4)

        if (time.time() > counter_timeout_text and time.time() < test_timeout):
            draw_text(frame, str(counter), x, y)
            counter_timeout_text += 0.03333

        if (time.time() > counter_timeout and time.time() < test_timeout):
            counter-=1
            counter_timeout+=1
            playsound.playsound(tick)

        cv2.imshow("Camera", frame)

        if not ret:
            break

        if (cv2.waitKey(1) & 0xFF == ord('q')) or (time.time() > final_timeout):
            playsound.playsound(shutter)
            img_name = "tmp/" + "photo_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

            init_time = time.time()
            test_timeout = init_time + config['timer']
            final_timeout = init_time + config['timer']
            counter_timeout_text = init_time + 1
            counter_timeout = init_time + 1
            counter = config['timer']

    cam.release()

    cv2.destroyAllWindows()