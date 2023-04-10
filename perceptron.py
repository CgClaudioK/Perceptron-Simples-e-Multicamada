
bias = 0.0
pesos = []
valores = []
def menu():
    while True:
        opcao = input("""
Selecione a Função desejada
da tabela verdade
===================
[OR] -> Tabela OR
[XOR] -> Tabela XOR
[AND] -> Tabela AND
[Q] -> Quit

===================
==> """).upper()

        if opcao == "OR": 
            valores = [[0.0, 0.0, 0.0], # Matriz de treinamento para OR
               [0.0, 1.0, 1.0],
               [1.0, 0.0, 1.0],
               [1.0, 1.0, 1.0]]
            return opcao
        
        elif opcao == "XOR": 
            valores = [[0.0, 0.0, 0.0], # Matriz de treinamento para XOR
               [0.0, 1.0, 1.0],
               [1.0, 0.0, 1.0],
               [1.0, 1.0, 0.0]]
            return opcao
            
        elif opcao == "AND": 
            valores = [[0.0, 0.0, 0.0], # Matriz de treinamento para AND
               [0.0, 1.0, 0.0],
               [1.0, 0.0, 0.0],
               [1.0, 1.0, 1.0]]
            return opcao

        elif opcao == "Q":
            exit()
            
        else:
            print("Opção inválida. Tente novamente.")

          

# Solicita ao usuário os valores dos pesos
for i in range(2):
    peso = float(input(f"Informe o valor do peso {i+1}: "))
    pesos.append(peso)

print(f"Bias: {bias}")
print(f"Pesos: {pesos}")


def treinamento():
     global pesos  
     global bias 
     global valores
     somaerro = 1
     erro = 0.0
     iteracao = 1
     maxiteracao= 1
     saida = 0.0
     tx_aprendizado = 1.00
     

     while iteracao < maxiteracao and somaerro > 0:
         somaerro = 0
         for i in range (len(valores)):
            saida = pesos[0] * valores[i][0] + pesos[1] * valores[i][1]+ bias
            if saida >= 0:
                 saida = 1
            else:
                 saida = 0
            erro = valores[i][2] - saida
            pesos[0] = pesos[0] + tx_aprendizado * erro * valores[i][0]
            pesos[1] = pesos[1] + tx_aprendizado * erro * valores[i][1]
            bias = bias + tx_aprendizado * erro
            if erro != 0:
                    somaerro = somaerro + 1
         iteracao += 1
            
     if somaerro == 0:
            print("Treinamento OK.")
     else:
            print("FALHA NO TREINAMENTO...")

# Função de utilização da rede
def testar():
    while True:
        valor1 = int(input("Entre o primeiro valor (0 ou 1): "))
        valor2 = int(input("Entre o segundo valor (0 ou 1): "))
        saida = pesos[0] * valor1 + pesos[1] * valor2 + bias
        if saida >= 0:
            saida = 1
        else:
            saida = 0
        print("Entradas: {} {} | Saída: {}".format(valor1, valor2, saida))

        if input("Deseja testar novamente? (s/n)") == 'n':
            break

menu()            #Chamadas das Funções
treinamento()
testar()