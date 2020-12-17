#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import random
import time

# Initialisiern der Variablen, Listen und Parametern, und definieren der Funktionen, Motoren und Sensoren.

arm=Motor(Port.B)
color=Motor(Port.A, Direction.COUNTERCLOCKWISE, [12, 36])
rotation=Motor(Port.C, Direction.CLOCKWISE, [12, 36])
scan=ColorSensor(Port.S1)

searched_stone = 0
is_solved = False
correct_scan = False
ROTATION_SPEED = 400
ROTATION_SPEED_SOLVE = 300
deltaAngle = 4
COLOR_ANGLE = 22
move = False
moves = []

up_center = 0
front_center = 0
down_center = 0
back_center = 0
left_center = 0
right_center = 0
up_front_left_corner = [0, 0, 0]
up_front_right_corner = [0, 0, 0]
up_back_right_corner = [0, 0, 0]
up_back_left_corner = [0, 0, 0]
down_front_left_corner = [0, 0, 0]
down_front_right_corner = [0, 0, 0]
down_back_right_corner = [0, 0, 0]
down_back_left_corner = [0, 0, 0]
up_front_edge = [0, 0]
up_right_edge = [0, 0]
up_left_edge = [0, 0]
up_back_edge = [0, 0]
middle_front_left_edge = [0, 0]
middle_front_right_edge = [0, 0]
middle_back_right_edge = [0, 0]
middle_back_left_edge = [0, 0]
down_front_edge = [0, 0]
down_right_edge = [0, 0]
down_left_edge = [0, 0]
down_back_edge = [0, 0]
count_yellow = 0
count_white = 0
count_red = 0
count_black = 0
count_blue = 0
count_green = 0

def rotate_clockwise():

    # Die untere Fläche dreht sich mit dem Uhrzeigersinn und ändert die Positionen der Mittelsteine.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle
    rotation.run_angle(ROTATION_SPEED_SOLVE, 90, Stop.HOLD)

    help = front_center
    front_center = right_center
    right_center = back_center
    back_center = left_center
    left_center = help

def rotate_counterclockwise():

    # Die untere Fläche dreht sich gegem den Uhrzeigersinn und ändert die Positionen der Mittelsteine.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle
    rotation.run_angle(ROTATION_SPEED_SOLVE, -90, Stop.HOLD)

    help = front_center
    front_center = left_center
    left_center = back_center
    back_center = right_center
    right_center = help

def rotate_2():

    # Die untere Fläche dreht sich mit dem Uhrzeigersinn 2-Mal und ändert die Positionen der Mittelsteine.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle
    rotation.run_angle(ROTATION_SPEED_SOLVE, 180, Stop.HOLD)

    help = front_center
    front_center = back_center
    back_center = help
    help = left_center
    left_center = right_center
    right_center = help

def turn(): 

    # Der Zauberwürfel dreht sich einmal und ändert die Position der Mittelsteine.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    arm.run_angle(150, -190)
    arm.run_angle(200, 190)

    help = up_center
    up_center = back_center
    back_center = down_center
    down_center = front_center
    front_center = help   

def independent_rotate_clockwise():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Die untere Fläche dreht sich mit dem Uhrzeigersinn.

    rotation.run_angle(ROTATION_SPEED_SOLVE, 90, Stop.HOLD)

def independent_rotate_counterclockwise():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Die untere Fläche dreht sich gegen den Uhrzeigersinn.

    rotation.run_angle(ROTATION_SPEED_SOLVE, -90, Stop.HOLD)

def independent_rotate_2():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Die untere Fläche dreht sich mit dem Uhrzeigersinn 2-Mal.

    rotation.run_angle(ROTATION_SPEED_SOLVE, 180, Stop.HOLD)

def independent_turn():

    # Der Zauberwürfel dreht sich einmal.

    arm.run_angle(150, -180)
    arm.run_angle(200, 180)

def turn_right_direction(up, front):

    # Der Roboter dreht den Stein in die gewünschte Position.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge

    if up == back_center:
        turn()
    if up == down_center:
        turn()
        turn()
    if up == front_center:
        rotate_2()
        turn()
    if up == left_center:
        rotate_clockwise()
        turn()
    if up == right_center:
        rotate_counterclockwise()
        turn()
    
    if front == back_center:
        rotate_2()
    if front == left_center:
        rotate_counterclockwise()
    if front == right_center:
        rotate_clockwise()

def hold():

    # Der Zauberwürfel wird festgehalten.

    arm.run_angle(100, -120)

def hold_back():

    # Der Zauberwürfel wird losgelassen.

    arm.run_angle(100, 120)

def hold_rotate_clockwise():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Der Zauberwürfel wird festgehalten und die untere Ebene wird um 90 Grad im Uhrzeigersinn gedreht. Variablen werden nicht verändert.

    hold()
    rotation.run_angle(ROTATION_SPEED_SOLVE, 90+deltaAngle)
    rotation.run_angle(ROTATION_SPEED_SOLVE, -deltaAngle)
    hold_back()

def hold_rotate_counterclockwise():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Der Zauberwürfel wird festgehalten und die untere Ebene wird um 90 Grad gegen den Uhrzeigersinn gedreht. Variablen werden nicht verändert.

    hold()
    rotation.run_angle(ROTATION_SPEED_SOLVE, -(90+deltaAngle))
    rotation.run_angle(ROTATION_SPEED_SOLVE, deltaAngle)
    hold_back()

def hold_rotate2():
    global ROTATION_SPEED,ROTATION_SPEED_SOLVE, deltaAngle

    # Der Zauberwürfel wird festgehalten und die untere Ebene wird um 180 Grad im Uhrzeigersinn gedreht. Variablen werden nicht verändert.

    hold()
    rotation.run_angle(ROTATION_SPEED_SOLVE, 180+deltaAngle)
    rotation.run_angle(ROTATION_SPEED_SOLVE, -deltaAngle)
    hold_back()

