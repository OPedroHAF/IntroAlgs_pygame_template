import pygame
import random 

def main():
    pygame.init()

    tela= pygame.display.set_mode([900, 600])
    pygame.display.set_caption("Iniciando jogo")
    frame=pygame.time.Clock()
    cor=(6, 1, 51)

    sup=pygame.Surface((870, 560))
    sup.fill((0, 0, 0))

    estrelas= []

    for i in range (100):
        x=random.randint(0,900)
        y = random.randint(0, 600)

        velocidade = random.randint(1, 5)

        estrelas.append([x, y, velocidade])

    ativo = True 

    while ativo:    
        for evento in pygame.event.get():
            if evento.type== pygame.QUIT:
                ativo= False

        frame.tick(30)

        tela.fill(cor)

        for estrela in estrelas:

            estrela[1] += estrela[2]

            if estrela[1] > 600:
                estrela[1] = 0
                estrela[0] = random.randint(0, 900)

            pygame.draw.circle(
                tela,
                (255, 255, 255),
                (estrela[0], estrela[1]),
                2
            )

        tela.blit(sup, (15, 20))

        pygame.display.update()

    pygame.quit()

main()
