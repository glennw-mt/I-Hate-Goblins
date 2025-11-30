import tcod.console
import tcod.context
import tcod.event
import tcod.tileset
from components import *
from systems import *
from events import *
import esper

def main() -> None:
    player: int = esper.create_entity(
        Velocity(x=0.0, y=0.0), 
        Position(x=5.0, y=5.0),
        Display(char="@")
    )
    esper.add_processor(MovementProcessor())
    esper.add_processor(DisplayProcessor())
    esper.add_processor(ControlProcessor())
    while True:
        esper.process()
        handle_events()
        


if __name__ == "__main__":
    main()
