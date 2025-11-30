from dataclasses import dataclass as component

@component
class Position:
    x: float = 0.0
    y: float = 0.0

@component
class Velocity:
    x: float = 0.0
    y: float = 0.0

@component
class Display:
    char: str = "?"