def find_brick(colors):
    
    # Findet einen gesuchten Stein anhand seiner Farben.

    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    
    # Das Programm checkt, ob die angegebenen Farben zu einer Ecke, einer Kante oder einem Mittelstein gehören. Dann antwortet die Funktion mit dem richtigen Stein. Chiffrierung: siehe Dokument im Projektordner.

    if type(colors) is list:
        if len(colors) == 2:
            if colors == up_front_edge:
                return ["up_front_edge", up_front_edge[0]]
            elif colors == up_back_edge:
                return ["up_back_edge", up_back_edge[0]]
            elif colors == up_left_edge:
                return ["up_left_edge", up_left_edge[0]]
            elif colors == up_right_edge:
                return ["up_right_edge", up_right_edge[0]]
            elif colors == middle_front_left_edge:
                return ["middle_front_left_edge", middle_front_left_edge[0]]
            elif colors == middle_front_right_edge:
                return ["middle_front_right_edge", middle_front_right_edge[0]]
            elif colors == middle_back_left_edge:
                return ["middle_back_left_edge", middle_back_left_edge[0]]
            elif colors == middle_back_right_edge:
                return ["middle_back_right_edge", middle_back_right_edge[0]]
            elif colors == down_front_edge:
                return ["down_front_edge", down_front_edge[0]]
            elif colors == down_back_edge:
                return ["down_back_edge", down_back_edge[0]]
            elif colors == down_left_edge:
                return ["down_left_edge", down_left_edge[0]]
            elif colors == down_right_edge:
                return ["down_right_edge", down_right_edge[0]]
            
            more_colors = [colors[1], colors[0]]

            if more_colors == up_front_edge:
                return ["up_front_edge", up_front_edge[0]]
            elif more_colors == up_back_edge:
                return ["up_back_edge", up_back_edge[0]]
            elif more_colors == up_left_edge:
                return ["up_left_edge", up_left_edge[0]]
            elif more_colors == up_right_edge:
                return ["up_right_edge", up_right_edge[0]]
            elif more_colors == middle_front_left_edge:
                return ["middle_front_left_edge", middle_front_left_edge[0]]
            elif more_colors == middle_front_right_edge:
                return ["middle_front_right_edge", middle_front_right_edge[0]]
            elif more_colors == middle_back_left_edge:
                return ["middle_back_left_edge", middle_back_left_edge[0]]
            elif more_colors == middle_back_right_edge:
                return ["middle_back_right_edge", middle_back_right_edge[0]]
            elif more_colors == down_front_edge:
                return ["down_front_edge", down_front_edge[0]]
            elif more_colors == down_back_edge:
                return ["down_back_edge", down_back_edge[0]]
            elif more_colors == down_left_edge:
                return ["down_left_edge", down_left_edge[0]]
            elif more_colors == down_right_edge:
                return ["down_right_edge", down_right_edge[0]]

        if len(colors) == 3:
            if colors == up_front_left_corner:
                return ["up_front_left_corner", up_front_left_corner[0]]
            elif colors == up_front_right_corner:
                return ["up_front_right_corner", up_front_right_corner[0]]
            elif colors == up_back_left_corner:
                return ["up_back_left_corner", up_back_left_corner[0]]
            elif colors == up_back_right_corner:
                return ["up_back_right_corner", up_back_right_corner[0]]
            elif colors == down_front_left_corner:
                return ["down_front_left_corner", down_front_left_corner[0]]
            elif colors == down_front_right_corner:
                return ["down_front_right_corner", down_front_right_corner[0]]
            elif colors == down_back_left_corner:
                return ["down_back_left_corner", down_back_left_corner[0]]
            elif colors == down_back_right_corner:
                return ["down_back_right_corner", down_back_right_corner[0]]         
            
            more_colors = [colors[2], colors[0], colors[1]]

            if more_colors == up_front_left_corner:
                return ["up_front_left_corner", up_front_left_corner[0]]
            elif more_colors == up_front_right_corner:
                return ["up_front_right_corner", up_front_right_corner[0]]
            elif more_colors == up_back_left_corner:
                return ["up_back_left_corner", up_back_left_corner[0]]
            elif more_colors == up_back_right_corner:
                return ["up_back_right_corner", up_back_right_corner[0]]
            elif more_colors == down_front_left_corner:
                return ["down_front_left_corner", down_front_left_corner[0]]
            elif more_colors == down_front_right_corner:
                return ["down_front_right_corner", down_front_right_corner[0]]
            elif more_colors == down_back_left_corner:
                return ["down_back_left_corner", down_back_left_corner[0]]
            elif more_colors == down_back_right_corner:
                return ["down_back_right_corner", down_back_right_corner[0]]

            more_colors = [more_colors[2], more_colors[0], more_colors[1]]

            if more_colors == up_front_left_corner:
                return ["up_front_left_corner", up_front_left_corner[0]]
            elif more_colors == up_front_right_corner:
                return ["up_front_right_corner", up_front_right_corner[0]]
            elif more_colors == up_back_left_corner:
                return ["up_back_left_corner", up_back_left_corner[0]]
            elif more_colors == up_back_right_corner:
                return ["up_back_right_corner", up_back_right_corner[0]]
            elif more_colors == down_front_left_corner:
                return ["down_front_left_corner", down_front_left_corner[0]]
            elif more_colors == down_front_right_corner:
                return ["down_front_right_corner", down_front_right_corner[0]]
            elif more_colors == down_back_left_corner:
                return ["down_back_left_corner", down_back_left_corner[0]]
            elif more_colors == down_back_right_corner:
                return ["down_back_right_corner", down_back_right_corner[0]]

    else:
        if colors == up_center:
            return ["up_center", up_center]
        elif colors == front_center:
            return ["front_center", front_center]
        elif colors == down_center:
            return ["down_center", down_center]
        elif colors == back_center:
            return ["back_center", back_center]
        elif colors == left_center:
            return ["left_center", left_center]
        elif colors == right_center:
            return ["right_center", right_center]

    more_colors = 0

def scan_test(variable):
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, correct_scan, count_black, count_blue, count_green, count_red, count_white, count_yellow
    
    # Zählt, wieviele Steine welche Farben haben.
    
    if type(variable) is list:
        count_yellow += variable.count(Color.YELLOW)
        count_black += variable.count(Color.BLACK)
        count_white += variable.count(Color.WHITE)
        count_red += variable.count(Color.RED)
        count_blue += variable.count(Color.BLUE)
        count_green += variable.count(Color.GREEN)

def tester():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, correct_scan, count_black, count_blue, count_green, count_red, count_white, count_yellow
    
    # Überprüft, ob richtig gescannt wurde.

    count_black = 0
    count_blue = 0
    count_green = 0
    count_red = 0
    count_white = 0
    count_yellow = 0
    
    scan_test(up_front_left_corner)
    scan_test(up_front_right_corner)
    scan_test(down_front_left_corner)
    scan_test(down_front_right_corner)
    scan_test(up_back_left_corner)
    scan_test(up_back_right_corner)
    scan_test(down_back_left_corner)
    scan_test(down_back_right_corner)
    scan_test(up_front_edge)
    scan_test(up_left_edge)
    scan_test(up_right_edge)
    scan_test(up_back_edge)
    scan_test(middle_back_left_edge)
    scan_test(middle_back_right_edge)
    scan_test(middle_front_left_edge)
    scan_test(middle_front_right_edge)
    scan_test(down_front_edge)
    scan_test(down_back_edge)
    scan_test(down_left_edge)
    scan_test(down_right_edge)
    if count_yellow == 8 and count_white == 8 and count_red == 8 and count_green == 8 and count_blue == 8 and count_black == 8:
        return True
    else:
        return False

def solved():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scanned_color
    
    # Überprüft, ob der Zauberwürfel fertig gelöst wurde. Dazu überprüft er, ob alle Seiten nur aus einer Farbe bestehen.

    if up_center == up_front_left_corner[0] == up_front_left_corner[0] == up_back_right_corner[0] == up_back_left_corner[0] == up_front_edge[0] == up_left_edge[0] == up_back_edge[0] == up_right_edge[0] and down_center == down_front_edge[0] == down_right_edge[0] == down_left_edge[0] == down_back_edge[0] == down_front_left_corner[0] == down_front_right_corner[0] == down_back_left_corner[0] == down_back_right_corner[0] and front_center == up_front_left_corner[1] == up_front_right_corner[2] == down_front_right_corner[1] == down_front_left_corner[2] == up_front_edge[1] == middle_front_left_edge[0] == middle_front_right_edge[0] == down_front_edge[1] and back_center == up_back_edge[1] == down_back_edge[1] == middle_back_left_edge[0] == middle_back_right_edge[0] == up_back_left_corner[2] == up_back_right_corner[1] == down_back_left_corner[1] == down_back_right_corner[2] and left_center == up_left_edge[1] == down_left_edge[1] == middle_back_left_edge[1] == middle_front_left_edge[1] == up_front_left_corner[2] == up_back_left_corner[1] == down_front_left_corner[1] == down_back_left_corner[2] and right_center == up_right_edge[1] == down_right_edge[1] == middle_front_right_edge[1] == middle_back_right_edge[1] == up_front_right_corner[1] == up_back_right_corner[2] == down_back_right_corner[1] == down_front_right_corner[2]:
        is_solved = True	
        return True

    else:
        is_solved = False
        return False

def getColor():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor
    
    rgb = [0, 0, 0]
    rgb_wert = []

    # RGB Werte des GAN 365i stickerless (gemessen)
    # 1 = ORANGE/SCHWARZ
    # 2 = BLAU
    # 3 = GRÜN
    # 4 = GELB
    # 5 = ROT
    # 6 = WEISS

    ROT    = [45.95,38.19,27.46]
    BLAU   = [ 7.84,26.57,80.45]
    GRUEN  = [ 8.72,41.70,96.45]
    GELB   = [64.97,78.21,100.0]
    ORANGE = [51.21,73.73,100.0]
    WEISS  = [78.42,92.02,100.0]

    COLORS = [ORANGE, BLAU, GRUEN, GELB, ROT, WEISS]
    COLORS_TXT = ["Orange","Blau","Gruen","Gelb","Rot","Weiss"]

    # Mittelwert aus 25 Messungen berechnen
    for i in range(25):
        rgb_wert = scan.rgb()
        for j in range(3):
            rgb[j] += rgb_wert[j]
    for i in range(3):
        rgb[i] /= 25

    # Abstände zu sechs Farben berechnen
    Abstand = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        Abstand[i] = (COLORS[i][0] - rgb[0]) ** 2 + (COLORS[i][1] - rgb[1]) ** 2 + (COLORS[i][2] - rgb[2]) ** 2

    # kleinster Abstand wird herausgefunden
    scannedColor = 0
    for i in range(5):
        if Abstand[i + 1] < Abstand[scannedColor]:
            scannedColor = i + 1
    print(COLORS_TXT[scannedColor])
    print(rgb)
    print(Abstand)
    print(Abstand[scannedColor])
    print("-------------------------------------------------")

    return scannedColor + 1

def check_angle():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor
    
    # Der Roboter checkt, ob die rotation Fläche richtig gedreht wurde und dreht ggf. auf die richtige Position.
    rotation_angle = rotation.angle() % 90

    if not rotation_angle == 0:
        if rotation_angle > 45:
            rotation.run_angle(50, 90 - rotation_angle, Stop.HOLD)
        elif rotation_angle < 45:
            rotation.run_angle(50, -1 * rotation_angle, Stop.HOLD)

    rotation_angle = 0
    rotation.reset_angle(0)

