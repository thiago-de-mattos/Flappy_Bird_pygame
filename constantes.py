import pygame
import os


TELA_LARGURA = 500
TELA_ALTURA = 800

VELOCIDADE_JOGO = 5
VELOCIDADE_PULO = -10.5
TEMPO_ANIMACAO_PASSARO = 5
ROTACAO_MAX_PASSARO = 25
VELOCIDADE_ROTACAO_PASSARO = 20
DISTANCIA_CANOS = 200

IMAGENS = {
    "cano": pygame.transform.scale2x(
        pygame.image.load(os.path.join("imgs", "pipe.png"))
    ),
    "chao": pygame.transform.scale2x(
        pygame.image.load(os.path.join("imgs", "base.png"))
    ),
    "background": pygame.transform.scale2x(
        pygame.image.load(os.path.join("imgs", "bg.png"))
    ),
    "passaro": [
        pygame.transform.scale2x(
            pygame.image.load(os.path.join("imgs", f"bird{i}.png"))
        )
        for i in range(1, 4)
    ],
}

SONS = {
    "game_over": os.path.join("sounds", "gameover.ogg"),
    "overflow": os.path.join("sounds", "overflow.ogg"),
}