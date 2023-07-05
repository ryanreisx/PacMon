from tupy import *
from Pokemon import *
from Mapa import *
from Barreira import *
from typing import List


class Pacball(Image):
    def __init__(self, barreiras: List[Barreira]) -> None:
        super().__init__()
        self.file: str = "Pokeball_Dir.png"
        self.x: int = 40
        self.y: int = 115
        self.vida: bool = True
        self.barreiras: List[Barreira] = barreiras
        self._hide()

    def update(self) -> None:
        """Atualiza a posição da Pacball de acordo com as teclas pressionadas.

        Verifica se as teclas de direção (esquerda, direita, cima, baixo) foram pressionadas
        e move a Pacball para a posição correspondente. Também verifica colisões com as paredes
        e mantém a Pacball dentro dos limites da tela.

        """
        if keyboard.is_key_down('Left'):
            self.x -= 20
            self.file = "Pokeball_Esq.png"
            self.colisao_parede()
            self.bordas()
           
        if keyboard.is_key_down('Right'):
            self.x += 20
            self.file = "Pokeball_Dir.png"
            self.colisao_parede()
            self.bordas()
     
            
        if keyboard.is_key_down('Up'):
            self.y -= 20
            self.file = "Pokeball_Cima.png"
            self.colisao_parede()
            self.bordas()

            
        if keyboard.is_key_down('Down'):
            self.y += 20   
            self.file = "Pokeball_Baixo.png"
            self.colisao_parede()
            self.bordas()
               
    def colisao_parede(self) -> None:
        """Verifica colisões da Pacball com as paredes.

        Verifica se a Pacball colide com alguma das barreiras presentes no jogo.
        Se houver colisão, a posição da Pacball é ajustada para evitar que ela atravesse
        as paredes.

        """
        for barreira in self.barreiras:
            if self._collides_with(barreira):
                if self.file == "Pokeball_Esq.png":
                    self.x = self.x + 20
                if self.file == "Pokeball_Dir.png":
                    self.x = self.x - 20
                if self.file == "Pokeball_Cima.png":
                    self.y = self.y + 20
                if self.file == "Pokeball_Baixo.png":
                    self.y -= 20
    

    
    def bordas(self) -> None:
        """Mantém a Pacball dentro dos limites da tela.

        Verifica se a posição da Pacball ultrapassou os limites da tela e ajusta sua posição
        para mantê-la dentro desses limites.

        """
        if self.x < 60: 
             self.x += 20
        elif self.x > 850: 
             self.x  -= 20

        if self.y < 40: 
             self.y += 20
        elif self.y > 440: 
             self.y  -= 20