def step_begin(text):
    # Schreibt, bevor ein Schritt ausgeführt wird, den Name des Schrittes.
    moves.append(text)
    moves.append("\n")

def step_finished():
    global move, moves

    # Wartet zwischen den Schritten, bis ein Knopf gedrückt wird. 
    moves.append("\n")
    if move:
        brick.sound.beep(1000, 500)
        while not any(brick.buttons()):
            wait(10)
        rotation.reset_angle(0)

def calibrate():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor

    # Kalibrieren.
   
    brick.light(Color.RED)

    brick.display.text("Kalibrieren", [60, 60])

    arm.run_until_stalled(100, Stop.HOLD, 50)
    arm.run_angle(100, -90)
    arm.reset_angle(0)

    color.run(100)
    wait(4000)
    color.stop()
    wait(500)
    color.reset_angle(0)

    rotation.reset_angle(0)

    brick.light(Color.YELLOW)

    # Warten bis der Center-Knopf gedrückt wird um anzufangen.

    print("Bitte legen sie den Zauberwürfel ein und drücken Sie anschließend eine Taste.")
    brick.display.clear()
    brick.display.text("Warten...", [60, 60])

    while not any(brick.buttons()):
        wait(10)
    rotation.reset_angle(0)

    brick.light(Color.GREEN)

    print("Danke!")
    brick.display.clear()
    brick.display.text("Dreht sich auf die", [60, 60])
    brick.display.text("korrekte Position...", [60, 60])

def turn_correctly():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor

    # Den ganzen Zauberwürfel scannen.
    # Die mittlere Farbe oben feststellen

    color.run_angle(100, -90, Stop.HOLD)
    up_center = getColor()
    color.run_angle(100, 90, Stop.HOLD)

    # Den Zauberwürfel auf die weiße Seite drehen (Gelb oben).

    while not up_center == Color.YELLOW:
        if not up_center == Color.WHITE:
            turn()
            color.run_angle(100, -90, Stop.HOLD)
            up_center = getColor()
            color.run_angle(100, 90, Stop.HOLD)
            if not up_center == Color.YELLOW and not up_center == Color.WHITE:
                if random.randint(1,2) == 1:
                    rotate_clockwise()
                else:
                    rotate_counterclockwise()
                turn()
                color.run_angle(100, -90, Stop.HOLD)
                up_center = getColor()
                color.run_angle(100, 90, Stop.HOLD)

        if up_center == Color.WHITE:
            turn()
            color.run_angle(100, -90, Stop.HOLD)
            up_center = getColor()
            color.run_angle(100, 90, Stop.HOLD)
            turn()
            color.run_angle(100, -90, Stop.HOLD)
            up_center = getColor()
            color.run_angle(100, 90, Stop.HOLD)

    # Dreht die rote Seite nach vorne und legt die anderen Seiten fest.

    if front_center == 0:
        turn()
        color.run_angle(100, -90, Stop.HOLD)
        up_center = getColor()
        color.run_angle(100, 90, Stop.HOLD)
        rotate_2()
        turn()

    if front_center == Color.BLACK:
        rotate_2()

    elif front_center == Color.GREEN:
        rotate_counterclockwise()

    elif front_center == Color.BLUE:
        rotate_clockwise()

    brick.sound.beep(1000, 10, 50)
    brick.display.clear()
    brick.display.text("Scannt...", [60, 60])

    up_center = Color.YELLOW
    down_center = Color.WHITE
    front_center = Color.RED
    back_center = Color.BLACK
    left_center = Color.BLUE
    right_center = Color.GREEN

