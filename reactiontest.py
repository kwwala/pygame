import pygame
import random
import time
import pygame.freetype as pgft

pygame.init()
screen = pygame.display.set_mode((640, 480)) # configura janela do jogo
pygame.display.set_caption("Reaction Test")
clock = pygame.time.Clock()
running = True
pygame.font.init()

text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

while running:
  # Processamento de eventos (entradas de teclado e mouse)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  if pygame.mouse.get_pressed()[0]:
    screen.fill((196, 48, 61)) # VERMELHO
    draw_text("espera ai irmão", text_font, (255, 255, 255), 220, 150)
    pygame.display.flip()
    time.sleep(random.randrange(3, 5))

    screen.fill((0, 255, 0))
    pygame.display.flip()
    start = time.time()
    
    # screen.fill((95, 217, 100)) # verde 
    while not pygame.mouse.get_pressed()[0]:
      pass  # Wait for the user to click

    if pygame.mouse.get_pressed()[0]:
      end = time.time()
      length = end - start
      pygame.display.flip()
      screen.fill((68, 134, 208)) # azul
      draw_text(f"{length}", text_font, (255, 255, 255), 220, 150)
      pygame.display.flip()

  clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)

pygame.quit()
