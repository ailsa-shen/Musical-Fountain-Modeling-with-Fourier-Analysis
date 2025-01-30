import pygame
import sys
import random
pygame.init() 

screen_width = 800
screen_height = 600
background_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height)) # create a display Surface

music_file = path_to_file
peaks = proc_wav(music_file) # get the peaks of the music signal using the proc_wav function

# scaling the peaks between 0 and 480
min_value = min(peaks)
max_value = max(peaks)
new_min = 0
new_max = 480
scaled_peaks = [(x - min_value) / (max_value - min_value) * (new_max - new_min) + new_min for x in peaks]

pygame.mixer.music.load(music_file) # load music file into pygame mixer

# define a Particle class which inherits from pygame's Sprite class
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.image = pygame.Surface((2, 2))
        self.image.fill((255, 255, 255)) 
        self.rect = self.image.get_rect() 
        self.rect.center = (x, y) 
        self.vel_x = random.uniform(-1, 1) 
        self.vel_y = random.uniform(-5, -1) 
        self.gravity = 0.1
    def update(self): # method to update the position/state of the particle each frame
        self.vel_y += self.gravity 
        self.rect.x += self.vel_x 
        self.rect.y += self.vel_y 
        if self.rect.bottom > screen_height:
            self.kill() # remove the particle if it goes off the bottom of the screen

particles = pygame.sprite.Group() 
running = True # flag to keep the main loop running

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play() 

    index = 0
    time = pygame.mixer.music.get_pos() / 1000.0 
    height = screen_height - 2 
    new_height = screen_height - 2 
    interval = 0 

    # Loop to update the screen while the music is playing
    while pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000.0
        if (current_time - time) >= 0.1:
            new_height = screen_height - scaled_peaks[index] #update height based on music peaks
            index += 1
            time = current_time
            interval = (new_height - height) / 200
            print(interval)
        if(abs(new_height - height) > 1): 
            height += interval
        particle = Particle(screen_width // 2, height) # particle creation and update
        particles.add(particle)
        particles.update()

        screen.fill(background_color)
        particles.draw(screen)
        pygame.display.flip()
        height -= 0.01 

    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()