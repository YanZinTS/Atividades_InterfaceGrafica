from ModulosAtiv import *
import customtkinter as Tk


def clique():
    a = int(caixa1.get())
    b = int(caixa2.get())
    prestacao = a / b

    if prestacao > 500:
        texto3.configure(text='O usuário não consegue pagar')
    else:
        texto3.configure(text=f'Você consegue pagar com o valor de: R${prestacao}')


Tk.set_appearance_mode('Dark')
Tk.set_default_color_theme('themes/metal.json')

janela = CriarJanela('Janela Principal', '900x400', 1, Redimensionar=False)

#criando um label
texto1 = Tk.CTkLabel(janela, text='Digite o valor do produto:',text_color='white', font=('Arial', 15), justify='center')
texto1.grid(row=5, column=5)

texto2 = Tk.CTkLabel(janela, text='Digite a quantidade de prestações:',text_color='white', font=('Arial', 15), justify='center')
texto2.grid(row=6, column=5)

texto3 = Tk.CTkLabel(janela, text='vai aparecer aqui sua parcela',text_color='white', font=('Arial', 16), justify='center')
texto3.grid(row=8, column=6)

#criando um botão
btn1 = Tk.CTkButton(janela, text='Calcular', command=clique,
                    width=50, height=50, fg_color='black', hover_color='blue')
btn1.grid(row=7, column=6)

#criando a caixa de texto
caixa1 = Tk.CTkEntry(janela, placeholder_text='Digite algo...', text_color='black', width=180, height=30,
                        font=('Arial', 15), fg_color='white', placeholder_text_color='gray')
caixa1.grid(row=5, column=6)

caixa2 = Tk.CTkEntry(janela, placeholder_text='Digite algo...', text_color='black', width=180, height=30,
                        font=('Arial', 15), fg_color='white', placeholder_text_color='gray')
caixa2.grid(row=6, column=6)

janela.mainloop()