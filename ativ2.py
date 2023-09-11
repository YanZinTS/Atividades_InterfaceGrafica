from ModulosAtiv import *
import customtkinter as Tk


def clique():
    a = int(caixa1.get())
    nascimento = 2023 - a
    if nascimento >= 18:
        texto3.configure(text='Você é maior de idade')
    else:
        texto3.configure(text='Você é menor de idade')


Tk.set_appearance_mode('Dark')
Tk.set_default_color_theme('themes/metal.json')

janela = CriarJanela('Janela Principal', '900x400', 1, Redimensionar=False)

#criando um label
texto1 = Tk.CTkLabel(janela, text='Digite seu ano de nascimento:',text_color='white', font=('Arial', 15), justify='center')
texto1.grid(row=5, column=5)

texto3 = Tk.CTkLabel(janela, text='vai aparecer aqui sua resposta',text_color='white', font=('Arial', 16), justify='center')
texto3.grid(row=8, column=6)

#criando um botão
btn1 = Tk.CTkButton(janela, text='Comparar Idade', command=clique,
                    width=50, height=50, fg_color='black', hover_color='blue')
btn1.grid(row=7, column=6)

#criando a caixa de texto
caixa1 = Tk.CTkEntry(janela, placeholder_text='Digite algo...', text_color='black', width=180, height=30,
                        font=('Arial', 15), fg_color='white', placeholder_text_color='gray')
caixa1.grid(row=5, column=6)

janela.mainloop()