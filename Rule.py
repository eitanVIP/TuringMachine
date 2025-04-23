import random

from Colors import Colors


class Rule:
    def __init__(self, name: str, write0: int, move0: int, halt0: bool, write1: int, move1: int, halt1: bool):
        self._name = name

        self._write0: int = write0
        self._move0: int = move0
        self._nextRule0: 'Rule' = None

        self._write1: int = write1
        self._move1: int = move1
        self._nextRule1: 'Rule' = None

        self._halt0: bool = halt0
        self._halt1: bool = halt1

    def getWrite(self, value: int) -> int:
        return self._write0 if value == 0 else self._write1

    def getMove(self, value: int) -> int:
        return self._move0 if value == 0 else self._move1

    def getNextRule(self, value: int) -> 'Rule':
        return self._nextRule0 if value == 0 else self._nextRule1

    def isHalt(self, value: int) -> bool:
        return self._halt0 if value == 0 else self._halt1

    def setNextRule(self, nextRule0: 'Rule', nextRule1: 'Rule'):
        self._nextRule0 = nextRule0
        self._nextRule1 = nextRule1

    @classmethod
    def randomRule(cls, name: str):
        return cls(name, random.randint(0, 1), random.randint(0, 2) - 1, True if random.randint(0, 3) == 0 else False, random.randint(0, 1), random.randint(0, 2) - 1, True if random.randint(0, 3) == 0 else False)

    def __repr__(self):
        match self._move0:
            case -1:
                move0 = "L"
            case 1:
                move0 = "R"
            case _:
                move0 = "S"

        match self._move1:
            case -1:
                move1 = "L"
            case 1:
                move1 = "R"
            case _:
                move1 = "S"

        nextRule0 = self._nextRule0._name if self._nextRule0 is not None else ''
        nextRule1 = self._nextRule1._name if self._nextRule1 is not None else ''

        if self._halt0:
            return f"{Colors.BOLD}Rule{Colors.END}(0: Halt, 1: {Colors.RED}{self._write1}{Colors.END}{Colors.YELLOW}{move1}{Colors.END}{Colors.BLUE}{nextRule1}{Colors.END})"

        elif self._halt1:
            return f"{Colors.BOLD}Rule{Colors.END}(0: {Colors.RED}{self._write0}{Colors.END}{Colors.YELLOW}{move0}{Colors.END}{Colors.BLUE}{nextRule0}{Colors.END}, 1: Halt)"

        return f"{Colors.BOLD}Rule{Colors.END}(0: {Colors.RED}{self._write0}{Colors.END}{Colors.YELLOW}{move0}{Colors.END}{Colors.BLUE}{nextRule0}{Colors.END}, 1: {Colors.RED}{self._write1}{Colors.END}{Colors.YELLOW}{move1}{Colors.END}{Colors.BLUE}{nextRule1}{Colors.END})"

    def getInstructionStr(self, value: int):
        match self._move0:
            case -1:
                move0 = "L"
            case 1:
                move0 = "R"
            case _:
                move0 = "S"

        match self._move1:
            case -1:
                move1 = "L"
            case 1:
                move1 = "R"
            case _:
                move1 = "S"

        nextRule0 = self._nextRule0._name if self._nextRule0 is not None else ''
        nextRule1 = self._nextRule1._name if self._nextRule1 is not None else ''

        match value:
            case 0:
                if self._halt0:
                    return f"{Colors.BOLD}Instruction(Halt){Colors.END}"
                return f"{Colors.BOLD}Instruction{Colors.END}({Colors.RED}{self._write0}{Colors.END}{Colors.YELLOW}{move0}{Colors.END}{Colors.BLUE}{nextRule0}{Colors.END})"
            case 1:
                if self._halt1:
                    return f"{Colors.BOLD}Instruction{Colors.END}(Halt)"
                return f"{Colors.BOLD}Instruction{Colors.END}({Colors.RED}{self._write1}{Colors.END}{Colors.YELLOW}{move1}{Colors.END}{Colors.BLUE}{nextRule1}{Colors.END})"
