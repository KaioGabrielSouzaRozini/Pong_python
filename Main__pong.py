import pygame

from pygame import mixer

pygame.init()

tela = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("arial", 50, True, False)

#cores

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VELOCIDADE = 1


#Sons do Background
mixer.music.load("trilha.mp3")
mixer.music.play(-1)

pontuou = mixer.Sound("ponto.mp3")
raquetada = mixer.Sound("raquetada.mp3")


class Raquetes:

    def __init__(self, bola):
        self.bolinha = bola
        self.posicao_x_raquete = 10
        self.posicao_y_raquete = 250
        self.posicao_x_raquete_2 = 778
        self.posicao_y_raquete_2 = 250
        self.vel_y = 0.3
        self.comprimento = 12
        self.altura = 100
        self.pontos = 0
        self.pontos_adversario = 0

    def desenha_raquetes(self, tela):

        pygame.draw.rect(tela, BRANCO, [self.posicao_x_raquete, self.posicao_y_raquete, self.comprimento, self.altura])
        pygame.draw.rect(tela, BRANCO, [self.posicao_x_raquete_2, self.posicao_y_raquete_2, self.comprimento, self.altura])

    def controla_raquete(self):

        pressiona = pygame.key.get_pressed()

        if pressiona[pygame.K_w]:
            self.posicao_y_raquete -= self.vel_y
        if pressiona[pygame.K_s]:
            self.posicao_y_raquete += self.vel_y

        if pressiona[pygame.K_UP]:
            self.posicao_y_raquete_2 -= self.vel_y
        if pressiona[pygame.K_DOWN]:
            self.posicao_y_raquete_2 += self.vel_y

    def colide_raquete_bolinha(self):

        if self.bolinha.posicao_x - self.bolinha.raio < self.posicao_x_raquete + self.comprimento and self.bolinha.posicao_y - self.bolinha.raio < self.posicao_y_raquete + self.altura and self.bolinha.posicao_y + self.bolinha.raio > self.posicao_y_raquete:
            self.bolinha.velocidade_x *= -VELOCIDADE
            raquetada.play()

        if self.bolinha.posicao_x > self.posicao_x_raquete_2 - self.comprimento and self.bolinha.posicao_y - self.bolinha.raio < self.posicao_y_raquete_2 + self.altura and self.bolinha.posicao_y + self.bolinha.raio > self.posicao_y_raquete_2:
            self.bolinha.velocidade_x *= -VELOCIDADE
            raquetada.play()

    def pintar_pontos(self, tela):
        img_pontos = fonte.render("{}".format(self.pontos), True, BRANCO)
        tela.blit(img_pontos, (200, 30))
        img_pontos_2 = fonte.render("{}".format(self.pontos_adversario), True, BRANCO)
        tela.blit(img_pontos_2, (600, 30))

    def adiciona_pontos(self):

        if self.bolinha.posicao_x < 20:
            self.pontos += 1
            pontuou.play()
        if self.bolinha.posicao_x > 780:
            self.pontos_adversario += 1
            pontuou.play()

class Bolinha:

    def __init__(self):
        self.posicao_x = 400
        self.posicao_y = 300
        self.velocidade_x = 0.3
        self.velocidade_y = 0.3
        self.raio = 20

    def desenha_bolinha(self, tela):

        pygame.draw.circle(tela, BRANCO, (self.posicao_x, self.posicao_y), self.raio, 0)

    def move_bolinha(self):

        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

        if self.posicao_x + self.raio > 800:
            self.velocidade_x *= -VELOCIDADE

        if self.posicao_x - self.raio < 0:
            self.velocidade_x *= -VELOCIDADE

        if self.posicao_y + self.raio > 600:
            self.velocidade_y *= -VELOCIDADE

        if self.posicao_y - self.raio < 0:
            self.velocidade_y *= -VELOCIDADE



if __name__ == "__main__":
    bolinha = Bolinha()
    raquetes = Raquetes(bolinha)

    while True:

        #Bolinha
        tela.fill(PRETO)
        bolinha.desenha_bolinha(tela)
        bolinha.move_bolinha()
        raquetes.colide_raquete_bolinha()

        #Raquetes
        raquetes.pintar_pontos(tela)
        raquetes.adiciona_pontos()
        raquetes.desenha_raquetes(tela)
        raquetes.controla_raquete()

        pygame.display.update()
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()



