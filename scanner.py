import token_type


class Scanner:
    def __init__(self, filename):
        with open(filename) as source:
            self.lines = source.read().split('\n')
            for i in range(len(self.lines)):
                self.lines[i] += "\n"
            self.line_index = 0
            self.char_index = 0

    def get_token(self):  # starting state
        char = self.get_char()
        if char == " ":
            return self.get_token()
        elif char == "\n":
            return token_type.TokenType.EOL, char
        elif char == ",":
            return token_type.TokenType.COM, char
        elif char == "a":
            return self.s_1(char)
        elif char == "j":
            return self.s_18(char)
        elif char == "i":
            return self.s_22(char)
        elif char == "l":
            return self.s_7(char)
        elif char == "p":
            return self.s_12(char)
        elif char == "r":
            return self.s_4(char)
        elif char == "=":
            return self.s_5(char)
        elif char == ":":
            return self.s_27(char)
        elif char == "EOF":
            return token_type.TokenType.EOF, char
        elif "0" <= char <= "9" or char == "-":
            return self.s_17(char)
        else:
            raise Exception("Unexpected Token" + char)

    # add
    def s_1(self, word):  # a
        char = self.get_char()
        if char == "d":
            return self.s_2(word + char)

    def s_2(self, word):  # ad
        char = self.get_char()
        if char == "d":
            return self.s_3(word + char)

    def s_3(self, word):  # add
        return token_type.TokenType.ADD, word

    # regs
    def s_4(self, word):
        char = self.get_char()
        if char != " " and char != "\n" and char != ",":
            return self.s_4(word + char)
        self.rollback()
        return token_type.TokenType.REG, word

    # =>
    def s_5(self, word):
        char = self.get_char()
        if char == ">":
            return self.s_6(word + char)

    def s_6(self, word):
        return token_type.TokenType.EQU, word

    def s_7(self, word):
        char = self.get_char()
        if char == "o":
            return self.s_8(word + char)

    def s_8(self, word):
        char = self.get_char()
        if char == "a":
            return self.s_9(word + char)

    def s_9(self, word):
        char = self.get_char()
        if char == "d":
            return self.s_10(word + char)

    def s_10(self, word):
        char = self.get_char()
        if char == "I":
            return self.s_11(word + char)

    def s_11(self, word):
        return token_type.TokenType.LDI, word

    def s_12(self, word):
        char = self.get_char()
        if char == "r":
            return self.s_13(word + char)

    def s_13(self, word):
        char = self.get_char()
        if char == "i":
            return self.s_14(word + char)

    def s_14(self, word):
        char = self.get_char()
        if char == "n":
            return self.s_15(word + char)

    def s_15(self, word):
        char = self.get_char()
        if char == "t":
            return self.s_16(word + char)

    def s_16(self, word):
        return token_type.TokenType.OUT, word

    def s_17(self, word):
        char = self.get_char()
        if char != " " and char != "\n" and char != ",":
            return self.s_17(word + char)
        self.rollback()
        return token_type.TokenType.NUM, word

    def s_18(self, word):
        char = self.get_char()
        if char == "u":
            return self.s_19(word + char)

    def s_19(self, word):
        char = self.get_char()
        if char == "m":
            return self.s_20(word + char)

    def s_20(self, word):
        char = self.get_char()
        if char == "p":
            return self.s_21(word + char)

    def s_21(self, word):
        return token_type.TokenType.JMP, word

    def s_22(self, word):
        char = self.get_char()
        if char == "f":
            return self.s_23(word + char)

    def s_23(self, word):
        char = self.get_char()
        if char == "e":
            return self.s_24(word + char)
        if char == "l":
            return self.s_25(word + char)
        if char == "g":
            return self.s_26(word + char)

    def s_24(self, word):
        return token_type.TokenType.IFE, word

    def s_25(self, word):
        return token_type.TokenType.IFL, word

    def s_26(self, word):
        return token_type.TokenType.IFG, word

    def s_27(self, word):
        return token_type.TokenType.COL, word

    def get_char(self):
        if self.line_index >= len(self.lines):
            return "EOF"
        char = self.lines[self.line_index][self.char_index]
        self.char_index += 1
        if self.char_index >= len(self.lines[self.line_index]):
            self.char_index = 0
            self.line_index += 1
        return char

    def rollback(self):
        self.char_index -= 1
        if self.char_index < 0:
            self.line_index -= 1
            self.char_index = len(self.lines[self.line_index]) - 1

    def jump(self, i):
        self.line_index -= i
        self.char_index = 0
