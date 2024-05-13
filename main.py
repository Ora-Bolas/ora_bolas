from funcoes import *

x_robo = float(input("Digite a posição em X do robô: "))
y_robo = float(input("Digite a posição em Y do robô: "))

while(True):

    print(""" 
1. Calcular pontos de interceptação e mostrar gráfico da trajetórias.
2. Gráfico das coordenadas x e y da posição da bola e do robô em função do tempo t.
3. Gráfico dos componentes vx e vy da velocidade da bola e do robô em função do tempo t  
4. Gráfico dos componentes ax e ay da aceleração da bola e do robô em função do tempo t
5. Gráfico da distância relativa d entre o robô e a bola como função do tempo t
6. Sair.
          """)

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        trajetoria(x_robo, y_robo)
    elif opcao == 2:
        print("")
        # posicao_robo_bola()
    elif opcao == 3:
        vel_robo(x_robo, y_robo)
    elif opcao == 4:
        acel_robo()
    elif opcao == 5:
        distancia_robo_bola()
    elif opcao == 6:
        break
    else:
        print("Opção inválida, tente novamente!")