def scan_cube():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor, correct_scan, ROTATION_SPEED, ROTATION_SPEED_SOLVE, deltaAngle

    # Der Roboter scannt den Zauberwürfel und checkt, ob er richtig gescannt hat. Wenn nicht, dann versucht er es noch einmal.

    while not correct_scan:

        # Der Roboter scannt die gelbe Seite.

        color.run(75)
        wait(1000)
        color.stop()

        color.run_angle(75, -60)
        up_back_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_left_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_left_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_left_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_front_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_right_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_right_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_right_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        # Der Roboter scannt die schwarze/orangene Seite.

        independent_turn()

        color.run_angle(75, -45)
        down_back_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_left_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_back_left_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_left_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_back_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_right_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_back_right_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_right_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        # Der Roboter scannt die weiße Seite.

        independent_turn()

        color.run_angle(75, -45)
        down_front_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_left_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_left_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_left_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_back_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_right_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_right_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_right_corner[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        # Der Roboter scannt die rote Seite.

        independent_turn()

        color.run_angle(75, -45)
        up_front_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_left_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_front_left_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_left_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_front_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_right_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_front_right_edge[0] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_right_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        # Der Roboter scannt die blaue Seite.

        independent_rotate_clockwise()
        independent_turn()

        color.run_angle(75, -45)
        middle_back_left_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_left_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_left_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_left_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_front_left_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_left_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_left_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_left_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        # Der Roboter scannt die grüne Seite.

        independent_turn()
        independent_turn()

        color.run_angle(75, -45)
        middle_front_right_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_front_right_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        down_right_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        down_back_right_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        middle_back_right_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_back_right_corner[2] = getColor()
        rotation.run_angle(ROTATION_SPEED, 45)
        color.run_angle(50, -COLOR_ANGLE)
        up_right_edge[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 44.75)
        color.run_angle(50, COLOR_ANGLE)
        up_front_right_corner[1] = getColor()
        rotation.run_angle(ROTATION_SPEED, 43)
        color.run(75)
        wait(1000)
        color.stop()
        check_angle()

        independent_rotate_counterclockwise()
        independent_turn()
        independent_rotate_counterclockwise()

        check_angle()
        
        print("up_center:")
        print(up_center)
        print("front_center:")
        print(front_center)
        print("down_center:")
        print(down_center)
        print("back_center:")
        print(back_center)
        print("left_center:")
        print(left_center)
        print("right_center:")
        print(right_center)
        print("up_front_left_corner:")
        print(up_front_left_corner)
        print("up_front_right_corner:")
        print(up_front_right_corner)
        print("up_back_right_corner:")
        print(up_back_right_corner)
        print("up_back_left_corner:")
        print(up_back_left_corner)
        print("down_front_left_corner:")
        print(down_front_left_corner)
        print("down_front_right_corner:")
        print(down_front_right_corner)
        print("down_back_right_corner:")
        print(down_back_right_corner)
        print("down_back_left_corner:")
        print(down_back_left_corner)
        print("up_front_edge:")
        print(up_front_edge)
        print("up_right_edge:")
        print(up_right_edge)
        print("up_left_edge:")
        print(up_left_edge)
        print("up_back_edge:")
        print(up_back_edge)
        print("middle_front_left_edge:")
        print(middle_front_left_edge)
        print("middle_front_right_edge:")
        print(middle_front_right_edge)
        print("middle_back_right_edge:")
        print(middle_back_right_edge)
        print("middle_back_left_edge:")
        print(middle_back_left_edge)
        print("down_front_edge:")
        print(down_front_edge)
        print("down_right_edge:")
        print(down_right_edge)
        print("down_left_edge:")
        print(down_left_edge)
        print("down_back_edge:")
        print(down_back_edge)
        
        # Checkt ob richtig gescannt wurde, d.h. er korrigiert ob jede Farbe so oft drankommt, wie sie auch sollte.

        if tester():
            correct_scan = True
            brick.display.clear()
            brick.display.text("Fertig gescannt", [60, 60])
            print("Fertig gescannt!")

        print("count_black:")
        print(count_black)
        print("count_blue:")
        print(count_blue)
        print("count_green:")
        print(count_green)
        print("count_red:")
        print(count_red)
        print("count_white:")
        print(count_white)
        print("count_yellow:")
        print(count_yellow)

def CFOP(): 
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge, count_black, count_blue, count_green, count_red, count_white, count_yellow, is_solved, scannedColor, correct_scan

    # Der Zauberwürfel wird gelöst.

    while not solved():   

        # Die weißen Kantensteine werden gelöst.
        # Cross

        if not solved():
            
            # Die weiß-rote Kante wird an seinen richtigen Platz gebracht. 
            # Dazu findet der Roboter zuerst du Position heraus und bringt dann Die Kante an die Stelle über der Richtigen. 
            # Anschließend wird die Kante eingedreht.

            step_begin("Cross:")
            
            searched_stone = find_brick([Color.WHITE, Color.RED])

            if searched_stone[0] == "down_back_edge":
                B2()
                U2()
            elif searched_stone[0] == "down_left_edge":
                L2()
                Ui()
            elif searched_stone[0] == "down_right_edge":
                R2()
                U()
            elif searched_stone[0] == "middle_front_left_edge":
                F()
            elif searched_stone[0] == "middle_front_right_edge":
                Fi()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
                Ui()
            elif searched_stone[0] == "middle_back_right_edge":
                Ri()
                U()
            elif searched_stone[0] == "up_back_edge":
                U2()
            elif searched_stone[0] == "up_right_edge":
                U()
            elif searched_stone[0] == "up_left_edge":
                Ui()

            check_angle()
            
            # Der Roboter checkt, wie die Kante ausgerichtet ist und wo sie ist und dreht sie anschließend ein.

            searched_stone = find_brick([Color.WHITE, Color.RED])

            if not searched_stone[0] == "down_front_edge":
                if searched_stone[1] == Color.WHITE:
                    F2()
                else:
                    U()
                    L()
                    Fi()
            
            else:
                if searched_stone[1] == Color.RED:
                    F2()
                    U()
                    L()
                    Fi()

            check_angle()

            step_finished()

            # Die weiß-blaue Kante wird an seinen richtigen Platz gebracht. 
            # Dazu findet der Roboter zuerst du Position heraus und bringt dann Die Kante an die Stelle über der Richtigen. 
            # Anschließend wird die Kante eingedreht.

            searched_stone = find_brick([Color.WHITE, Color.BLUE])

            if searched_stone[0] == "up_front_edge":
                U()
            elif searched_stone[0] == "up_back_edge":
                Ui()
            elif searched_stone[0] == "up_right_edge":
                U2()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
            elif searched_stone[0] == "middle_back_right_edge":
                Ri()
                U2()
            elif searched_stone[0] == "middle_front_left_edge":
                Li()
            elif searched_stone[0] == "middle_front_right_edge":
                R()
                U2()
            elif searched_stone[0] == "down_back_edge":
                B2()
                Ui()
            elif searched_stone[0] == "down_right_edge":
                R2()
                U2()
            
            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.BLUE])

            # Der Roboter checkt, wie die Kante ausgerichtet ist und wo sie ist und dreht sie anschließend ein.

            if not searched_stone[0] == "down_left_edge":
                if searched_stone[1] == Color.BLUE:
                    U()
                    B()
                    Li()
                else:
                    L2()

            else:
                if not searched_stone[1] == Color.WHITE:
                    L2()
                    U()
                    B()
                    Li()

            check_angle()

            step_finished()

            # Die weiß-orangene Kante wird an seinen richtigen Platz gebracht. 
            # Dazu findet der Roboter zuerst du Position heraus und bringt dann Die Kante an die Stelle über der Richtigen. 
            # Anschließend wird die Kante eingedreht.

            searched_stone = find_brick([Color.WHITE, Color.BLACK])

            if searched_stone[0] == "up_front_edge":
                U2()
            elif searched_stone[0] == "up_right_edge":
                Ui()
            elif searched_stone[0] == "up_left_edge":
                U()
            elif searched_stone[0] == "middle_back_left_edge":
                Bi()
            elif searched_stone[0] == "middle_back_right_edge":
                B()
            elif searched_stone[0] == "middle_front_left_edge":
                F()
                U2()
                Fi()
            elif searched_stone[0] == "middle_front_right_edge":
                Fi()
                U2()
                F()
            elif searched_stone[0] == "down_right_edge":
                R2()
                Ui()
            
            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.BLACK])

            # Der Roboter checkt, wie die Kante ausgerichtet ist und wo sie ist und dreht sie anschließend ein.

            if not searched_stone[0] == "down_back_edge":
                if searched_stone[1] == Color.BLACK:
                    U()
                    R()
                    Bi()
                else:
                    B2()
            
            elif not searched_stone[1] == Color.WHITE:
                B2()
                U()
                R()
                Bi()

            check_angle()

            step_finished()

            # Die weiß-grüne Kante wird an seinen richtigen Platz gebracht. 
            # Dazu findet der Roboter zuerst du Position heraus und bringt dann Die Kante an die Stelle über der Richtigen. 
            # Anschließend wird die Kante eingedreht.

            searched_stone = find_brick([Color.WHITE, Color.GREEN])

            if searched_stone[0] == "up_front_edge":
                Ui()
            elif searched_stone[0] == "up_left_edge":
                U2()
            elif searched_stone[0] == "up_back_edge":
                U()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
                U2()
                Li()
            elif searched_stone[0] == "middle_back_right_edge":
                Ri()
            elif searched_stone[0] == "middle_front_left_edge":
                F()
                Ui()
                Fi()
            elif searched_stone[0] == "middle_front_right_edge":
                R()
            
            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.GREEN])

            # Der Roboter checkt, wie die Kante ausgerichtet ist und wo sie ist und dreht sie anschließend ein.

            if not searched_stone[0] == "down_right_edge":
                if searched_stone[1] == Color.GREEN:
                    U()
                    F()
                    Ri()
                    Fi()
                else:
                    R2()
            
            elif searched_stone[1] == Color.GREEN:
                R()
                Fi()
                Ui()
                F()
                R2()
            

            check_angle()

            step_finished()

        # Die weißen Ecksteine werden gelöst.
        # F2L first look

        if not solved():

            # Die weiß-rot-grüne Ecke wird an seinen richtigen Platz gebracht. 
            # Der Roboter sucht sich die Position dieses Steins heraus und sucht sich dann den richtigen Algorithmus.

            step_begin("F2L (first look):")

            searched_stone = find_brick([Color.WHITE, Color.RED, Color.GREEN])

            if searched_stone[0] == "up_back_right_corner":
                U()
            elif searched_stone[0] == "up_back_left_corner":
                U2()
            elif searched_stone[0] == "up_front_left_corner":
                Ui()
            elif searched_stone[0] == "down_back_right_corner":
                Ri()
                Ui()
                R()
                U2()
            elif searched_stone[0] == "down_back_left_corner":
                L()
                U2()
                Li()
            elif searched_stone[0] == "down_front_left_corner":
                Li()
                Ui()
                L()
            elif searched_stone[0] == "down_front_right_corner" and not searched_stone[1] == Color.WHITE:
                R()
                U()
                Ri()
                Ui()

            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.RED, Color.GREEN])

            # Jetzt überprüft der Roboter, wie die Ecke gedreht ist und versucht die Ecke anschließend richtig einzudrehen. 
            # Falls die Ecke schon falsch drin ist wird sie durch einen entsprechenden Algorithmus heringedreht.

            if searched_stone[0] == "up_front_right_corner":
                if searched_stone[1] == Color.RED:
                    U()
                    R()
                    Ui()
                    Ri()
                elif searched_stone[1] == Color.GREEN:
                    R()
                    U()
                    Ri()
                elif searched_stone[1] == Color.WHITE:
                    R()
                    U2()
                    Ri()
                    Ui()
                    R()
                    U()
                    Ri()  

            check_angle()

            step_finished()

            # Die weiß-blau-rote Ecke wird an seinen richtigen Platz gebracht. 
            # Der Roboter sucht sich die Position dieses Steins heraus und sucht sich dann den richtigen Algorithmus.

            searched_stone = find_brick([Color.WHITE, Color.BLUE, Color.RED])

            if searched_stone[0] == "up_back_right_corner":
                U2()
            elif searched_stone[0] == "up_back_left_corner":
                Ui()
            elif searched_stone[0] == "up_front_right_corner":
                U()
            elif searched_stone[0] == "down_back_right_corner":
                Ri()
                U2()
                R()
            elif searched_stone[0] == "down_back_left_corner":
                L()
                U() 
                Li()
                U2()
            elif searched_stone[0] == "down_front_left_corner" and not searched_stone[1] == Color.WHITE:
                F()
                U()
                Fi()
                Ui()

            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.BLUE, Color.RED])

            # Jetzt überprüft der Roboter, wie die Ecke gedreht ist und versucht die Ecke anschließend richtig einzudrehen. 
            # Falls die Ecke schon falsch drin ist wird sie durch einen entsprechenden Algorithmus heringedreht.

            if searched_stone[0] == "up_front_left_corner":
                if searched_stone[1] == Color.RED:
                    F()
                    U()
                    Fi()
                elif searched_stone[1] == Color.BLUE:
                    Li()
                    Ui()
                    L()
                elif searched_stone[1] == Color.WHITE:
                    F()
                    U2()
                    Fi()
                    Ui()
                    F()
                    U()
                    Fi()

            check_angle()

    	    step_finished()

            # Der weiß-blau-schwarze Eckstein wird an seinen richtigen Platz gebracht. 
            # Der Roboter sucht sich die Position dieses Steins heraus und sucht sich dann den richtigen Algorithmus.

            searched_stone = find_brick([Color.WHITE, Color.BLACK, Color.BLUE])

            if searched_stone[0] == "up_front_left_corner":
                U()
            elif searched_stone[0] == "up_front_right_corner":
                U2()
            elif searched_stone[0] == "up_back_right_corner":
                Ui()
            elif searched_stone[0] == "down_back_right_corner":
                Ri()
                Ui()
                R()
            elif searched_stone[0] == "down_back_left_corner" and not searched_stone[1] == Color.WHITE:
                L()
                U()
                Li()
                Ui()

            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.BLACK, Color.BLUE])

            # Jetzt überprüft der Roboter, wie die Ecke gedreht ist und versucht die Ecke anschließend richtig einzudrehen. 
            # Falls die Ecke schon falsch drin ist wird sie durch einen entsprechenden Algorithmus heringedreht.

            if searched_stone[0] == "up_back_left_corner":
                if searched_stone[1] == Color.BLUE:
                    L()
                    U()
                    Li()
                elif searched_stone[1] == Color.BLACK:
                    Bi()
                    Ui()
                    B()
                elif searched_stone[1] == Color.WHITE:
                    L()
                    Ui()
                    Li()
                    U2()
                    L()
                    U()
                    Li()
            
            check_angle()

            step_finished()

            # Der weiß-grün-schwarze Eckstein wird an seinen richtigen Platz gebracht. 
            # Der Roboter sucht sich die Position dieses Steins heraus und sucht sich dann den richtigen Algorithmus.

            searched_stone = find_brick([Color.WHITE, Color.GREEN, Color.BLACK])

            if searched_stone[0] == "up_front_left_corner":
                U2()
            elif searched_stone[0] == "up_front_right_corner":
                Ui()
            elif searched_stone[0] == "up_back_left_corner":
                U()
            elif searched_stone[0] == "down_back_right_corner" and not searched_stone[1] == Color.WHITE:
                Ri()
                Ui()
                R()
                U()
            
            check_angle()

            searched_stone = find_brick([Color.WHITE, Color.GREEN, Color.BLACK])

            # Jetzt überprüft der Roboter, wie die Ecke gedreht ist und versucht die Ecke anschließend richtig einzudrehen. 
            # Falls die Ecke schon falsch drin ist wird sie durch einen entsprechenden Algorithmus heringedreht.

            if searched_stone[0] == "up_back_right_corner":
                if searched_stone[1] == Color.WHITE:
                    Ri()
                    U()
                    R()
                    U2()
                    Ri()
                    Ui()
                    R()
                elif searched_stone[1] == Color.GREEN:
                    Ri()
                    Ui()
                    R()
                elif searched_stone[1] == Color.BLACK:
                    B()
                    U()
                    Bi()

            check_angle()

            step_finished()
            
        # Die middle-Ecksteine werden gelöst.
        # F2L second look
        
        if not solved():
            
            # Der rot-blaue Eckstein wird an seinen richtigen Platz gebracht. 
            # Sie wird dazu zuerst an die Stelle über der passenden Stelle platziert.

            step_begin("F2L (second look):")

            searched_stone = find_brick([Color.RED, Color.BLUE])

            if searched_stone[0] == "middle_front_right_edge":
                R()
                Ui()
                Ri()
                Ui()
                Fi()
                U()
                F()
                U2()
            elif searched_stone[0] == "middle_back_right_edge":
                B()
                Ui()
                Bi()
                Ui()
                Ri()
                U()
                R()
                Ui()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
                Ui()
                Li()
                Ui()
                Bi()
                U()
                B()
            elif searched_stone[0] == "up_right_edge":
                U()
            elif searched_stone[0] == "up_left_edge":
                Ui()
            elif searched_stone[0] == "up_back_edge":
                U2()
            elif searched_stone[0] == "middle_front_left_edge" and searched_stone[1] == Color.BLUE:
                F()
                Ui()
                Fi()
                U()
                Li()
                U2()
                L()
                U2()
                Li()
                U()
                L()

            check_angle()

            searched_stone = find_brick([Color.RED, Color.BLUE])

            # Wenn der Kantenstein an der Stelle über der passneden ist, wird der richtige Algorithmus ausgeführt.

            if searched_stone[0] == "up_front_edge" and searched_stone[1] == Color.RED:
                U2()
                F()
                U()
                Fi()
                Ui()
                Li()
                Ui()
                L()
            elif searched_stone[0] == "up_front_edge" and searched_stone[1] == Color.BLUE:
                Ui()
                Li()
                Ui()
                L()
                U()
                F()
                U()
                Fi()

            check_angle()

            step_finished()

            # Der rot-grüne Eckstein wird an seinen richtigen Platz gebracht.
            # Sie wird dazu zuerst an die Stelle über der passenden Stelle platziert.

            searched_stone = find_brick([Color.RED, Color.GREEN])

            if searched_stone[0] == "middle_front_right_edge" and searched_stone[1] == Color.GREEN:
                R()
                Ui()
                Ri()
                U()
                Fi()
                U2()
                F()
                U2()
                Fi()
                U()
                F()
            elif searched_stone[0] == "middle_back_right_edge":
                B()
                Ui()
                Bi()
                Ui()
                Ri()
                U()
                R()
                U2()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
                Ui()
                Li()
                Ui()
                Bi()
                U()
                B()
                Ui()
            elif searched_stone[0] == "up_front_edge":
                Ui()
            elif searched_stone[0] == "up_left_edge":
                U2()
            elif searched_stone[0] == "up_back_edge":
                U()
            
            check_angle()

            searched_stone = find_brick([Color.RED, Color.GREEN])

            # Wenn der Kantenstein an der Stelle über der passneden ist, wird der richtige Algorithmus ausgeführt.

            if searched_stone[0] == "up_right_edge" and searched_stone[1] == Color.RED:
                Ui()
                Fi()
                Ui()
                F()
                U()
                R()
                U()
                Ri()
            elif searched_stone[0] == "up_right_edge" and searched_stone[1] == Color.GREEN:
                U2()
                R()
                U()
                Ri()
                Ui()
                Fi()
                Ui()
                F()
            
            check_angle()

            step_finished()

            # Der schwarz-grüne Eckstein wird an seinen richtigen Platz gebracht.
            # Sie wird dazu zuerst an die Stelle über der passenden Stelle platziert.

            searched_stone = find_brick([Color.BLACK, Color.GREEN])

            if searched_stone[0] == "middle_back_right_edge" and searched_stone[1] == Color.GREEN:
                B()
                Ui()
                Bi()
                U()
                Ri()
                U2()
                R()
                U2()
                Ri()
                U()
                R()
            elif searched_stone[0] == "middle_back_left_edge":
                L()
                Ui()
                Li()
                Ui()
                Bi()
                U()
                B()
                U2()
            elif searched_stone[0] == "up_front_edge":
                U2()
            elif searched_stone[0] == "up_left_edge":
                U()
            elif searched_stone[0] == "up_right_edge":
                Ui()

            check_angle()

            searched_stone = find_brick([Color.BLACK, Color.GREEN])

            # Wenn der Kantenstein an der Stelle über der passneden ist, wird der richtige Algorithmus ausgeführt.

            if searched_stone[0] == "up_back_edge" and searched_stone[1] == Color.BLACK:
                U2()
                B()
                U()
                Bi()
                Ui()
                Ri()
                Ui()
                R()
            elif searched_stone[0] == "up_back_edge" and searched_stone[1] == Color.GREEN:
                Ui()
                Ri()
                Ui()
                R()
                U()
                B()
                U()
                Bi()

            check_angle()

            step_finished()

            # Der schwarz-blaue Eckstein wird an seinen richigen Platz gebracht.
            # Sie wird dazu zuerst an die Stelle über der passenden Stelle platziert.

            searched_stone = find_brick([Color.BLACK, Color.BLUE])

            if searched_stone[0] == "middle_back_left_edge" and searched_stone[1] == Color.BLUE:
                L()
                Ui()
                Li()
                U()
                Bi()
                U2()
                B()
                U2()
                Bi()
                U()
                B()
            elif searched_stone[0] == "up_front_edge":
                U()
            elif searched_stone[0] == "up_back_edge":
                Ui()
            elif searched_stone[0] == "up_right_edge":
                U2()

            searched_stone = find_brick([Color.BLACK, Color.BLUE])

            # Wenn der Kantenstein an der Stelle über der passneden ist, wird der richtige Algorithmus ausgeführt.

            if searched_stone[0] == "up_left_edge" and searched_stone[1] == Color.BLACK:
                Ui()
                Bi()
                Ui()
                B()
                U()
                L()
                U()
                Li()
            elif searched_stone[0] == "up_left_edge" and searched_stone[1] == Color.BLUE:
                U2()
                L()
                U()
                Li()
                Ui()
                Bi()
                Ui()
                B()

            check_angle()

            step_finished()

        # Die gelben Kanten werden auf die richtige Seite geflippt.
        # OLL first look

        if not solved():
            
            # Es wird überprüft, wieviele gelbe Kantensteine auf der gelben Seite mit Gelb nach oben zeigen und daraus wird errechnet, 
            # welchen Move der Roboter machen muss.

            step_begin("OLL (first look):")

            yellow_edges = 0
            if up_back_edge[0] == Color.YELLOW:
                yellow_edges += 1
            if up_left_edge[0] == Color.YELLOW:
                yellow_edges += 1
            if up_right_edge[0] == Color.YELLOW:
                yellow_edges += 1
            if up_front_edge[0] == Color.YELLOW:
                yellow_edges += 1
            
            if yellow_edges == 0:
                # Wenn keine gelbe Seite eines Kantensteins nach oben schaut, dann kommt der folgende Algorythmus.

                F()
                R()
                U()
                Ri()
                Ui()
                Fi()
                U2()
                F()
                U()
                R()
                Ui()
                Ri()
                Fi()
            
            elif yellow_edges == 2:
                # Wenn zwei gelbe Seiten von irgendwelchen Kantensteinen nach oben schauen, dann wird überprüft,
                # ob sie in einer Reihe angeordnet sind oder in einem Eck. Daraus schließt sich der Algorithmus.
                
                if up_front_edge[0] == Color.YELLOW and up_back_edge[0] == Color.YELLOW:
                    U()
                    F()
                    R()
                    U()
                    Ri()
                    Ui()
                    Fi()
                
                elif up_left_edge[0] == Color.YELLOW and up_right_edge[0] == Color.YELLOW:
                    F()
                    R()
                    U()
                    Ri()
                    Ui()
                    Fi()
                
                else:
                    while not (up_back_edge[0] == Color.YELLOW and up_left_edge[0] == Color.YELLOW):
                        # AUF
                        U()
                    
                    F()
                    U()
                    R()
                    Ui()
                    Ri()
                    Fi()
                    

            step_finished()

        # Die gelben Ecken werden auf die richtige Seite geflippt.
        # OLL second look

        if not solved():
        
            # Es wird gecheckt wieviele gelbe Ecksteine mit gelb nach oben gucken. Danach macht der Roboter eine Fallunterscheidung, 
            # um den richtigen OLL-Algorithmus auszuführen

            step_begin("OLL (second look):")

            yellow_corners = 0
            if up_front_left_corner[0] == Color.YELLOW:
                yellow_corners += 1
            if up_front_right_corner[0] == Color.YELLOW:
                yellow_corners += 1
            if up_back_left_corner[0] == Color.YELLOW:
                yellow_corners += 1
            if up_back_right_corner[0] == Color.YELLOW:
                yellow_corners += 1
            
            if yellow_corners == 0:

                # Möglichkeiten, dass keine obere Ecke gelb ist (2) und deren Lösungsalgorithmus.

                if (up_front_left_corner[1] == Color.YELLOW and up_front_right_corner[2] == Color.YELLOW and up_back_left_corner[2] == Color.YELLOW and up_back_right_corner[1] == Color.YELLOW) or (up_back_right_corner[2] == Color.YELLOW and up_back_left_corner[1] == Color.YELLOW and up_front_left_corner[2] == Color.YELLOW and up_front_right_corner[1] == Color.YELLOW):
                    while not up_front_right_corner[2] == Color.YELLOW:
                        # AUF
                        U()
                    
                    F()
                    for i in range(3):
                        R()
                        U()
                        Ri()
                        Ui()
                    Fi()
                
                else:
                    while not (up_front_right_corner[2] == Color.YELLOW and (not up_front_left_corner[1] == Color.YELLOW)):

                        # AUF for OLL.
                        U()
                    R()
                    U2()
                    R2()
                    Ui()
                    R2()
                    Ui()
                    R2()
                    U2()
                    R()

            if yellow_corners == 1:

                # Möglichkeiten, dass eine obere Ecke gelb ist (2) und deren Lösungsalgorithmus (Parallelalgorithhmus zu Sune und dessen Gegenalgorithmus).

                while not up_front_left_corner[0] == Color.YELLOW:
                    # AUF
                    U()
                
                if up_front_right_corner[2] == Color.YELLOW:
                    R()
                    Ui()
                    Li()
                    U()
                    Ri()
                    Ui()
                    L()
                
                else:
                    Ui()
                    Li()
                    U()
                    R()
                    Ui()
                    L()
                    U()
                    Ri()
                
            if yellow_corners == 2:

                # Möglichkeiten, dass 2 gelbe Ecken oben sind (3) und deren Lösungsalgorithmus.

                if (up_front_left_corner[0] == Color.YELLOW and up_back_right_corner[0] == Color.YELLOW) or (up_back_left_corner[0] == Color.YELLOW and up_front_right_corner[0] == Color.YELLOW):
                    while not up_front_left_corner[1] == Color.YELLOW:
                        # AUF
                        U()

                    Ri()
                    F()
                    R()
                    Bi()
                    Ri()
                    Fi()
                    R()
                    B()
                
                else:
                    while not up_front_left_corner[1] == Color.YELLOW:
                        # AUF
                        U()

                    if up_front_right_corner[2] == Color.YELLOW:
                        R2()
                        D()
                        Ri()
                        U2()
                        R()
                        Di()
                        Ri()
                        U2()
                        Ri()
                    
                    else:
                        L()
                        F()
                        Ri()
                        Fi()
                        Li()
                        F()
                        R()
                        Fi()

            step_finished()

        # Die gelben Ecken werden auf den richtigen Platz gebracht.
        # first look PLL

        if not solved():

            # Der Roboter versucht alle 4 gelben Ecksteine in das richtige Verhältnis zueinander zu bringen.
            # Der Roboter bringt ein schon fertiges Paar (die Farben an der Seite sind bei beiden gleich) nach links.
            # Wenn es kein Paar gibt, wird der Algorithmus einmal durchgeführt.

            if not (up_front_right_corner[1] == up_back_right_corner[2] and up_front_left_corner[2] == up_back_left_corner[1]):
                
                step_begin("PLL (first look):")

                good_corners = False

                if up_front_right_corner[2] == up_front_left_corner[1]:
                    good_corners = True
                    U()
                elif up_front_right_corner[1] == up_back_right_corner[2]:
                    good_corners = True
                    U2()
                elif up_back_right_corner[1] == up_back_left_corner[2]:
                    good_corners = True
                    Ui()
                elif up_back_left_corner[1] == up_front_right_corner[2]:
                    good_corners = True
                else:
                    F()
                    R()
                    Ui()
                    Ri()
                    Ui()
                    R()
                    U()
                    Ri()
                    Fi()
                    R()
                    U()
                    Ri()
                    Ui()
                    Ri()
                    F()
                    R()
                    Fi()

                if good_corners:
                    R()
                    U2()
                    Ri()
                    Ui()
                    R()
                    U2()
                    Li()
                    U()
                    Ri()
                    Ui()
                    L()

                step_finished()

        # Gelbe Kantensteine werden auf den richtigen Platz gebracht.
        # second look PLL

        if not solved():

            # Der Roboter versucht die 4 gelben Kantensteinen ins richtige Verhältnis mit den gelben Ecksteinen zu bringen.
            # Roboter sucht eine passende Kante und bringt diese nach hinten. Wenn es keine gibt, wird ein anderer Algorithmus durchgeführt.
            # Der Roboter überprüft außerdem, in welche Richtung er den oberen Layer drehen muss, falls der 3-Cycle-Fall eintritt.
            # Macht das ganze aber nur, wenn noch nicht alles außer AUF gelöst wurde. 

            if not (up_front_edge[1] == up_front_left_corner[1] and up_right_edge[1] == up_front_right_corner[1]):
                
                step_begin("PLL (second_look):")

                if up_front_edge[1] == up_front_left_corner[1] or up_right_edge[1] == up_front_right_corner[1] or up_back_edge[1] == up_back_right_corner[1] or up_left_edge[1] == up_back_left_corner[1]:
                
                    # Überprüft, an welcher Stelle der Zauberwürfel schon eine gelöste Kante hat.

                    if up_front_right_corner[1] == up_right_edge[1]:
                        Ui()
                    elif up_front_left_corner[1] == up_front_edge[1]:
                        U2()
                    elif up_back_left_corner[1] == up_left_edge[1]:
                        U()

                    # Roboter checkt, in welche Richtung er cyclen muss. Dann führt er den passenden Algorithmus aus.
                    
                    cycle_to_the_left = True
                    if up_front_edge[1] == up_front_right_corner[1]:
                        cycle_to_the_left = False

                    U2()
                    M2()
                    if cycle_to_the_left:
                        Di()
                    else:
                        D()
                    Mi()
                    B2()
                    M()
                    if cycle_to_the_left:
                        Di()
                    else:
                        D()
                    M2()

                else:

                    # Roboter findet den richtigen Algorithmus.

                    if up_front_edge[1] == up_back_right_corner[1]:
                        M2()
                        Di()
                        M2()
                        U2()
                        M2()
                        Di()
                        M2()
                    
                    else:
                        if up_front_edge[1] == up_front_right_corner[1]:
                            Mi()
                            Fi()
                            M2()
                            Bi()
                            M2()
                            Fi()
                            Mi()
                            D2()
                            M2()

                        elif up_front_edge[1] == up_back_left_corner[1]:
                            Mi()
                            F()
                            M2()
                            B()
                            M2()
                            F()
                            Mi()
                            D2()
                            M2()
                            
                
            step_finished()

        # Der Roboter dreht den oberen Layer, bis der ganze Zauberwürfel gelöst ist.
        # AUF (Adjust Upper Face)

        if not solved():
            step_begin("AUF:")

            i = 0
            while (not solved()) and i <= 3:
                i += 1
                U()

