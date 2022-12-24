from tkinter import *
from emoji import *
import pygame

hand = '''
┏┓
┃┃
┃┃
            ┏┫┣┳┓
            ┣┻┫┃┃
            ┃┏┻┻┫'''


def clap():
    c = ':clapping_hands:'
    text_2['text'] = emojize(f'{30 * c}\n{30 * c}\n{30 * c}\n{30 * c}\n{30 * c}\n{30 * c}\n{30 * c}')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('clap_sound.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=0, start=0.0)


def clear():
    text_2['text'] = '''
┏┓
┃┃
┃┃
            ┏┫┣┳┓
            ┣┻┫┃┃
            ┃┏┻┻┫'''
    if pygame.init():
        pygame.mixer.music.stop()


janela = Tk()
janela.title('Clap Program! by Alejandro Alosilla')
janela.geometry('390x260')

text_1 = Label(janela, text='Press the button to clap:')
text_1.grid(column=0, row=0, padx=130, pady=10)

button_clap = Button(janela, text='Clap!', command=clap)
button_clap.grid(column=0, row=1, padx=10, pady=10)

button_clear = Button(janela, text='Clear!', command=clear)
button_clear.grid(column=0, row=2, padx=10, pady=10)

text_2 = Label(janela, text=hand)
text_2.grid(column=0, row=3, padx=10, pady=0)

janela.mainloop()
