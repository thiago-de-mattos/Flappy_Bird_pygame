from random import randrange
import pygame
from constantes import TELA_LARGURA, TELA_ALTURA, IMAGENS, SONS
from atores import Passaro, Cano, Chao


class GerenciadorJogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
        pygame.display.set_caption("Flappy Bird")
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.fonte_pontos = pygame.font.SysFont("arial", 50)
        self.iniciar_novo_jogo()

    def iniciar_novo_jogo(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(SONS["overflow"])
        pygame.mixer.music.play(-1)

        self.passaro = Passaro(230, 350)
        self.chao = Chao(730)
        self.canos = [Cano(500)]
        self.pontos = 0

    def gerenciar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                self.passaro.pular()

    def atualizar_estado_jogo(self):
        self.passaro.mover()
        self.chao.mover()
        remover_canos = []
        adicionar_novo_cano = False

        for cano in self.canos:
            cano.mover()
            if cano.colidir(self.passaro):
                self.game_over()
                return
            if not cano.passou and self.passaro.x > cano.x:
                cano.passou = True
                self.pontos += 1
                adicionar_novo_cano = True
            if cano.x + cano.cano_topo_imagem.get_width() < 0:
                remover_canos.append(cano)

        for cano in remover_canos:
            self.canos.remove(cano)

        if adicionar_novo_cano:
            self.canos.append(Cano(TELA_LARGURA + randrange(20, 150)))

        if (
            self.passaro.y + self.passaro.imagem.get_height() >= self.chao.y
            or self.passaro.y < 0
        ):
            self.game_over()

    def desenhar_elementos(self):
        self.tela.blit(IMAGENS["background"], (0, 0))
        for cano in self.canos:
            cano.desenhar(self.tela)
        self.chao.desenhar(self.tela)
        self.passaro.desenhar(self.tela)
        texto_pontos = self.fonte_pontos.render(
            f"Pontuação: {self.pontos}", True, (255, 255, 255)
        )
        self.tela.blit(
            texto_pontos,
            (TELA_LARGURA - 10 - texto_pontos.get_width(), 10),
        )
        pygame.display.update()

    def game_over(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(SONS["game_over"])
        pygame.mixer.music.play()

        fonte_game_over = pygame.font.SysFont("arial", 60)
        texto_game_over = fonte_game_over.render(
            "Game Over",
            True,
            (255, 0, 0),
        )
        texto_reiniciar = self.fonte_pontos.render(
            "Reiniciar",
            True,
            (255, 255, 255),
        )
        btn_largura, btn_altura = 200, 60
        btn_x = (TELA_LARGURA - btn_largura) // 2
        btn_y = (TELA_ALTURA - btn_altura) // 2 + 50
        btn_rect = pygame.Rect(btn_x, btn_y, btn_largura, btn_altura)

        while True:
            self.desenhar_elementos()
            self.tela.blit(
                texto_game_over,
                ((TELA_LARGURA - texto_game_over.get_width()) // 2, 200),
            )
            pygame.draw.rect(self.tela, (0, 100, 200), btn_rect)
            self.tela.blit(
                texto_reiniciar,
                (
                    btn_x + (btn_largura - texto_reiniciar.get_width()) // 2,
                    btn_y + (btn_altura - texto_reiniciar.get_height()) // 2,
                ),
            )
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                    return
                if (
                    evento.type == pygame.MOUSEBUTTONDOWN
                    and btn_rect.collidepoint(evento.pos)
                ):
                    self.iniciar_novo_jogo()
                    return

    def executar(self):
        while self.rodando:
            self.relogio.tick(30)
            self.gerenciar_eventos()
            self.atualizar_estado_jogo()
            self.desenhar_elementos()

        pygame.quit()