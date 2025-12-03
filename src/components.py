from dataclasses import dataclass as component


@component
class Player:
    pass


@component
class Position:
    x: int = 0
    y: int = 0


@component
class Velocity:
    x: int = 0
    y: int = 0


@component
class Display:
    char: str = "?"

