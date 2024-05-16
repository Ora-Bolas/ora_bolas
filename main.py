from funcoes import *
from game import animar
from grafico import animacao_grafico
import tkinter as tk

def menu_opcoes():
    def executar_opcao():
        opcao = int(opcao_var.get().split('.')[0]) 
        if opcao == 1:
            trajetoria(float(x_entry.get()), float(y_entry.get()))
        elif opcao == 2:
            posicao_robo_bola_x()
        elif opcao == 3:
            posicao_robo_bola_y()
        elif opcao == 4:
            velocidade_robo_bola_x(float(x_entry.get()), float(y_entry.get()))
        elif opcao == 5:
            grafico_velocidade_y()
        elif opcao == 6:
            aceleracao_robo_x()
        elif opcao == 7:
            aceleracao_robo_y()
        elif opcao == 8:
            distancia_robo_bola()
        elif opcao == 9:
            animacao_grafico()
        elif opcao == 10:
            animar()
        elif opcao == 11:
            janela.quit()
        else:
            output_label.config(text="Opção inválida, tente novamente!")

    janela = tk.Tk()
    janela.title("Ora Bolas")
    janela.geometry("600x300")
    janela.config(bg='#f0f0f0')  # Cor de fundo

    titulo_label = tk.Label(janela, text="Ora Bolas", bg='#f0f0f0', fg='#333', font=("Arial", 24, "bold"))
    titulo_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    x_label = tk.Label(janela, text="Posição X do Robô:", bg='#f0f0f0', fg='#333', font=("Arial", 12))
    x_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    x_entry = tk.Entry(janela)
    x_entry.grid(row=1, column=1, padx=10, pady=5)

    y_label = tk.Label(janela, text="Posição Y do Robô:", bg='#f0f0f0', fg='#333', font=("Arial", 12))
    y_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
    y_entry = tk.Entry(janela)
    y_entry.grid(row=2, column=1, padx=10, pady=5)

    opcao_label = tk.Label(janela, text="Escolha uma Opção:", bg='#f0f0f0', fg='#333', font=("Arial", 12))
    opcao_label.grid(row=3, column=0, padx=10, pady=5, sticky='e')
    opcao_var = tk.StringVar(janela)
    opcao_var.set("Escolha sua opção")  # Valor padrão
    opcoes_menu = tk.OptionMenu(janela, opcao_var, "1. Gráfico das trajetórias.","2. Gráfico das coordenadas em x.", "3. Gráfico das coordenadas em y.", "4. Gráfico das velocidades em x.", "5. Gráfico das velocidades em y.", "6. Gráfico das acelerações no eixo X.", "7. Gráfico das acelerações no eixo Y.", "8. Gráfico da distância relativa.", "9. Animação do gráfico das trajetórias.", "10. Animação usando pygame", "11. Sair")
    opcoes_menu.config(bg='#f0f0f0', fg='#333', width=35, font=("Arial", 12))
    opcoes_menu.grid(row=3, column=1, padx=10, pady=5)

    executar_botao = tk.Button(janela, text="Gerar gráfico", command=executar_opcao, bg='#007bff', fg='white', font=("Arial", 14, "bold"))
    executar_botao.grid(row=4, column=0, columnspan=2, pady=20)

    output_label = tk.Label(janela, text="", bg='#f0f0f0', fg='red', font=("Arial", 12))
    output_label.grid(row=5, column=0, columnspan=2)

    janela.mainloop()

menu_opcoes()

