import scanner
import token_type
from token_type import TokenType
from collections import defaultdict


class Parser:
    def __init__(self, filename):
        self.scan = scanner.Scanner(filename)
        self.regs = defaultdict(int)
        token = None
        while True:
            token = self.scan.get_token()[0]
            if token == TokenType.EOF:
                break
            if token == TokenType.EOL:
                continue
            self.get_first_token(token)

    def ADD(self):
        token1, reg1 = self.scan.get_token()  # 1st term
        self.scan.get_token()
        token2, reg2 = self.scan.get_token()  # 2nd term
        self.scan.get_token()
        _, reg3 = self.scan.get_token()  # destination
        sum = 0
        if token1 == TokenType.REG:
            sum += self.regs[int(reg1[1:])]
        else:
            sum += int(reg1)
        if token2 == TokenType.REG:
            sum += self.regs[int(reg2[1:])]
        else:
            sum += int(reg2)
        self.regs[int(reg3[1:])] = sum

    def LOADI(self):
        _, reg1 = self.scan.get_token()
        _, reg2 = self.scan.get_token()
        self.regs[int(reg2[1:])] = int(reg1)

    def PRINT(self):
        _, reg1 = self.scan.get_token()
        print(self.regs[int(reg1[1:])])

    def JUMP(self):
        token1, reg1 = self.scan.get_token()
        if token1 == TokenType.REG:
            self.scan.jump(self.regs[int(reg1[1:])])
        if token1 == TokenType.NUM:
            self.scan.jump(int(reg1))

    def IF(self, type):
        token1, reg1 = self.scan.get_token()  # 1st term
        self.scan.get_token()
        token2, reg2 = self.scan.get_token()  # 2nd term
        self.scan.get_token()
        num1 = None
        num2 = None
        if token1 == TokenType.REG:
            num1 = self.regs[int(reg1[1:])]
        else:
            num1 = int(reg1)
        if token2 == TokenType.REG:
            num2 = self.regs[int(reg2[1:])]
        else:
            num2 = int(reg2)
        if not ((num1 == num2 and type == "e") or (num1 > num2 and type == "g") or (num1 < num2 and type == "l")):
            while self.scan.get_token()[0] not in {token_type.TokenType.EOL, token_type.TokenType.EOF}:
                pass

    def get_first_token(self, token):
        if token == TokenType.ADD:
            self.ADD()
        if token == TokenType.LDI:
            self.LOADI()
        if token == TokenType.OUT:
            self.PRINT()
        if token == TokenType.JMP:
            self.JUMP()
        if token == TokenType.IFE:
            self.IF("e")
        if token == TokenType.IFG:
            self.IF("g")
        if token == TokenType.IFL:
            self.IF("l")



parser = Parser("code.txt")
