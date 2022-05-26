import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):   
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
            sys.exit()

            
def fire_bullets(ai_settings,screen,ship,bullets):
    '''Fire a bullet if limit isn't reaches yet.'''
    #Create a new bullet and add it to the bullets group
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
    '''Respond to keypress and mouse events.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,alien,bullets):
    '''Update images on the screen and flip to the new screen.'''
    screen.fill(ai_settings.screen_bg_color)
    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    pygame.display.flip()
    
def update_bullets(bullets):
    '''Update position of bullets and get rid of bullets.'''
    #Update bullet positions.
    bullets.update()
    #Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)