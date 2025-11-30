from components import *
from options import *
import esper
import tcod.context

class ControlProcessor(esper.Processor):
    def process(self):
        pass

class MovementProcessor(esper.Processor):
    def process(self):
        for ent, (vel, pos) in esper.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y

class DisplayProcessor(esper.Processor):
    def __init__(self): 
        tileset = tcod.tileset.load_tilesheet(FONT_PATH, 16, 16, tcod.tileset.CHARMAP_CP437)
        self.context: tcod.context.Context = tcod.context.new(columns=WIDTH, rows=HEIGHT, tileset=tileset)
    def process(self):
        console = tcod.console.Console(WIDTH, HEIGHT)
        for ent, (disp, pos) in esper.get_components(Display, Position):    
            console.print(int(pos.x), int(pos.y), disp.char)
        self.context.present(console)