#Morco, Cathleen Jan M., BSCPE 1-5 , 04/15/2023
#A program that uses The Vigenère Cipher

#Imports the pygame module
import pygame

#Sets the value for the width and height of the display screen
W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
pygame.display.set_caption("Vigenère Cipher")
clock = pygame.time.Clock()

#RGB example values
black = (0,0,0)
white = (255,255,255)

#The rate of change in colors
col_spd = 1

#The color directory & its values
col_dir =[[-1,1,1],[-1,1,-1],[-1,1,1],[-1,1,-1]]
def_col = [[120,120,240],[140,140,240],[160,160,220]]

#Initialized values for functions
minimum = 0
maximum = 255

#Draws the text
def draw_text(text, size, col, x, y):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, col)
    text_rect=text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface, text_rect)
    
#Creates the color change

#Combines the color change and draw text into one function

# Initializing pygame

# Ask for user input

# Make sure the keyword is long enough

# Encrypt the message

# Format the ciphertext into three lines

#Informs the user of the output

#Runs the program
