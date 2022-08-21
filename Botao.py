class Botao:

    def __init__(self, imagem, posicao, texto, fonte, cor_base, cor_transitoria):
        self.imagem = imagem
        self.posicao_x = posicao[0]
        self.posicao_y = posicao[1]
        self.fonte = fonte
        self.cor_base, self.cor_transitoria = cor_base, cor_transitoria
        self.texto = texto
        self.text = fonte.render(self.texto, True, "white")
        if self.imagem is None:
            self.imagem = self.text
        self.rect = self.imagem.get_rect(center = (self.posicao_x, self.posicao_y))
        self.text_rect = self.text.get_rect(center = (self.posicao_x, self.posicao_y))

    def update(self, tela):
        if self.imagem is not None:
            tela.blit(self.imagem, self.rect)
        tela.blit(self.text, self.text_rect)

    def check_click(self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False

    def muda_cor(self, posicao):
        if posicao[0] in range(self.rect.left, self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.fonte.render(self.texto, True, self.cor_transitoria)
        else:
            self.text = self.fonte.render(self.texto, True, self.cor_base)