def printAlgorithm():
    
    # Diese Funktion schreibt einfach den Lösungsalgorithmus.

    print("Der Lösungsalgorithmus ist:")
    for i in range(len(moves)):
        print(moves[i], end = " ")
    
# Die Zauberwürfel-Moves, Variablen werden entsprechend verändert.
#region
def R():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLUE, 0)
        hold_rotate_counterclockwise()

    help = middle_front_right_edge
    middle_front_right_edge = down_right_edge
    down_right_edge = middle_back_right_edge
    middle_back_right_edge = up_right_edge
    up_right_edge = help

    help = up_front_right_corner
    up_front_right_corner = [down_front_right_corner[1], down_front_right_corner[2], down_front_right_corner[0]]
    down_front_right_corner = [down_back_right_corner[2], down_back_right_corner[0], down_back_right_corner[1]]
    down_back_right_corner = [up_back_right_corner[1], up_back_right_corner[2], up_back_right_corner[0]]
    up_back_right_corner = [help[2], help[0], help[1]]

    moves.append("R")

    check_angle()

def Ri():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLUE, 0)
        hold_rotate_clockwise()

    help = middle_front_right_edge
    middle_front_right_edge = up_right_edge
    up_right_edge = middle_back_right_edge
    middle_back_right_edge = down_right_edge
    down_right_edge = help

    help = up_front_right_corner
    up_front_right_corner = [up_back_right_corner[1], up_back_right_corner[2], up_back_right_corner[0]]
    up_back_right_corner = [down_back_right_corner[2], down_back_right_corner[0], down_back_right_corner[1]]
    down_back_right_corner = [down_front_right_corner[1], down_front_right_corner[2], down_front_right_corner[0]]
    down_front_right_corner = [help[2], help[0], help[1]]

    moves.append("R'")

    check_angle()

