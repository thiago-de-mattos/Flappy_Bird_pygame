import pygame
from random import randrange
from constantes import (
    IMAGENS,
    VELOCIDADE_JOGO,
    VELOCIDADE_PULO,
    TEMPO_ANIMACAO_PASSARO,
    ROTACAO_MAX_PASSARO,
    VELOCIDADE_ROTACAO_PASSARO,
    DISTANCIA_CANOS,
)


class AtorJogo:
    def __init__(self, x, y, imagem):
        self.x = x
        self.y = y
        self.imagem = imagem

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))


class Passaro(AtorJogo):
    def __init__(self, x, y):
        super().__init__(x, y, IMAGENS["passaro"][0])
        self.velocidade_vertical = 0
        self.angulo = 0
        self.tempo = 0
        self.contagem_imagem = 0
        self.altura = self.y

    def pular(self):
        self.velocidade_vertical = VELOCIDADE_PULO
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = (
            1.5 * (self.tempo**2) + (self.velocidade_vertical * self.tempo)
        )

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < -8:
            deslocamento = -8

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < ROTACAO_MAX_PASSARO:
                self.angulo = ROTACAO_MAX_PASSARO
        else:
            if self.angulo > -90:
                self.angulo -= VELOCIDADE_ROTACAO_PASSARO

    def desenhar(self, tela):
        self.contagem_imagem += 1
        self.imagem = IMAGENS["passaro"][
            self.contagem_imagem // TEMPO_ANIMACAO_PASSARO % 3
        ]

        if self.angulo <= -80:
            self.imagem = IMAGENS["passaro"][1]

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo_rotacionado = imagem_rotacionada.get_rect(
            center=centro_imagem
        )
        tela.blit(imagem_rotacionada, retangulo_rotacionado.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano(AtorJogo):
    def __init__(self, x):
        self.x = x
        self.altura = randrange(50, 450)
        self.passou = False
        self.cano_topo_imagem = pygame.transform.flip(
            IMAGENS["cano"], False, True
        )
        self.cano_base_imagem = IMAGENS["cano"]
        self.pos_topo = self.altura - self.cano_topo_imagem.get_height()
        self.pos_base = self.altura + DISTANCIA_CANOS

    def mover(self):
        self.x -= VELOCIDADE_JOGO

    def desenhar(self, tela):
        tela.blit(self.cano_topo_imagem, (self.x, self.pos_topo))
        tela.blit(self.cano_base_imagem, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.cano_topo_imagem)
        base_mask = pygame.mask.from_surface(self.cano_base_imagem)

        offset_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        offset_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        colisao_topo = passaro_mask.overlap(topo_mask, offset_topo)
        colisao_base = passaro_mask.overlap(base_mask, offset_base)

        return colisao_topo or colisao_base


class Chao(AtorJogo):
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = IMAGENS["chao"].get_width()

    def mover(self):
        self.x1 -= VELOCIDADE_JOGO
        self.x2 -= VELOCIDADE_JOGO

        if self.x1 + IMAGENS["chao"].get_width() <= 0:
            self.x1 = self.x2 + IMAGENS["chao"].get_width()

        if self.x2 + IMAGENS["chao"].get_width() <= 0:
            self.x2 = self.x1 + IMAGENS["chao"].get_width()

    def desenhar(self, tela):
        tela.blit(IMAGENS["chao"], (self.x1, self.y))
        tela.blit(IMAGENS["chao"], (self.x2, self.y))