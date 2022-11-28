import pygame
from random import randint, random
import math
pygame.init()

WIDTH = 1000
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('N Body Simulation')

AU = 149e9                                                                     # In m
G = 6.67e-11                                                                   # In N*m/kg
DAY = 8640                                                                     # Seconds in a day
SCALE = 300 / AU                                                               # How many pixels per AU

class Body:

    def __init__(self, x, y, color, mass):
        self.x = x
        self.y = y
        self.color = color
        self.mass = mass

        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0


    def draw(self, win):                                                       # Fits x and y into scale and prints on the screen
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))
                
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        pygame.draw.circle(win, self.color, (x, y), 10)
        

    def attraction(self, other):                                               # Calculates the forces acting on the bodies
        other_x = other.x
        other_y = other.y
        
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        
        return force_x, force_y
    
    def movement(self, objects):                                               # Translates the forces into movements
        total_fx = 0
        total_fy = 0
        for object in objects:
            if self == object:
                continue
            fx, fy = self.attraction(object)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * DAY
        self.y_vel += total_fy / self.mass * DAY

        self.x += self.x_vel * DAY
        self.y += self.y_vel * DAY
        self.orbit.append((self.x, self.y))

def main():
    run = True
    clock = pygame.time.Clock()
    
    body1 = Body(random() * AU, 0, (randint(0, 255), randint(0, 255), randint(0, 255)), randint(1e10, 1e30))
    body1.y_vel = randint(-50000, 50000)
    
    body2 = Body(random() * AU, 0, (randint(0, 255), randint(0, 255), randint(0, 255)), randint(1e10, 1e30))
    body2.y_vel = randint(-50000, 50000)
    
    body3 = Body(random() * AU, 0, (randint(0, 255), randint(0, 255), randint(0, 255)), randint(1e10, 1e30))
    body3.y_vel = randint(-50000, 50000)
    
    bodies = [body1, body2, body3]

    
    while run:
        clock.tick(10)
        SCREEN.fill((0, 0, 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        for body in bodies:
            body.movement(bodies)
            body.draw(SCREEN)
            
        
        pygame.display.update()
        
    pygame.quit()
    
main()
