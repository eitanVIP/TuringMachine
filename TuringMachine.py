from Colors import Colors
from Rule import Rule


class TuringMachine:
    def __init__(self, size: int, rules: list[Rule]):
        self._rules: list[Rule] = rules
        self._board: list[int] = [0] * size
        self._pos: int = size // 2
        self._currentRule: Rule = rules[0]
        self._halted: bool = False
        self._preInstruction: str = ""
        self._prePos: int = self._pos

    def execute(self):
        if self._pos >= len(self._board):
            self._pos -= len(self._board)
        if self._pos < 0:
            self._pos += len(self._board)

        pos = self._pos
        self._prePos = pos
        value = self._board[pos]

        self._preInstruction = self._currentRule.getInstructionStr(value)

        if self._currentRule.isHalt(value):
            self._halted = True
            return

        self._board[pos] = self._currentRule.getWrite(value)
        self._pos += self._currentRule.getMove(value)
        self._currentRule = self._currentRule.getNextRule(value)

    def isHalted(self):
        return self._halted

    def setPos(self, pos: int):
        self._pos = pos

    def __repr__(self):
        board = "["
        for i in self._board:
            if i == 1:
                board += f"{Colors.GREEN}{1}{Colors.END}"
            else:
                board += f"{Colors.RED}{0}{Colors.END}"
        board += "]"

        pos = f"{Colors.YELLOW}pos- {self._prePos}{Colors.END}"

        return f"{Colors.BOLD}TuringMachine{Colors.END}({board}, {pos}, {self._preInstruction}, {self._currentRule}, {self._rules})"