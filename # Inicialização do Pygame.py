# Inicialização do Pygame
pygame.init()

# Dimensões da janela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Corrida")
relogio = pygame.time.Clock()

# Carrega a imagem do carro
carro_img = pygame.image.load('carro.png')
carro_img = pygame.transform.scale(carro_img, (40, 50))  # Ajusta o tamanho da imagem

# Posições do carro
x = largura / 2
y = altura / 2

# Contador de movimento
cont = 0

# Loop principal
true = True
while true:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação do carro
    if pygame.key.get_pressed()[K_UP]:
        y -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        y += 5   
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 5

    # Desenha o carro usando a imagem
    carro_rect = tela.blit(carro_img, (x, y))

    # Movimento da calçada
    cont += 5
    if cont > altura:
        cont = -100  # Reinicia o movimento

    # Desenha a calçada
    calçada = pygame.draw.rect(tela, (60, 60, 60), (590, cont, 50, 1000))
    calçada1 = pygame.draw.rect(tela, (60, 60, 60))