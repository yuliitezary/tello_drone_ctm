import pygame
from time import sleep

def init():
    pygame.init()
    win = pygame.display.set_mode((200,200))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("A fost apasata tasta stanga")
    if getKey("RIGHT"):
        print("A fost apasata tasta dreapta")
    if getKey("UP"):
        print("A fost apasata tasta sus")
    if getKey("DOWN"):
        print("A fost apasata tasta jos")

if __name__ == "__main__":
    init()
    while True:
        main()
        sleep(0.5)