def R2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:    
        turn_right_direction(Color.BLUE, 0)
        hold_rotate2()

    help = down_right_edge
    down_right_edge = up_right_edge
    up_right_edge = help

    help = middle_front_right_edge
    middle_front_right_edge = middle_back_right_edge
    middle_back_right_edge = help

    help = up_front_right_corner
    up_front_right_corner = down_back_right_corner
    down_back_right_corner = help

    help = up_back_right_corner
    up_back_right_corner = down_front_right_corner
    down_front_right_corner = help

    moves.append("R2")

    check_angle()
    
def U():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.WHITE, 0)
        hold_rotate_counterclockwise()

    help = up_front_edge
    up_front_edge = up_right_edge
    up_right_edge = up_back_edge
    up_back_edge = up_left_edge
    up_left_edge = help

    help = up_front_right_corner
    up_front_right_corner = up_back_right_corner
    up_back_right_corner = up_back_left_corner
    up_back_left_corner = up_front_left_corner
    up_front_left_corner = help

    moves.append("U")

    check_angle()
    
def Ui():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.WHITE, 0)
        hold_rotate_clockwise()

    help = up_front_edge
    up_front_edge = up_left_edge
    up_left_edge = up_back_edge
    up_back_edge = up_right_edge
    up_right_edge = help

    help = up_front_right_corner
    up_front_right_corner = up_front_left_corner
    up_front_left_corner = up_back_left_corner
    up_back_left_corner = up_back_right_corner
    up_back_right_corner = help

    moves.append("U'")

    check_angle()
    
