import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Two Sided Border Button Example')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600), 'data/themes/two_sided_border_theme.json')

# Create a button with borders only on left and bottom sides
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (200, 50)),
                                            text='Hello',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
