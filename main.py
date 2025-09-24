import pygame
from jogo import GerenciadorJogo


if __name__ == "__main__":
    pygame.init()
    jogo = GerenciadorJogo()
    jogo.executar()