def U2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.WHITE, 0)
        hold_rotate2()

    help = up_front_edge
    up_front_edge = up_back_edge
    up_back_edge = help

    help = up_left_edge
    up_left_edge = up_right_edge
    up_right_edge = help

    help = up_front_left_corner
    up_front_left_corner = up_back_right_corner
    up_back_right_corner = help

    help = up_front_right_corner
    up_front_right_corner = up_back_left_corner
    up_back_left_corner = help

    moves.append("U2")

    check_angle()
    
def M():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLUE, 0)
        hold_rotate_counterclockwise()
        turn_right_direction(Color.GREEN, 0)
        hold_rotate_clockwise()

    help = up_left_edge
    up_left_edge = middle_front_left_edge
    middle_front_left_edge = down_left_edge
    down_left_edge = middle_back_left_edge
    middle_back_left_edge = help
    
    help = middle_front_right_edge
    middle_front_right_edge = down_right_edge
    down_right_edge = middle_back_right_edge
    middle_back_right_edge = up_right_edge
    up_right_edge = help

    help = up_front_left_corner
    up_front_left_corner = [down_front_left_corner[2], down_front_left_corner[0], down_front_left_corner[1]]
    down_front_left_corner = [down_back_left_corner[1], down_back_left_corner[2], down_back_left_corner[0]]
    down_back_left_corner = [up_back_left_corner[2], up_back_left_corner[0], up_back_left_corner[1]]
    up_back_left_corner = [help[1], help[2], help[0]]

    help = up_front_right_corner
    up_front_right_corner = [down_front_right_corner[1], down_front_right_corner[2], down_front_right_corner[0]]
    down_front_right_corner = [down_back_right_corner[2], down_back_right_corner[0], down_back_right_corner[1]]
    down_back_right_corner = [up_back_right_corner[1], up_back_right_corner[2], up_back_right_corner[0]]
    up_back_right_corner = [help[2], help[0], help[1]]

    moves.append("M")

    check_angle()
    
def Mi():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLUE, 0)
        hold_rotate_clockwise()
        turn_right_direction(Color.GREEN, 0)
        hold_rotate_counterclockwise()

    help = up_left_edge
    up_left_edge = middle_back_left_edge
    middle_back_left_edge = down_left_edge
    down_left_edge = middle_front_left_edge
    middle_front_left_edge = help

    help = middle_front_right_edge
    middle_front_right_edge = up_right_edge
    up_right_edge = middle_back_right_edge
    middle_back_right_edge = down_right_edge
    down_right_edge = help

    help = up_front_right_corner
    up_front_right_corner = [up_back_right_corner[1], up_back_right_corner[2], up_back_right_corner[0]]
    up_back_right_corner = [down_back_right_corner[2], down_back_right_corner[0], down_back_right_corner[1]]
    down_back_right_corner = [down_front_right_corner[1], down_front_right_corner[2], down_front_right_corner[0]]
    down_front_right_corner = [help[2], help[0], help[1]]

    help = up_front_left_corner
    up_front_left_corner = [up_back_left_corner[2], up_back_left_corner[0], up_back_left_corner[1]]
    up_back_left_corner = [down_back_left_corner[1], down_back_left_corner[2], down_back_left_corner[0]]
    down_back_left_corner = [down_front_left_corner[2], down_front_left_corner[0], down_front_left_corner[1]]
    down_front_left_corner = [help[1], help[2], help[0]]

    moves.append("M'")

    check_angle()
    
def M2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLUE, 0)
        hold_rotate2()
        turn_right_direction(Color.GREEN, 0)
        hold_rotate2()

    help = middle_back_left_edge
    middle_back_left_edge = middle_front_left_edge
    middle_front_left_edge = help

    help = down_left_edge
    down_left_edge = up_left_edge
    up_left_edge = help

    help = down_right_edge
    down_right_edge = up_right_edge
    up_right_edge = help

    help = middle_front_right_edge
    middle_front_right_edge = middle_back_right_edge
    middle_back_right_edge = help

    help = down_back_left_corner
    down_back_left_corner = up_front_left_corner
    up_front_left_corner = help

    help = down_front_left_corner
    down_front_left_corner = up_back_left_corner
    up_back_left_corner = help

    help = up_front_right_corner
    up_front_right_corner = down_back_right_corner
    down_back_right_corner = help

    help = up_back_right_corner
    up_back_right_corner = down_front_right_corner
    down_front_right_corner = help

    moves.append("M2")

    check_angle()
    
