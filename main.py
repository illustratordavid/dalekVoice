import random

import flask
import pygame.mixer
from flask import Flask, json
import glob
import os
from pygame import mixer

def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))

pygame.mixer.init()
pygame.mixer.music.set_volume(1)

path = "sounds"
sounds = listdir_nohidden(path)
print(sounds)
currentTrack = None

app = Flask(__name__)


def playARandomSound():
    global sounds
    sounds = sounds[1:] + [sounds[0]]  # move current song to the back of the list
    pygame.mixer.music.load(sounds[0])
    print('play' + sounds[0])
    pygame.mixer.music.play()

    status_code = flask.Response(status=201)
    return status_code


@app.route("/dalek")
def dalek():
    return playARandomSound()


@app.route("/start")
def start():
    pygame.mixer.music.load("new-humans-look-at-them-look.mp3")
    pygame.mixer.music.play()
    status_code = flask.Response(status=201)
    return status_code
