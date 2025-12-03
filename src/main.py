import components as C
import systems as S
import events as EV
import esper


def main() -> None:
    player: int = esper.create_entity(
        C.Player(),
        C.Velocity(x=0, y=0),
        C.Position(x=5, y=5),
        C.Display(char="@"),
    )
    esper.add_processor(S.MovementProcessor())
    esper.add_processor(S.DisplayProcessor())
    esper.add_processor(S.ControlProcessor())
    while True:
        esper.process()


if __name__ == "__main__":
    main()