def F():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLACK, 0)
        hold_rotate_counterclockwise()

    help = up_front_edge
    up_front_edge = [middle_front_left_edge[1], middle_front_left_edge[0]]
    middle_front_left_edge = [down_front_edge[1], down_front_edge[0]]
    down_front_edge = [middle_front_right_edge[1], middle_front_right_edge[0]]
    middle_front_right_edge = [help[1], help[0]]

    help = up_front_left_corner
    up_front_left_corner = [down_front_left_corner[1], down_front_left_corner[2], down_front_left_corner[0]]
    down_front_left_corner = [down_front_right_corner[2], down_front_right_corner[0], down_front_right_corner[1]]
    down_front_right_corner = [up_front_right_corner[1], up_front_right_corner[2], up_front_right_corner[0]]
    up_front_right_corner = [help[2], help[0], help[1]]

    moves.append("F")

    check_angle()
    
def Fi():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLACK, 0)
        hold_rotate_clockwise()

    help = up_front_edge
    up_front_edge = [middle_front_right_edge[1], middle_front_right_edge[0]]
    middle_front_right_edge = [down_front_edge[1], down_front_edge[0]]
    down_front_edge = [middle_front_left_edge[1], middle_front_left_edge[0]]
    middle_front_left_edge = [help[1], help[0]]

    help = up_front_left_corner
    up_front_left_corner = [up_front_right_corner[1], up_front_right_corner[2], up_front_right_corner[0]]
    up_front_right_corner = [down_front_right_corner[2], down_front_right_corner[0], down_front_right_corner[1]]
    down_front_right_corner = [down_front_left_corner[1], down_front_left_corner[2], down_front_left_corner[0]]
    down_front_left_corner = [help[2], help[0], help[1]]

    moves.append("F'")

    check_angle()
    
def F2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.BLACK, 0)
        hold_rotate2()

    help = up_front_edge
    up_front_edge = down_front_edge
    down_front_edge = help

    help = middle_front_left_edge
    middle_front_left_edge = middle_front_right_edge
    middle_front_right_edge = help

    help = down_front_left_corner
    down_front_left_corner = up_front_right_corner
    up_front_right_corner = help

    help = down_front_right_corner
    down_front_right_corner = up_front_left_corner
    up_front_left_corner = help

    moves.append("F2")

    check_angle()
    
def L():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.GREEN, 0)
        hold_rotate_counterclockwise()

    help = up_left_edge
    up_left_edge = middle_back_left_edge
    middle_back_left_edge = down_left_edge
    down_left_edge = middle_front_left_edge
    middle_front_left_edge = help

    help = up_front_left_corner
    up_front_left_corner = [up_back_left_corner[2], up_back_left_corner[0], up_back_left_corner[1]]
    up_back_left_corner = [down_back_left_corner[1], down_back_left_corner[2], down_back_left_corner[0]]
    down_back_left_corner = [down_front_left_corner[2], down_front_left_corner[0], down_front_left_corner[1]]
    down_front_left_corner = [help[1], help[2], help[0]]

    moves.append("L")

    check_angle()
    
def Li():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.GREEN, 0)
        hold_rotate_clockwise()

    help = up_left_edge
    up_left_edge = middle_front_left_edge
    middle_front_left_edge = down_left_edge
    down_left_edge = middle_back_left_edge
    middle_back_left_edge = help

    help = up_front_left_corner
    up_front_left_corner = [down_front_left_corner[2], down_front_left_corner[0], down_front_left_corner[1]]
    down_front_left_corner = [down_back_left_corner[1], down_back_left_corner[2], down_back_left_corner[0]]
    down_back_left_corner = [up_back_left_corner[2], up_back_left_corner[0], up_back_left_corner[1]]
    up_back_left_corner = [help[1], help[2], help[0]]

    moves.append("L'")

    check_angle()
    
def L2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.GREEN, 0)
        hold_rotate2()

    help = middle_back_left_edge
    middle_back_left_edge = middle_front_left_edge
    middle_front_left_edge = help

    help = down_left_edge
    down_left_edge = up_left_edge
    up_left_edge = help

    help = down_back_left_corner
    down_back_left_corner = up_front_left_corner
    up_front_left_corner = help

    help = down_front_left_corner
    down_front_left_corner = up_back_left_corner
    up_back_left_corner = help

    moves.append("L2")

    check_angle()
    
def D():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.YELLOW, 0)
        hold_rotate_counterclockwise()
    
    help = down_front_edge
    down_front_edge = down_left_edge
    down_left_edge = down_back_edge
    down_back_edge = down_right_edge
    down_right_edge = help

    help = down_front_right_corner
    down_front_right_corner = down_front_left_corner
    down_front_left_corner = down_back_left_corner
    down_back_left_corner = down_back_right_corner
    down_back_right_corner = help

    moves.append("D")

    check_angle()
    
def Di():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.YELLOW, 0)
        hold_rotate_clockwise()

    help = down_front_edge
    down_front_edge = down_right_edge
    down_right_edge = down_back_edge
    down_back_edge = down_left_edge
    down_left_edge = help

    help = down_front_right_corner
    down_front_right_corner = down_back_right_corner
    down_back_right_corner = down_back_left_corner
    down_back_left_corner = down_front_left_corner
    down_front_left_corner = help

    moves.append("D'")

    check_angle()
    
def D2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.YELLOW, 0)
        hold_rotate2()

    help = down_front_edge
    down_front_edge = down_back_edge
    down_back_edge = help

    help = down_left_edge
    down_left_edge = down_right_edge
    down_right_edge = help

    help = down_front_left_corner
    down_front_left_corner = down_back_right_corner
    down_back_right_corner = help

    help = down_front_right_corner
    down_front_right_corner = down_back_left_corner
    down_back_left_corner = help

    moves.append("D2")

    check_angle()
    
def B():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.RED, 0)
        hold_rotate_counterclockwise()

    help = up_back_edge
    up_back_edge = [middle_back_right_edge[1], middle_back_right_edge[0]]
    middle_back_right_edge = [down_back_edge[1], down_back_edge[0]]
    down_back_edge = [middle_back_left_edge[1], middle_back_left_edge[0]]
    middle_back_left_edge = [help[1], help[0]]

    help = up_back_right_corner
    up_back_right_corner = [down_back_right_corner[1], down_back_right_corner[2], down_back_right_corner[0]]
    down_back_right_corner = [down_back_left_corner[2], down_back_left_corner[0], down_back_left_corner[1]]
    down_back_left_corner = [up_back_left_corner[1], up_back_left_corner[2], up_back_left_corner[0]]
    up_back_left_corner = [help[2], help[0], help[1]]

    moves.append("B")

    check_angle()
    
def Bi():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.RED, 0)
        hold_rotate_clockwise()

    help = up_back_edge
    up_back_edge = [middle_back_left_edge[1], middle_back_left_edge[0]]
    middle_back_left_edge = [down_back_edge[1], down_back_edge[0]]
    down_back_edge = [middle_back_right_edge[1], middle_back_right_edge[0]]
    middle_back_right_edge = [help[1], help[0]]

    help = up_back_right_corner
    up_back_right_corner = [up_back_left_corner[1], up_back_left_corner[2], up_back_left_corner[0]]
    up_back_left_corner = [down_back_left_corner[2], down_back_left_corner[0], down_back_left_corner[1]]
    down_back_left_corner = [down_back_right_corner[1], down_back_right_corner[2], down_back_right_corner[0]]
    down_back_right_corner = [help[2], help[0], help[1]]

    moves.append("B'")

    check_angle()
    
def B2():
    global up_center, front_center, down_center, back_center, left_center, right_center, up_front_left_corner, up_front_right_corner, up_back_right_corner, up_back_left_corner, down_front_left_corner, down_front_right_corner, down_back_right_corner, down_back_left_corner, up_front_edge, up_right_edge, up_left_edge, up_back_edge, middle_front_left_edge, middle_front_right_edge, middle_back_right_edge, middle_back_left_edge, down_front_edge, down_right_edge, down_left_edge, down_back_edge
    if move:
        turn_right_direction(Color.RED, 0)
        hold_rotate2()

    help = down_back_edge
    down_back_edge = up_back_edge
    up_back_edge = help

    help = middle_back_left_edge
    middle_back_left_edge = middle_back_right_edge
    middle_back_right_edge = help

    help = down_back_left_corner
    down_back_left_corner = up_back_right_corner
    up_back_right_corner = help

    help = down_back_right_corner
    down_back_right_corner = up_back_left_corner
    up_back_left_corner = help

    moves.append("B2")

    check_angle()
#endregion


# Hauptprogramm
# Der Roboter fängt an zu kalibrieren, denn Zauberwürfel auf die richtige Seite zu drehen, 
# den Zauberwürfel zu scannen und ihn anschließend zu lösen.

calibrate()

turn_correctly()

scan_cube()

CFOP()

printAlgorithm()