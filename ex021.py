# ex021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame as pg

pg.init() # Inicia o pygame
pg.mixer.music.load('ex021.mp3') # Carrega o ficheiro de áudio
pg.mixer.music.play('ex021.mp3') # Reproduz o ficheiro de áudio
pg.event.wait()