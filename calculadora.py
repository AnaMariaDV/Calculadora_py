# vamos fazer uma funcao para mostrar um menu
#o usuario vai digitar um numero para escolher que operacao vai fazer
def mostra_menu():
    print("escolha que operação você dejesa realizar:")
    print("1. adição")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
   
#Agora vou fazer uma funcao para cad operacao
def opcao_1(num1, num2):
    return num1+num2

def opcao_2(num1, num2):
    return num1-num2

def opcao_3(num1, num2):
    return num1*num2

def opcao_4(num1, num2):
    if num2!=0:
        return num1/num2
    else:
        return "erro!Divisão por zero"


def menu():
    while True:
        mostra_menu()
        escolha = input ("Escolha uma opção:")
        if escolha in["1","2","3","4"]:
#aqui vamos verificar se a condicao acima for verdadeira, se for, vamos digitar os numeros para fazer a operacao
#quase o mesmo metodo de verificacao de alocacao de memoria"NULL"
            try:
                num1=float(input("Digite o primeiro número:"))
                num2=float(input("Digite o segundo valor:"))
            except ValueError:
                print("Erro: Números inválidos!")
                continue


        if escolha== "1":
           resultado= opcao_1(num1, num2)
           print(f"O resultado da soma é:{resultado}")

        elif escolha == "2":
            resultado=opcao_2(num1, num2)
            print(f"O resultado da subtração é:{resultado}")

        elif escolha =="3":
            resultado=opcao_3(num1, num2)
            print(f"O resultado da multiplicação é:{resultado}")

        elif escolha == "4":
            resultado=opcao_4(num1, num2)
            print(f"O resultado da divisão é:{resultado}")

        else:
            print("Não existe essa opção")
            break



if __name__=="__main__":
    menu()





    



    

