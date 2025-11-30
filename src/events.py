import esper
import tcod

def handle_events():
    for event in tcod.event.wait():
        if isinstance(event, tcod.event.Quit):
            raise SystemExit
        else:
            continue