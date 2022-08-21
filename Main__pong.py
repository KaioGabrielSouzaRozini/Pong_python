import pygame

from pygame import mixer

from Botao import Botao

import sys

pygame.init()

#Tela e fonte
tela = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("arial", 50, True, False)

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VELOCIDADE = 1
VERMELHO = (200, 0, 60)
musica = False

#Sons
pontuou = mixer.Sound("ponto.mp3")
raquetada = mixer.Sound("raquetada.mp3")

#BackGround
BG = pygame.image.load("assets/Background.png")

#Define tamanho da fonte
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)



class Raquetes:

    def __init__(self, bola):
        self.bolinha = bola
        self.posicao_x_raquete = 10
        self.posicao_y_raquete = 250
        self.posicao_x_raquete_2 = 778
        self.posicao_y_raquete_2 = 250
        self.velocidade = 1
        self.vel_y = 0.22
        self.comprimento = 12
        self.altura = 100
        self.pontos = 0
        self.pontos_adversario = 0

    def desenha_raquetes(self, tela):

        pygame.draw.rect(tela, BRANCO, [self.posicao_x_raquete, self.posicao_y_raquete, self.comprimento, self.altura])
        pygame.draw.rect(tela, BRANCO, [self.posicao_x_raquete_2, self.posicao_y_raquete_2, self.comprimento, self.altura])

    def controla_raquete(self):

        pressiona = pygame.key.get_pressed()
        if self.posicao_y_raquete > 0:
            if pressiona[pygame.K_w]:
                self.posicao_y_raquete -= self.vel_y
        if self.posicao_y_raquete < 600 - self.altura:
            if pressiona[pygame.K_s]:
                self.posicao_y_raquete += self.vel_y

        if self.posicao_y_raquete_2 > 0:
            if pressiona[pygame.K_UP]:
                self.posicao_y_raquete_2 -= self.vel_y
        if self.posicao_y_raquete_2 < 600 - self.altura:
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

    def controla_velocidade(self):
        if self.vel_y < 0.44:
            self.vel_y += 0.11
        else:
            self.vel_y = 0.22

        if self.vel_y == 0.22:
            self.velocidade = 1
        elif self.vel_y == 0.33:
            self.velocidade = 2
        else:
            self.velocidade = 3


class Bolinha:

    def __init__(self):
        self.posicao_x = 400
        self.posicao_y = 300
        self.velocidade = 1
        self.velocidade_x = 0.22
        self.velocidade_y = 0.22
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

    def controla_velocidade(self):
        if self.velocidade_x < 0.44:
            self.velocidade_x += 0.11
            self.velocidade_y += 0.11
        else:
            self.velocidade_x = 0.22
            self.velocidade_y = 0.22
        if self.velocidade_x == 0.22:
            self.velocidade = 1
        elif self.velocidade_x == 0.33:
            self.velocidade = 2
        else:
            self.velocidade = 3


class Menu:

    def __init__(self, bola, raquetes):
        self.bolinha = bola
        self.raquetes = raquetes


    def menu_principal(self):


        while True:

            tela.blit(BG, (0, 0))

            menu_mouse_posicao = pygame.mouse.get_pos()

            botao_texto = get_font(100).render("Menu", True, BRANCO)
            botao_quadrado = botao_texto.get_rect(center=(400, 80))

            botao_jogar = Botao(imagem=None, posicao=(400, 200), texto="JOGAR", fonte=get_font(75),
                                cor_base=BRANCO, cor_transitoria=VERMELHO)

            botao_opcoes = Botao(imagem=None, posicao=(400, 325), texto="Opcões", fonte=get_font(75),
                                 cor_base=BRANCO, cor_transitoria=VERMELHO)

            botao_sair = Botao(imagem=None, posicao=(400, 450), texto="Sair", fonte=get_font(75),
                               cor_base=BRANCO, cor_transitoria=VERMELHO)

            tela.blit(botao_texto, botao_quadrado)

            for botao in [botao_jogar, botao_opcoes, botao_sair]:
                botao.muda_cor(menu_mouse_posicao)
                botao.update(tela)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogar.check_click(menu_mouse_posicao):
                        play()
                    if botao_opcoes.check_click(menu_mouse_posicao):
                        self.opcoes()
                    if botao_sair.check_click(menu_mouse_posicao):
                        exit()
                        sys.exit()

                pygame.display.update()


    def opcoes(self):
        while True:
            tela.blit(BG, (0, 0))

            menu_mouse_posicao = pygame.mouse.get_pos()

            botao_texto = get_font(100).render("Opções", True, BRANCO)
            botao_quadrado = botao_texto.get_rect(center=(400, 80))


            botao_opcoes_velocidade_bolinha = Botao(imagem=None, posicao=(400, 250),
                                                    texto="velocidade da bolinha:{}".format(bolinha.velocidade), fonte=get_font(25),
                                                    cor_base=BRANCO, cor_transitoria=VERMELHO)

            botao_opcoes_velocidade_raquete = Botao(imagem=None, posicao=(400, 325),
                                 texto="velocidade das raquetes:{}".format(raquetes.velocidade), fonte=get_font(25),
                                 cor_base=BRANCO, cor_transitoria=VERMELHO)


            botao_voltar = Botao(imagem=None, posicao=(400, 450),
                                 texto="Voltar", fonte=get_font(75), cor_base=BRANCO,
                                 cor_transitoria=VERMELHO)

            for botao in [botao_opcoes_velocidade_bolinha, botao_opcoes_velocidade_raquete, botao_voltar]:
                botao.muda_cor(menu_mouse_posicao)
                botao.update(tela)

            tela.blit(botao_texto, botao_quadrado)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botao_opcoes_velocidade_bolinha.check_click(menu_mouse_posicao):
                        self.bolinha.controla_velocidade()

                    if botao_opcoes_velocidade_raquete.check_click(menu_mouse_posicao):
                        self.raquetes.controla_velocidade()


                    if botao_voltar.check_click(menu_mouse_posicao):
                        self.menu_principal()

                pygame.display.update()


#Instacia Objetos
if __name__ == "__main__":
    bolinha = Bolinha()
    raquetes = Raquetes(bolinha)
    menu = Menu(bolinha, raquetes)

#Roda o jogo
def play():

    mixer.music.load("trilha.mp3")
    mixer.music.play(-1)

    Rodar = True
    while Rodar:

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


#Chama Menu principal
menu.menu_principal()
