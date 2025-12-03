import components as C
import options as O
import esper
import tcod.context


class ControlProcessor(esper.Processor):
    def process(self):
        _, (_, vel) = esper.get_components(C.Player, C.Velocity)[0]
        for event in tcod.event.wait():
            match event:
                case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                    vel.x -= 1
                case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                    vel.x += 1
                case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                    vel.y -= 1
                case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                    vel.y += 1
                case tcod.event.Quit():
                    raise SystemExit


class MovementProcessor(esper.Processor):
    def process(self):
        for _, (vel, pos) in esper.get_components(C.Velocity, C.Position):
            pos.x += vel.x
            pos.y += vel.y
            vel.x = 0
            vel.y = 0


class DisplayProcessor(esper.Processor):
    def __init__(self):
        tileset = tcod.tileset.load_tilesheet(
            O.FONT_PATH, 16, 16, tcod.tileset.CHARMAP_CP437
        )
        self.context: tcod.context.Context = tcod.context.new(
            columns=O.WIDTH, rows=O.HEIGHT, tileset=tileset
        )

    def process(self):
        console = tcod.console.Console(O.WIDTH, O.HEIGHT)
        for ent, (disp, pos) in esper.get_components(C.Display, C.Position):
            console.print(int(pos.x), int(pos.y), disp.char)
        self.context.present(console)
