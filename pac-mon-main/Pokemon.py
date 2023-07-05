from tupy import *
from Pacball import *
from Mapa import *
import time
import random
from typing import Union

class Pokemon(Image):
    """Classe que representa um Pokémon no jogo.

    Args:
        file (str): O nome do arquivo de imagem do Pokémon.
        inicio_x (int): A posição inicial do Pokémon no eixo X.
        inicio_y (int): A posição inicial do Pokémon no eixo Y.
        pokeball (Pacball): A instância da classe Pacball usada para capturar o Pokémon.
        pontos (int, optional): A quantidade de pontos do jogador. Padrão é 0.

    Attributes:
        file (str): O nome do arquivo de imagem do Pokémon.
        x (int): A posição atual do Pokémon no eixo X.
        y (int): A posição atual do Pokémon no eixo Y.
        vida (bool): Indica se o Pokémon está vivo.
        pokeball (Pacball): A instância da classe Pacball usada para capturar o Pokémon.
        pontos (int): A quantidade de pontos do jogador.
        tempo_inicial (float): O tempo de início do jogo.

    """

    def __init__(self, file: str, inicio_x: int, inicio_y: int, pokeball, pontos: int = 0) -> None:
        """Inicializa uma instância da classe Pokémon.

        Args:
            file (str): O nome do arquivo de imagem do Pokémon.
            inicio_x (int): A posição inicial do Pokémon no eixo X.
            inicio_y (int): A posição inicial do Pokémon no eixo Y.
            pokeball (Pacball): A instância da classe Pacball usada para capturar o Pokémon.
            pontos (int, optional): A quantidade de pontos do jogador. Padrão é 0.

        """
        super().__init__()
        self.file = file
        self.x = inicio_x
        self.y = inicio_y
        self.vida = True
        self.pokeball = pokeball
        self.pontos = pontos
        self._hide()
        self.tempo_inicial = time.time()

    def mover(self, aceleracao: int = 1) -> None:
        """Move o Pokémon aleatoriamente.

        Args:
            aceleracao (int, optional): O fator de aceleração do movimento. Padrão é 1.

        """
        direcoes = ['cima', 'baixo', 'esq', 'dir']
        direcao = random.choice(direcoes)

        if direcao == 'cima':
            self.y -= 20 * aceleracao
        elif direcao == 'baixo':
            self.y += 20 * aceleracao
        elif direcao == 'esq':
            self.x -= 20 * aceleracao
        elif direcao == 'dir':
            self.x += 20 * aceleracao
    
    def update(self) -> None:
        """Atualiza a posição do Pokémon e verifica se foi capturado.

        Também exibe informações sobre os pontos do jogador e o tempo decorrido.
        Se o tempo decorrido for maior ou igual a 10 segundos, o jogo termina.

        """
        self.mover()
        self.capturado(self.pokeball)
        tempo_decorrido = time.time() - self.tempo_inicial
        tempo_formatado = format(tempo_decorrido, ".1f")
        
        toast(self.pontos)
        toast(tempo_formatado)
        
        if tempo_decorrido >= 10:
            toast("Tempo esgotado!")
            toast("Pressione a tecla Esc para sair!")
            self.derrota(self.pokeball)  
            if keyboard.is_key_down('Esc'):      
                exit() 

        # Delimita a tela
        if self.x < 60: 
             self.x += 20
        elif self.x > 850: 
             self.x  -= 20

        if self.y < 40: 
             self.y += 20
        elif self.y > 440: 
             self.y  -= 20
    
    def capturado(self, pokeball) -> None:
        """Verifica se o Pokémon foi capturado pela Pacball.

        Se o Pokémon for capturado, sua imagem é atualizada para a próxima forma,
        sua posição é redefinida e sua vida é definida como False.

        Args:
            pokeball (Pacball): A instância da classe Pacball usada para capturar o Pokémon.

        """
        if self._collides_with(pokeball):
            if self.file == "charmander.png":
                self.file = "charmeleon.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "charmeleon.png":
                self.file = "charizard.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "charizard.png":
                self._destroy()
                
            if self.file == "pichu.png":
                self.file = "pikachu.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "pikachu.png":
                self.file = "raichu-f.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "raichu-f.png":
                self._destroy()
                self.vida = False

            if self.file == "bulbasaur.png":
                self.file = "ivysaur.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "ivysaur.png":
                self.file = "venusaur-f.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "venusaur-f.png":
                self._destroy()
                self.vida = False

            if self.file == "squirtle.png":
                self.file = "wartortle.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "wartortle.png":
                self.file = "blastoise.png"
                self.x = random.randint(100, 800)
                self.y = random.randint(100, 400)
                self.vida = False
            elif self.file == "blastoise.png":
                self.pontos += 1
                self._destroy()
                self.vida = False

    def derrota(self, pokeball) -> None:
        """Executa a ação de derrota do Pokémon.


        Args:
            pokeball (Pacball): A instância da classe Pacball.

        """
        self.x -= 20
        self.y += 20
        pokeball.x -= 20
        pokeball.y += 20
