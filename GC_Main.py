"""
author: BrendanMoore42
date: Jan 12, 2019

Standard moveset - Gamecube Controller for Dolphin

Can be ported to custom console and game-specific packs

Games Supported Currently:
Super Smash Bros. Melee
"""
# from smash_melee import AddOn
from directkeys import *

buttons = {'a': ['a'],
           'b': ['b'],
           'x': ['x'],
           'y': ['y'],
           'L': ['L'],
           'R': ['R'],
           'z': ['Z'],
           'up': ['up'],
           'down': ['down'],
           'left': ['left'],
           'right': ['up'],}

class Move():
    def __init__(self, move, direction, modifier=None, mod_move=None, mod_time=None, execute=True):
        self.move = move
        self.direction = direction
        self.modifier = modifier
        self.mod_move = mod_move
        self.mod_time = 1
        self.hold = 1
        self.tilt = 'left'
        self.smash = 'right'

        available_moves = {self.a_press: buttons["a"], self.b_press: buttons["b"],
                           self.down_press: ['crouch', 'down'],}

        if execute:
            self.execute_moves()

    def execute_moves(self):

        if self.move in ['wait', 'hold']:



        if self.move == ''
        print('sup')


    #Each function is a macro for a specific move
    def wait(self, wait):
        time.sleep(wait)


    def jump(self):
        PressKey(T)
        time.sleep(0.1)
        ReleaseKey(T)


    def up(self):
        PressKey(UP)
        time.sleep(0.25)
        ReleaseKey(UP)


    def left(self):
        PressKey(LEFT)
        time.sleep(0.1)#To alter timing of presses
        ReleaseKey(LEFT)


    def right(self):
        PressKey(RIGHT)
        time.sleep(0.1)
        ReleaseKey(RIGHT)


    def crouch(self):
        PressKey(DOWN)
        time.sleep(0.1)
        ReleaseKey(DOWN)


    def jab(self):
        PressKey(A)
        time.sleep(0.05)
        ReleaseKey(A)


    def djab(self):
        PressKey(A)
        ReleaseKey(A)
        time.sleep(0.05)
        PressKey(A)
        ReleaseKey(A)


    def shield(self):
        PressKey(R)
        time.sleep(2)
        ReleaseKey(R)


    def grab(self):
        PressKey(Z)
        time.sleep(0.05)
        ReleaseKey(Z)


    def Rsmash(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def Lsmash(self):
        PressKey(LEFT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(LEFT)
        ReleaseKey(A)

    def laser(self):
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(B)

    def shdl(self):
        PressKey(Y)
        PressKey(B)
        ReleaseKey(B)
        PressKey(B)
        ReleaseKey(B)


    def shine(self):
        PressKey(DOWN)
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(DOWN)
        ReleaseKey(B)


    def wd_left(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(LEFT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(LEFT)


    def wd_right(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(RIGHT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(RIGHT)

        def wombo_combo(self, *moves):
            print('sup')

        wombo_combo()

moves = "hey up smash then hold shield for 4 seconds"
move = "smash"
direction = "up" # if not defined will default to last direction called
modifier = "hold"
mod_move = "sheild"
mod_time = 4

player = Move(move=move, direction=direction, modifier=modifier, mod_move=mod_move, mod_time=mod_time) # for debugs