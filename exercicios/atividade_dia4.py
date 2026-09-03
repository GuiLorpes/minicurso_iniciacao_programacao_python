from dataclasses import dataclass
from enum import Enum, auto

class Classe(Enum):
    MAGO = auto()
    ARQUEIRO = auto()
    GUERREIRO = auto()
    TANQUE = auto()

@dataclass
class Jogador:
    classe: Classe
    nivel: int
    exp: int
    vida: int

def cria_jogador(classe: Classe) -> Jogador:
    if classe == Classe.ARQUEIRO:
        vida = 70
    elif classe == Classe.GUERREIRO:
        vida = 100
    elif classe == Classe.MAGO:
        vida = 80
    else: # classe == Classe.TANQUE
        vida = 120
    return Jogador(classe, 0, 0, vida)


def ganha_xp(xp_ganho: int, jg: Jogador) -> None:
    jg.exp += xp_ganho
    if jg.exp >= 50:
        jg.nivel += jg.exp // 50
        jg.exp = jg.exp % 50


def da_dano(dano: int, jg: Jogador) -> None:
    jg.vida -= dano
    if jg.vida <= 0:
        jg.vida = 0
        print("Você Morreu!!!")
 

def main() -> None:
    print("Bem vindo ao Ilha de Esgard")
    print("Crie seu jogador: ")
    print("Defina sua classe: \n1 -> Mago\n2 -> Guerreiro")
    print("3 -> Arqueiro\n4 -> Tanque")
    escolha: int = int(input())
    classe: Classe
    match escolha:
        case 1:
            classe = Classe.MAGO
        case 2:
            classe = Classe.GUERREIRO
        case 3:
            classe = Classe.ARQUEIRO
        case 4:
            classe = Classe.TANQUE
        case _:
            print("Valor inválido")
    jogador = cria_jogador(classe)

    print(jogador)
    ganha_xp(139, jogador)
    print(jogador.nivel, jogador.exp)
    da_dano(130, jogador)
    print(jogador.vida)

if __name__ == "__main__":
    main()