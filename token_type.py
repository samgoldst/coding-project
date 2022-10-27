import enum


class TokenType(enum.Enum):
    ADD = enum.auto()
    EQU = enum.auto()
    REG = enum.auto()
    EOL = enum.auto()
    COM = enum.auto()
    EOF = enum.auto()
    LDI = enum.auto()
    OUT = enum.auto()
    NUM = enum.auto()
    JMP = enum.auto()
    IFE = enum.auto()
    IFL = enum.auto()
    IFG = enum.auto()
    COL = enum.auto()
