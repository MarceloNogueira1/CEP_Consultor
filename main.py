from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from pygame import image
import consultor_cep_v2


fundo = '#242424'
branca = "#ffffff"
azul = '#0086ff'
azul_escuro = '#002336'


janela = Tk()
janela.geometry('500x280')
janela.configure(bg=fundo)


#Imagem Botão tela principal
img_botao = Image.open('D:\Python\Scripts\CEP\images\img_buscar.png')
img_botao = ImageTk.PhotoImage(img_botao)

#Imagem botão tela resultado
img_outrocep = Image.open('D:\Python\Scripts\CEP\images\img_outrocep.png')
img_outrocep = img_outrocep.resize((290, 38), Image.ANTIALIAS)
img_outrocep = ImageTk.PhotoImage(img_outrocep)

#Logo Tela principal
down = Image.open('D:\Python\Scripts\CEP\images\cep_consultor.png')
down = down.resize((210, 210), Image.ANTIALIAS)
down = ImageTk.PhotoImage(down)
l_logo = Label(janela, image=down, compound=LEFT, bg=fundo)
l_logo.place(x=140, y=-35)


def resultado_tela():
    global teste
    global cep_tela
    global rua_tela
    global complemento_tela
    global bairro_tela
    global estado_tela
    global ddd_tela
    global titulo_tela
    global b_outrocep

    tela_resultado = Toplevel()
    tela_resultado.geometry('300x280')
    tela_resultado.configure(bg=fundo)

    teste = Label(tela_resultado, text='RESULTADO', bg=fundo, fg=azul,
                  font=('Roboto 20 bold'), anchor='nw')
    teste.place(x=65, y=10)

    cep_tela = Label(tela_resultado, text='', bg=fundo, fg=azul,
                     font=('Roboto 12 bold'), anchor='nw')
    cep_tela.place(x=20, y=70)

    rua_tela = Label(tela_resultado, text='', bg=fundo, fg=azul,
                     font=('Roboto 12 bold'), anchor='nw')
    rua_tela.place(x=20, y=100)

    complemento_tela = Label(tela_resultado, text='', bg=fundo,
                             fg=azul, font=('Roboto 12 bold'), anchor='nw')
    complemento_tela.place(x=20, y=220)

    bairro_tela = Label(tela_resultado, text='', bg=fundo, fg=azul,
                        font=('Roboto 12 bold'), anchor='nw')
    bairro_tela.place(x=20, y=160)

    estado_tela = Label(tela_resultado, text='', bg=fundo, fg=azul,
                        font=('Roboto 12 bold'), anchor='nw')
    estado_tela.place(x=20, y=190)

    ddd_tela = Label(tela_resultado, text='', bg=fundo, fg=azul,
                     font=('Roboto 12 bold'), anchor='nw')
    ddd_tela.place(x=20, y=130)

    b_outrocep = Button(tela_resultado, image=img_outrocep, relief='flat', bg=fundo,
                        command=tela_resultado.destroy)
    b_outrocep.place(x=2, y=230)


def campo_pesquisa():
    global cep_get
    global e_url
    e_url = Entry(janela, width=33, font='Calibri 14 bold', justify=CENTER)
    e_url.place(x=80, y=170)
    cep_get = e_url.get()

    b_pesquisa = Button(janela, image=img_botao, relief='flat', bg=fundo, command=lambda: [
                        resultado_tela(), resul()])
    b_pesquisa.place(x=150, y=210)


def resul():
    while True:
        cep = e_url.get()
        consultor_cep_v2.consulta(cep)
        consultor_cep_v2.resultado()

        teste['text'] = consultor_cep_v2.titulo_resultado
        cep_tela['text'] = 'CEP: '+consultor_cep_v2.cep_resultado
        rua_tela['text'] = 'RUA: '+consultor_cep_v2.rua_resultado
        bairro_tela['text'] = 'BAIRRO: '+consultor_cep_v2.bairro_resultado
        estado_tela['text'] = 'ESTADO: '+consultor_cep_v2.estado_resultado
        ddd_tela['text'] = 'DDD: '+consultor_cep_v2.ddd_resultado
        complemento_tela['text'] = '' + consultor_cep_v2.complemento_resultado
        break


# resultado_tela()
campo_pesquisa()

janela.mainloop()
