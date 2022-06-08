from time import sleep as wait
from os import system
system("clear||cls&&title TABUADA")

def clear():
    system("clear||cls")

def pause():
    input("\nPressione algo para continuar...")

def calc(num, to):
    local_to = to + 1

    for i in range(0, local_to):
        print("{}x{} = {}".format(num, i, num * i))

def print_tabuada(tabuada):
    if tabuada > 0:
        print("===TABUADA DO {}===".format(tabuada))
    elif tabuada == 0 or None:
        print("===TABUADA===")

while True:
    clear()
    print_tabuada(0)
    input_one = input("\n\n[C].Calcular\n[S].Sair\n\nDigite: ").lower().strip()

    if input_one == "c":
        clear()
        try:
            n = int(input("Digite o numero da tabuada: ").strip())
            to = int(input("Ate: ").strip())
            clear()
            print_tabuada(n)
            print("\n")
            calc(n, to)
            print("\n")
            wait(2)
            pause()
        except:
            clear()
            print("DIGITE UM NUMERO!")
            wait(3)

    elif input_one == "s":
        quit()
    elif input_one not in ["c", "s"]:
        clear()
        print("DIGITE UMA LETRA VALIDA!")
        wait(3)