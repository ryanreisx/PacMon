

from tupy import *
from Pacball import *
from Mapa import *
from Pokemon import *
from Barreira import *
import time


class Logo(BaseImage):
    def __init__(self):
        """
        Inicializa a classe Logo.

        Carrega a imagem 'pacman-logo-2.png' como imagem base e define as coordenadas (450, 250) para sua posição.
        """
        super().__init__('pacman-logo-2.png', 450, 250)



    def update(self):
        """
        Atualiza a imagem do logo.

        Se a tecla Enter for pressionada, troca a imagem base para 'campo.png' e exibe os fantasmas na tela.
        """
        if keyboard.is_key_just_down("Return"):
            self._file = 'campo.png'
            pokebola._show()
            fantasma1._show()
            fantasma2._show()
            fantasma3._show()
            fantasma4._show()
            barreira1._show()
            barreira2._show()
            barreira3._show()
            barreira4._show()
            barreira5._show()
            barreira6._show() 
            barreira7._show() 
            barreira8._show() 
            barreira9._show() 
            barreira10._show() 
            barreira11._show() 
            barreira12._show() 
            


if __name__ == '__main__':
    logo = Logo() 
    

    
    # Criação das barreiras
    barreira1 = Barreira(150, 80)
    barreira2 = Barreira(150, 280)
    barreira3 = Barreira(150, 480)
    barreira4 = Barreira(300, 150)
    barreira5 = Barreira(300, 350)
    barreira6 = Barreira(450, 150)
    barreira7 = Barreira(450, 350)
    barreira8 = Barreira(600, 80)
    barreira9 = Barreira(600, 280)
    barreira10 = Barreira(600, 480)
    barreira11 = Barreira(750, 150)
    barreira12 = Barreira(750, 350)

    barreiras = [barreira1, barreira2, barreira3, barreira4, barreira5, barreira6, barreira7, barreira8, barreira9, barreira10, barreira11, barreira12]
    pokebola = Pacball(barreiras)
    fantasma1 = Pokemon('bulbasaur.png', 410, 205, pokebola)
    fantasma2 = Pokemon('pichu.png', 470, 205, pokebola)
    fantasma3 = Pokemon('charmander.png', 410, 205, pokebola)
    fantasma4 = Pokemon('squirtle.png', 410, 205, pokebola)

run(globals())
