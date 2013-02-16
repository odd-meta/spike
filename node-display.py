import pygame
from pygame.locals import *


from spikeGenerator import *
"""
TODO:
during the loop:
    be able to take a list of nodes and render them and their children out as a tree of connected circles
during events:
    have a collision checking deal running for nodes and links, highlight nodes/links when hover
    
    

"""


class App:
    def __init__(self, node_list = []):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1440, 900
        self.node_list = node_list
        self.bgcolor = 0, 0, 0
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._running = True

    def pre_loop(self):
        pass
 
    def on_event(self, event):
        
        
        if event.type == pygame.QUIT:
            self._running = False
            

        elif event.type == pygame.MOUSEMOTION:
            print "mouse at (%d, %d)" % event.pos
            self._display_surf.fill( self.bgcolor )
            pygame.draw.circle(self._display_surf, (255,255,255), event.pos, 64, 0)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print "You released the left mouse button at (%d, %d)" % event.pos
            
    def on_loop(self):
        pass
    
    def on_render(self):
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.pre_loop()
            
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
 
if __name__ == "__main__" :



    """
        figure out algorithm for generating network structure
    """

    generator = spikeGenerator(60)

    node_list = generator.generate()


    theApp = App(node_list)
    theApp.on_execute()
