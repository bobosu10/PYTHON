import cv2
import numpy as np
import tkinter as tk
from customtkinter import CTk, CTkButton, CTkLabel
import random

def sorteio_reyna():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,22,23,24,25,27,28,29,30,31,33,36,38,43,45,48,49,53,54,57,58,59,66,67,70,72,74,75,77,78,84,87,88,98,99,100]
    pessoan1 = random.choice(lista)
    pessoan2 = random.choice(lista)
    pessoan3 = random.choice(lista)
    texto = "Pessoa sorteada número {}, {} e {}".format(pessoan1, pessoan2, pessoan3)
    texto_num.configure(text=texto)

# Janela
janela = CTk()
janela.title("SORTEIO DA RIFA DA REYNA")
janela.geometry("1920x1080")

# Imagem
caminho_imagem = "/home/lucas/Downloads/WhatsApp Image 2024-04-07 at 20.32.23.jpeg"
imagem_cv2 = cv2.imread(caminho_imagem)

# Converter a imagem para RGB
imagem_rgb = cv2.cvtColor(imagem_cv2, cv2.COLOR_BGR2RGB)

# Converter a imagem para um formato aceito pelo Tkinter
h, w, _ = imagem_rgb.shape
imagem_tk = tk.PhotoImage(master=janela, width=w, height=h)
imagem_tk.blank()
imagem_tk.photo = imagem_rgb
for i in range(h):
    for j in range(w):
        imagem_tk.put("#%02x%02x%02x" % tuple(imagem_rgb[i, j]), (j, i))

# Exibir a imagem em um rótulo
label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Texto
texto_orientacao = CTkLabel(master=janela,
                             text="Clique no botão para ver o resultado do sorteio!",
                             width=150,
                             height=100,
                             corner_radius=0)
texto_orientacao.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Botão
button = CTkButton(master=janela,
                    text="Sorteio",
                    command=sorteio_reyna,
                    width=120,
                    height=50,
                    border_width=0,
                    corner_radius=8)
button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Texto 2
texto_num = CTkLabel(master=janela,
                      text="Clique no botão",
                      width=120,
                      height=25,
                      corner_radius=0)
texto_num.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

janela.mainloop()
